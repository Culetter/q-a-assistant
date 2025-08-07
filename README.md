# Question-Answering Assistant

A local AI-powered question-answering assistant that uses your own documents as a knowledge base. It loads .md files from a local folder, splits them into chunks, indexes them using FAISS, and allows you to ask natural language questions via a simple web interface.

# Project Structure
```
├── /data                # Input data
├── /DB                  # Stored FAISS vector database
├── /src
│   ├── pipeline.py      # Loads, splits, embeds, and saves documents
│   └── run_ollama.py    # Connects to a local LLM (e.g., via Ollama) to handle queries
├── /ui                  # Web interface
│   ├── /static          # Static assets
│   ├── /templates       # HTML templates rendered by FastAPI
│   └── /app.py          # FastAPI server handling routes and Q&A requests
├── /requirements.txt    # Python dependencies for the entire project
```

# Installation
1. Clone the repository:
```bash
git clone https://github.com/Culetter/q-a-assistant
cd q-a-assistant
```
2. Install the dependencies
```
pip install -r requirements.txt
```

# Usage
To use this assistant, you need to have **Ollama** and the **Mistral** model installed.

1. Run the FastAPI application using the Uvicorn server:
```
uvicorn ui.app:app --reload
```
2. After running the server, open your browser and go to:
```
http://localhost:8000/
```

To add new files to the database:
1. Copy your .md files into the data folder.
2. In your browser, click Update Data in the sidebar.
This will reload the documents and update the vector database.

# Tech Stack
* Ollama with mistral model (local LLM)
* LangChain for document parsing & chunking
* FAISS for similarity search
* HuggingFace Embeddings (all-MiniLM-L6-v2)
* FastAPI backend
* HTML/CSS/JavaScript frontend

# Author
**Nazarii Lozynskyi**  
[@Culetter](https://github.com/Culetter)
