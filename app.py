from flask import Flask, request, render_template, redirect, url_for
import os
from scripts.resume_parser import extract_text
from scripts.ats_score import calculate_ats_score
from scripts.recommendations import generate_recommendations
from utils import (
    extract_basic_info,
    extract_skills,
    recommend_skills,
    provide_feedback,
    evaluate_experience,
    evaluate_project_quality
)

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Upload and Analyze Resume
@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return redirect(request.url)

    file = request.files['resume']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Extract text from PDF/Docx file
        text = extract_text(filepath)

        # Call new functions from utils.py
        basic_info = extract_basic_info(text)
        found_skills = extract_skills(text)
        recommended_skills = recommend_skills(found_skills)
        tips = provide_feedback(text, found_skills)
        experience_eval = evaluate_experience(text)
        project_eval = evaluate_project_quality(text)

        # Handle Job Description (if provided)
        job_desc = request.form.get('job_desc', '')  # ✅ Fix applied
        ats_score = 0

        if job_desc:
            ats_score = calculate_ats_score(text, job_desc)

        # Recommendations
        recommendations = generate_recommendations(text)

        return render_template(
            'results.html',
            ats_score=ats_score,
            recommendations=recommendations,
            basic_info=basic_info,
            found_skills=found_skills,
            recommended_skills=recommended_skills,
            tips=tips,
            experience_eval=experience_eval,
            project_eval=project_eval
        )


if __name__ == '__main__':
    app.run(debug=True)
