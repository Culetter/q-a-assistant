from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
import ollama

DB_PATH = "DB"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def get_answer(query, k=3):
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(DB_PATH, embedding_function, allow_dangerous_deserialization=True)

    results = db.similarity_search_with_score(query, k)
    
    for doc, score in results:
        print(f"{doc.page_content}\nScore: {score}\n-------------------\n")

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    sources = list(set([doc.metadata.get("source", "") for doc, _ in results]))
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query)

    model = "mistral"
    client = ollama.Client()

    response = client.generate(model=model, prompt=prompt)

    return response.response, sources