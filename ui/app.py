from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.pipeline import generate_data_store, get_files
from src.run_ollama import get_answer

app = FastAPI()

app.mount("/static", StaticFiles(directory="ui/static"), name="static")
templates = Jinja2Templates(directory="ui/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/ask")
def ask(q: str = Query(..., description="Your question")):
    response, sources = get_answer(q)
    return JSONResponse(content={"answer": response.strip(), "sources": sources})

@app.get("/load")
def load(b: bool = Query(..., description="Generation status")):
    if b: generate_data_store()
    files = get_files()

    return JSONResponse(content={"files": files})