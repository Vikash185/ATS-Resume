🛡️ ATS Resume Formatting & Score Engine

An intelligent web application that enforces strict layout, structural formatting, and section validation on uploaded resumes BEFORE analyzing their ATS (Applicant Tracking System) compatibility score. Built using pure JavaScript, Tailwind CSS, PDF.js, and html2pdf.

🌟 Key Features

🛡️ Strict Formatting Gatekeeper: Validates resume readability, layout structure, contact information (Email/Phone), and required standard sections before unlocking the ATS scoring phase.

📊 Automated ATS Scoring Engine: Calculates a weighted compatibility score (out of 100) based on structural health, keyword density, and quantifiable impact metrics (%, $, numbers).

🔍 Keyword & Skill Extraction: Automatically detects tech stack keywords and highlights critical missing skills for targeted job optimization.

💼 Direct Job Portal Integration: Generates single-click search links for LinkedIn, Google Jobs, Indeed, and Naukri.com matched to the candidate's detected role.

📄 Custom Resume Builder & PDF Generator: Allows candidates to create an ATS-compliant resume from scratch and export it instantly as a clean, parseable PDF.

🔬 How The Formatting Verification Works

The application operates on a Formatting-First Policy. When a candidate uploads a resume, the engine runs the following checks before evaluating the ATS score:

[ Upload PDF ] ──► [ Text Readability Check ] ──► [ Contact Info Validation ] ──► [ Section Headers Check ]
                                                                                         │
                                         ┌───────────────────────────────────────────────┴──────────────────────────────┐
                                         ▼                                                                              ▼
                              ❌ Formatting Failed                                                            ✅ Formatting Passed
                           (Halts & Shows Error)                                                      (Runs ATS Engine & Shows Score)


Text Readability Check: Rejects scanned/image-only PDFs with insufficient readable text (< 100 characters).

Contact Structure: Verifies if valid Email or Phone Number formatting exists.

Section Headers Check: Scans for standard structural sections:

💼 Work Experience / Employment

🎓 Education / Academic

🛠️ Skills / Technical Competencies

🚀 Projects / Key Deliverables

Metrics Density Check: Scans for quantifiable indicators (%, years, $, project metrics) to measure resume impact.

Note: If the uploaded document fails the gatekeeper check, execution halts immediately and displays an error message explaining why the format is invalid.

🚀 Getting Started

Follow these step-by-step terminal commands to run the project locally.

Prerequisites

You only need Git and a web browser. No NodeJS, npm packages, or build tools are required!

Step-by-Step Terminal Commands

Clone the Repository:

git clone https://github.com/your-username/ats-resume-checker.git


Navigate into the Project Directory:

cd ats-resume-checker


Run the Application:

Option A: Direct Open (Easiest)

# On Windows Command Prompt / PowerShell
start index.html

# On macOS
open index.html

# On Linux
xdg-open index.html


Option B: Run via Python Local Server (Recommended)

# For Python 3.x
python -m http.server 8000


Once started, open your browser and go to: http://localhost:8000

🛠️ Tech Stack & Dependencies

Frontend: HTML5, Modern JavaScript (ES6+)

Styling: Tailwind CSS (via CDN)

Icons: Lucide Icons

PDF Parsing Engine: PDF.js Library

PDF Export Engine: html2pdf.js

📂 Project Structure

ats-resume-checker/
│
├── index.html        # Complete Single-File Application (UI, Formatting Engine, ATS Scoring Logic)
├── README.md         # Full Project Documentation & Instructions
└── LICENSE           # Open-Source License


🤝 Contributing

Live Application Link

You can test and use the deployed live version of this project directly in your browser:

🌐 Live Demo: https://rococo-paletas-d51f53.netlify.app/

Open a Pull Request.

📜 License

This project is open-source and available under the MIT License.
