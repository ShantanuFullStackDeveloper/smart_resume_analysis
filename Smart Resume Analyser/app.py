from flask import Flask, request, render_template, redirect, url_for
import os
from scripts.resume_parser import extract_text
from scripts.ats_score import calculate_ats_score
from scripts.recommendations import generate_recommendations

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

        # Extract text from resume
        resume_text = extract_text(filepath)

        # ATS Score Calculation
        job_desc = request.form['job_desc']
        ats_score = calculate_ats_score(resume_text, job_desc)

        # Recommendations
        recommendations = generate_recommendations(resume_text)

        return render_template('results.html', ats_score=ats_score, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
