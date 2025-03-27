import re
 
# 1. Extract Basic Information
def extract_basic_info(text):
    name_pattern = r"Name[:\s]*(.*)"
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}"
    phone_pattern = r"\(?\+?[0-9]*\)?[-.\s]?[0-9]+[-.\s]?[0-9]+"

    name_match = re.search(name_pattern, text)
    email_match = re.findall(email_pattern, text)
    phone_match = re.findall(phone_pattern, text)

    return {
        "Name": name_match.group(1) if name_match else "N/A",
        "Email": email_match[0] if email_match else "N/A",
        "Phone": phone_match[0] if phone_match else "N/A"
    }

# 2. Extract Skills
def extract_skills(text):
    skills_list = ["Python", "Machine Learning", "Data Analysis", "Flask", "HTML", "CSS", "SQL"]
    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    return found_skills

# 3. Recommend Skills
def recommend_skills(found_skills):
    skill_recommendations = {
        "Python": ["Django", "FastAPI"],
        "Machine Learning": ["TensorFlow", "Keras"],
        "Data Analysis": ["Pandas", "NumPy", "Matplotlib"],
    }

    recommended_skills = []
    for skill in found_skills:
        if skill in skill_recommendations:
            recommended_skills.extend(skill_recommendations[skill])
    
    return list(set(recommended_skills))  # Avoid duplicates

# 4. Provide Tips and Ideas
def provide_feedback(text, found_skills):
    tips = []

    if len(text) < 500:
        tips.append("Consider adding more content to highlight your experience.")
    
    if "Python" not in found_skills:
        tips.append("Python is a valuable skill. Consider adding it if relevant.")
    
    if "Machine Learning" in found_skills and "Data Analysis" not in found_skills:
        tips.append("Since you know Machine Learning, adding Data Analysis would complement your skillset.")
    
    if not any(skill in text.lower() for skill in ["communication", "leadership", "teamwork"]):
        tips.append("Soft skills like communication and teamwork can enhance your resume.")
    
    return tips

import re

# Existing functions...

# 5. Evaluate Experience
def evaluate_experience(text):
    exp_pattern = r"(\d+)\s*(?:years?|yrs|Yrs|Years) of experience"
    exp_match = re.findall(exp_pattern, text, re.IGNORECASE)

    if exp_match:
        exp_years = max([int(year) for year in exp_match])
        if exp_years >= 5:
            return f"Strong experience with {exp_years} years in the industry."
        elif exp_years >= 2:
            return f"Moderate experience with {exp_years} years of expertise."
        else:
            return f"Basic experience with {exp_years} year(s) in the field."
    return "Experience information not found or insufficient."

# 6. Evaluate Project Quality
def evaluate_project_quality(text):
    project_keywords = ["project", "developed", "built", "created", "designed"]
    technologies = ["Python", "Flask", "Machine Learning", "AI", "NLP", "Django"]

    project_count = sum(text.lower().count(keyword) for keyword in project_keywords)
    tech_count = sum(text.lower().count(tech.lower()) for tech in technologies)

    if project_count >= 3 and tech_count >= 3:
        return "The resume shows strong project work with relevant technologies."
    elif project_count >= 1 and tech_count >= 1:
        return "The resume mentions projects but could elaborate more on relevant technologies."
    else:
        return "Project work or relevant technologies are not clearly mentioned."
