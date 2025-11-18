HireAssistantAI

AI-powered recruitment automation — resume parsing, JD analysis, and personalized email generation.

<p align="left"> <img src="https://img.shields.io/badge/Python-3.10+-blue" /> <img src="https://img.shields.io/badge/LangGraph-Workflow-orange" /> <img src="https://img.shields.io/badge/LLM-Groq%20LLaMA%203.3%2070B-brightgreen" /> <img src="https://img.shields.io/badge/Status-Active-success" /> <img src="https://img.shields.io/badge/License-MIT-blue" /> <img src="https://img.shields.io/badge/PRs-Welcome-purple" /> </p> <p align="left"> <img src="https://img.shields.io/github/stars/prateekroyy/HireAssistantAI?style=social&v=1" /> <img src="https://img.shields.io/github/forks/prateekroyy/HireAssistantAI?style=social&v=1" /> </p>

HireAssistantAI is a modular, LangGraph-driven workflow system that extracts structured information from resumes and job descriptions and automatically generates professional interview invitation emails using Groq LLaMA 3.3 70B.

🌟 Features
🔍 1. Resume Parsing (PDF → JSON)

Extracts:

Candidate Name

Current Company

Current Role

Total Years of Experience

Email Address

📄 2. Job Description Parsing

Extracts:

Job Title

Company

Experience Required

Skills Required

Education

Location

Salary Range

Employment Type

✉️ 3. Email Generation

Produces a polished, personalized interview invitation email using the parsed resume and job attributes.

🧹 4. Clean Output (JSON)
{
  "recipient": "candidate@example.com",
  "subject": "Interview Invitation – Software Engineer",
  "body": "..."
}

🧠 Architecture
                   ┌────────────────────┐
Resume PDF ───────► Resume Parser Node ─┐
                                        │
                                        ├──► Email Writer ─► Formatter ─► Final JSON
                                        │
Job Description PDF ─► JD Parser Node ──┘


Modular, composable workflow powered by LangGraph.

📁 Project Structure
HIREASSISTANTAI/
│
├── models/
│   ├── structures.py          # Pydantic schemas
│   ├── flowstate.py           # Workflow state definitions
│   └── nodes/
│       ├── resumeparser.py
│       ├── jdparser.py
│       ├── email_writer.py
│       └── format_output.py
│
├── workflows/
│   ├── resume_workflow.py
│   ├── jd_workflow.py
│
├── data/
│   ├── sample_resume.pdf
│   └── sample_jd.pdf
│
├── main.py                     # End-to-end execution
├── requirements.txt
├── .env
├── LICENSE                     # License file
└── README.md                   # Project documentation (this file)

🔧 Installation
1️⃣ Clone the Repository
git clone https://github.com/prateekroyy/HireAssistantAI.git
cd HireAssistantAI

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add Your API Key

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here

▶️ Usage
Step 1: Add Your PDFs

Place them in data/:

data/
├── my_resume.pdf
└── job_description.pdf

Step 2: Update Paths in main.py
initial_state = {
    "pdf_resume": "data/my_resume.pdf",
    "pdf_jd": "data/job_description.pdf"
}

Step 3: Run
python main.py

Step 4: Output

The structured JSON email prints in your terminal.

🛠 Tech Stack

Python 3.10+

LangGraph

LangChain

Groq API (LLaMA 3.3 70B)

Pydantic

PyPDFLoader

dotenv

🚀 Roadmap

🔹 AI candidate ranking

🔹 Screening question generator

🔹 Follow-up / rejection email templates

🔹 Streamlit dashboard

🔹 FastAPI backend

🔹 Bulk résumé/JD processing

🔹 Export to ATS formats (CSV, JSONL, PDF)

🤝 Contributing

PRs are welcome!
Open an issue for major changes.

📄 License

This project is licensed under the MIT License.
