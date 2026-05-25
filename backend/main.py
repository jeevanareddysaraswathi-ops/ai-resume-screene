from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from scorer import score_resumes
from parser import extract_text

app = FastAPI(title="AI Resume Screener")

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/app")
def serve_frontend():
    return FileResponse("frontend/index.html")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")

@app.get("/")
def home():
    return {"message": "AI Resume Screener API is running!"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"message": f"Resume '{file.filename}' uploaded successfully!"}

@app.post("/rank-candidates")
async def rank_candidates(job_description: str = Form(...)):
    results = score_resumes(job_description, resume_folder=UPLOAD_FOLDER)
    return {"candidates": results}