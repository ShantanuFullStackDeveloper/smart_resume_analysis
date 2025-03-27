from fuzzywuzzy import fuzz

# Predefined skill sets for matching
career_data = {
    "Data Scientist": ["python", "machine learning", "data analysis", "nlp"],
    "Web Developer": ["html", "css", "javascript", "django", "flask"],
    "AI Engineer": ["deep learning", "tensorflow", "pytorch", "nlp"],
    "DevOps Engineer": ["docker", "kubernetes", "ci/cd", "aws"]
}

def generate_recommendations(resume_text):
    recommendations = []
    for career, skills in career_data.items():
        match_score = fuzz.token_set_ratio(resume_text.lower(), ' '.join(skills))
        if match_score > 50:
            recommendations.append({"career": career, "match_score": match_score})

    # Sort by match score
    recommendations = sorted(recommendations, key=lambda x: x['match_score'], reverse=True)
    return recommendations
