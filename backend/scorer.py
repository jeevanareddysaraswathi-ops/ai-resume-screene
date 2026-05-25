from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from parser import extract_text
from nlp import preprocess
import os

def score_resumes(job_description, resume_folder="uploads"):
    # Preprocess job description
    jd_processed = preprocess(job_description)
    jd_text = jd_processed["processed_text"]

    results = []

    # Loop through all resumes in uploads folder
    for filename in os.listdir(resume_folder):
        if filename.endswith(".docx") or filename.endswith(".pdf"):
            file_path = os.path.join(resume_folder, filename)

            # Extract and preprocess resume text
            raw_text = extract_text(file_path)
            resume_processed = preprocess(raw_text)
            resume_text = resume_processed["processed_text"]

            # TF-IDF + Cosine Similarity
            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform([jd_text, resume_text])
            score = cosine_similarity(vectors[0], vectors[1])[0][0]

            # Get matched skills
            jd_skills = set(jd_processed["skills"])
            resume_skills = set(resume_processed["skills"])
            matched_skills = list(jd_skills & resume_skills)

            results.append({
                "candidate": filename.replace("_Resume.docx", "").replace("_", " "),
                "filename": filename,
                "score": round(float(score) * 100, 2),
                "matched_skills": matched_skills,
                "total_skills": len(resume_skills)
            })

    # Rank by score
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results