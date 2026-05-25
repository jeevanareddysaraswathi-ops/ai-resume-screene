import spacy
import re

nlp = spacy.load("en_core_web_sm")

SKILLS_LIST = [
    "python", "machine learning", "deep learning", "nlp", "tensorflow",
    "pytorch", "scikit-learn", "pandas", "numpy", "sql", "java",
    "javascript", "react", "node.js", "docker", "kubernetes", "git",
    "data analysis", "computer vision", "bert", "opencv", "statistics",
    "matplotlib", "fastapi", "flask", "html", "css", "mongodb", "ai",
    "xgboost", "word2vec", "data science", "neural networks"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_skills(text):
    text_lower = text.lower()
    found_skills = []
    for skill in SKILLS_LIST:
        if skill in text_lower:
            found_skills.append(skill)
    return found_skills

def preprocess(text):
    cleaned = clean_text(text)
    doc = nlp(cleaned)
    tokens = [token.lemma_ for token in doc
              if not token.is_stop and not token.is_punct and len(token.text) > 2]
    skills = extract_skills(text)
    processed_text = " ".join(tokens)
    return {
        "cleaned_text": cleaned,
        "processed_text": processed_text,
        "skills": skills
    }