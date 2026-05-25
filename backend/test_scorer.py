from scorer import score_resumes

job_description = """
We need a Python developer with Machine Learning, NLP, and Deep Learning skills.
Experience with TensorFlow, Scikit-learn, and data analysis is required.
Knowledge of BERT and computer vision is a plus.
"""

results = score_resumes(job_description)

print("=" * 50)
print("CANDIDATE RANKING RESULTS")
print("=" * 50)

for i, r in enumerate(results):
    print(f"\nRank {i+1}: {r['candidate']}")
    print(f"  Score: {r['score']}%")
    print(f"  Matched Skills: {r['matched_skills']}")