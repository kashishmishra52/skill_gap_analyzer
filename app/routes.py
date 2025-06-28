from flask import Blueprint, render_template, request, url_for
import os
from app.resume_parser import extract_text_from_pdf
from app.analyzer import analyze_skills, get_recommendations, score_resume
from app.visualizer import create_skill_graph

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('resume')
        job_input = request.form.get('job', '')

        if not file or not job_input.strip():
            return render_template('error.html', message="Please upload a resume and specify job roles.")

        save_path = os.path.join('data', file.filename)
        file.save(save_path)

        resume_text = extract_text_from_pdf(save_path)
        job_roles = [job.strip().lower() for job in job_input.split(',') if job.strip()]

        if not job_roles:
            return render_template('error.html', message="No valid job roles provided.")

        matched, missing, tas_score = analyze_skills(resume_text, job_roles)
        resume_score, resume_tips = score_resume(resume_text)
        recommendations = get_recommendations(missing)

        # Create pie chart
        pie_chart_path = os.path.join('static', 'skill_pie.png')
        create_skill_graph(matched, missing, output_path=pie_chart_path)

        return render_template(
            'result.html',
            matched=matched,
            missing=missing,
            tas_score=tas_score,
            resume_score=resume_score,
            resume_tips=resume_tips,
            jobs=', '.join([job.title() for job in job_roles]),
            recommendations=recommendations,
            pie_chart_url=url_for('static', filename='skill_pie.png')
        )

    return render_template('index.html')

