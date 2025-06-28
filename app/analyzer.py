import json
import re
from app.utils import clean_text

def normalize_skill(skill):
    """Normalize skill string for matching: lowercase, no dots or spaces."""
    return skill.lower().replace('.', '').replace(' ', '')

def load_skills():
    with open('data/skills.json', 'r') as file:
        return json.load(file)

def analyze_skills(resume_text, job_roles):
    resume_text = clean_text(resume_text).lower()  # Normalize the resume text

    # Load skill data
    all_skills = load_skills()

    # Aggregate skills from multiple roles
    aggregated_skills = {}
    for role in job_roles:
        role = role.strip().lower()
        role_skills = all_skills.get(role, {})
        for skill, weight in role_skills.items():
            if skill in aggregated_skills:
                aggregated_skills[skill] = max(aggregated_skills[skill], weight)
            else:
                aggregated_skills[skill] = weight

    # Prepare normalized resume text for skill matching
    # We'll check if normalized skill appears as substring in resume text
    matched = []
    missing = []
    matched_weight = 0
    total_weight = sum(aggregated_skills.values())

    for skill, weight in aggregated_skills.items():
        skill_norm = normalize_skill(skill)
        # Check if normalized skill substring exists in normalized resume text (also normalized)
        if skill_norm in normalize_skill(resume_text):
            matched.append(skill)
            matched_weight += weight
        else:
            missing.append(skill)

    tas_score = round((matched_weight / total_weight) * 100, 2) if total_weight > 0 else 0

    return matched, missing, tas_score

def load_course_links():
    with open('data/course_links.json', 'r') as file:
        return json.load(file)

def get_recommendations(missing_skills):
    course_links = load_course_links()
    recommendations = {}
    for skill in missing_skills:
        if skill in course_links:
            recommendations[skill] = course_links[skill]
    return recommendations

def score_resume(resume_text):
    score = 0
    tips = []

    text = resume_text.lower()

    # 1. Check for email
    if re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", resume_text):
        score += 10
    else:
        tips.append("Add an email address to your resume.")

    # 2. Check for phone number
    if re.search(r"\+?\d[\d\s\-]{8,}", resume_text):
        score += 10
    else:
        tips.append("Add a valid phone number.")

    # 3. Check for important sections with multiple aliases for each section
    section_aliases = {
        'education': ['education'],
        'experience': ['experience', 'internship', 'work experience', 'professional experience'],
        'project': ['project', 'projects'],
        'skill': ['skill', 'skills'],
    }

    found_sections = []
    for section, aliases in section_aliases.items():
        if any(alias in text for alias in aliases):
            found_sections.append(section)
            score += 5
        else:
            tips.append(f"Add a section for {section.title()}.")

    # 4. Resume length (approximate words)
    word_count = len(text.split())
    if 300 <= word_count <= 800:
        score += 20
    elif word_count < 300:
        tips.append("Your resume looks too short. Add more content.")
    else:
        tips.append("Consider shortening your resume slightly.")

    # 5. Keywords: action verbs
    action_verbs = ['developed', 'created', 'managed', 'led', 'designed', 'implemented', 'improved']
    if any(verb in text for verb in action_verbs):
        score += 20
    else:
        tips.append("Use strong action verbs like 'developed', 'led', 'designed', etc.")

    return score, tips
