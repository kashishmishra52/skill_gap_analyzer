# Skill Gap Analyzer

## Overview

**Skill Gap Analyzer** is a web application designed to help job applicants evaluate their resumes against desired job roles by identifying matched and missing skills. It provides a comprehensive skill gap analysis, a Total Applicant Score (TAS), visual skill gap graphs, and personalized course recommendations to improve the missing skills. Additionally, the app offers resume quality scoring with tailored suggestions for enhancing the resume.

This tool is aimed at freshers and professionals across multiple industries and job roles, empowering users to better tailor their resumes and skillsets to job requirements and improve their chances of landing the desired position.

---

## Features

- **Multi-Role Analysis:** Evaluate your resume against multiple job roles simultaneously.
- **Skill Matching:** Detect matched and missing skills by comparing resume content with predefined skill requirements.
- **Total Applicant Score (TAS):** Quantitative score representing how well your skills align with the job roles.
- **Skill Gap Visualization:** Pie chart visualization showing matched vs missing skills.
- **Course Recommendations:** Personalized learning resources for missing skills with direct links.
- **Resume Quality Scoring:** Scores your resume based on content structure and suggests improvements.
- **Support for Various Job Roles:** Includes technical, managerial, and other professional roles like Data Scientist, Web Developer, DevOps Engineer, Product Manager, and more.

---

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Jinja2 Templates
- **PDF Parsing:** `pdfminer` or `PyPDF2` (used in `resume_parser.py`)
- **Data Visualization:** Matplotlib for skill gap pie charts
- **Version Control:** Git, GitHub

---

## Installation

### Prerequisites

- Python 3.7 or higher
- Git
- Virtual Environment (recommended)

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/kashishmishra52/skill_gap_analyzer.git
   cd skill_gap_analyzer
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask application:

bash
Copy code
flask run
Open your browser and go to http://127.0.0.1:5000 to access the app.

Usage
Upload your resume in PDF format.

Enter one or more job roles separated by commas (e.g., data scientist, web developer).

Submit the form to receive:

Matched and missing skills.

Total Applicant Score.

Skill gap pie chart.

Course recommendations for missing skills.

Resume quality score with improvement suggestions.

Project Structure
graphql
Copy code
skill_gap_analyzer/
├── app/
│   ├── templates/           # HTML templates (index.html, result.html, error.html)
│   ├── static/              # CSS, JS, images, skill gap chart images
│   ├── analyzer.py          # Core skill analysis and recommendations
│   ├── resume_parser.py     # Resume PDF text extraction
│   ├── visualizer.py        # Matplotlib skill graph generation
│   ├── routes.py            # Flask route definitions
│   └── __init__.py          # Flask app initialization
├── data/                    # Uploaded resumes stored temporarily
├── requirements.txt         # Python dependencies
├── README.md                # This documentation file
└── .gitignore
Adding More Job Roles & Skills
The job roles and corresponding required skills are defined in analyzer.py.

Add new roles or update existing skill weights to customize for different industries and positions.

Future Enhancements
Support for more resume formats (Word, TXT).

Integration with NLP models for better skill extraction.

User authentication and resume history.

Interactive dashboard for visualizing progress over time.

Support for different languages.

Contributing
Contributions are welcome! Please open an issue or submit a pull request.



Contact
Kashish Mishra
GitHub: https://github.com/kashishmishra52
Email: kashish.official52@gmail.com

Acknowledgements
Flask framework

Matplotlib for visualization

Open source resume parsing and NLP libraries
