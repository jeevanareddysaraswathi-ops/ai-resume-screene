from docx import Document
import os

def create_sample_resumes():
    resumes = [
        {
            "name": "Alice_Johnson",
            "content": """Alice Johnson
Email: alice@email.com | Phone: 123-456-7890

SKILLS
Python, Machine Learning, Deep Learning, TensorFlow, NLP, Scikit-learn, SQL, Data Analysis

EXPERIENCE
Machine Learning Engineer - TechCorp (2021-2024)
- Built ML models for customer prediction with 92% accuracy
- Developed NLP pipelines for text classification
- Used TensorFlow and Scikit-learn for model training

EDUCATION
B.Tech Computer Science - IIT Hyderabad (2021)

PROJECTS
- Sentiment Analysis using BERT
- Image Classification using CNN
"""
        },
        {
            "name": "Bob_Smith",
            "content": """Bob Smith
Email: bob@email.com | Phone: 123-456-7891

SKILLS
Java, Spring Boot, MySQL, REST API, Docker, Kubernetes, Git

EXPERIENCE
Backend Developer - InfoSys (2020-2024)
- Developed REST APIs using Spring Boot
- Managed MySQL databases
- Deployed applications using Docker and Kubernetes

EDUCATION
B.Tech Information Technology - JNTU (2020)

PROJECTS
- Employee Management System
- Online Banking API
"""
        },
        {
            "name": "Priya_Sharma",
            "content": """Priya Sharma
Email: priya@email.com | Phone: 123-456-7892

SKILLS
Python, Data Science, Machine Learning, Pandas, NumPy, Matplotlib, SQL, Statistics

EXPERIENCE
Data Scientist - Analytics India (2022-2024)
- Analyzed large datasets using Pandas and NumPy
- Built predictive models using Scikit-learn
- Created data visualizations using Matplotlib

EDUCATION
M.Tech Data Science - BITS Pilani (2022)

PROJECTS
- Customer Churn Prediction
- Sales Forecasting Model
"""
        },
        {
            "name": "Rahul_Verma",
            "content": """Rahul Verma
Email: rahul@email.com | Phone: 123-456-7893

SKILLS
React, JavaScript, HTML, CSS, Node.js, MongoDB, Git, Figma

EXPERIENCE
Frontend Developer - WebSolutions (2021-2024)
- Built responsive web applications using React
- Designed UI components using HTML and CSS
- Integrated REST APIs using JavaScript

EDUCATION
B.Tech Computer Science - VIT (2021)

PROJECTS
- E-commerce Website
- Portfolio Website Builder
"""
        },
        {
            "name": "Sneha_Reddy",
            "content": """Sneha Reddy
Email: sneha@email.com | Phone: 123-456-7894

SKILLS
Python, AI, Deep Learning, Computer Vision, OpenCV, PyTorch, NLP, BERT

EXPERIENCE
AI Engineer - DeepMind Solutions (2021-2024)
- Developed computer vision models using OpenCV and PyTorch
- Built NLP applications using BERT and transformers
- Trained deep learning models for image recognition

EDUCATION
M.Tech Artificial Intelligence - IIT Bombay (2021)

PROJECTS
- Face Recognition System
- Object Detection using YOLO
- Text Summarization using BERT
"""
        }
    ]

    os.makedirs("backend/uploads", exist_ok=True)

    for resume in resumes:
        doc = Document()
        doc.add_paragraph(resume["content"])
        file_path = f"backend/uploads/{resume['name']}_Resume.docx"
        doc.save(file_path)
        print(f"Created: {file_path}")

    print("\nAll sample resumes created successfully!")

create_sample_resumes()