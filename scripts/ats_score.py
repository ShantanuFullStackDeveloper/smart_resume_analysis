import numpy as np
from collections import Counter

def calculate_ats_score(resume_text, job_desc):
    # Tokenize and count word frequency
    resume_words = Counter(resume_text.lower().split())
    job_words = Counter(job_desc.lower().split())

    # Get common words and calculate score
    common_words = set(resume_words.keys()) & set(job_words.keys())
    score = len(common_words) / len(job_words.keys()) * 100
    return round(score, 2)
