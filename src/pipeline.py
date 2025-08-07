from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

import os
import shutil

DATA_PATH = 'data'
DB_PATH = "DB"

def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)
    
    return chunks

def save_to_chroma(chunks: list[Document]):
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)
    
    vectorstore = FAISS.from_documents(chunks, HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
    vectorstore.save_local(DB_PATH)

    print(f"Saved {len(chunks)} chunks to {DB_PATH}.")

def search(query, k=4):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

    results = vectorstore.similarity_search_with_relevance_scores(query, k=k)
    
    return results

def get_files():
    if not os.path.exists(DB_PATH):
        return []

    vectorstore = FAISS.load_local(DB_PATH, HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"), allow_dangerous_deserialization=True)
    documents = vectorstore.docstore._dict.values()
    filenames = {
        os.path.basename(doc.metadata.get('source'))
        for doc in documents
        if 'source' in doc.metadata
    }

    return list(filenames)