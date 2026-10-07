<div align="center">

# ATS Score Engine

ATS resume checker, job description matcher and resume builder that runs entirely in the browser.

You can test and use the deployed live version of this project directly in your browser:

🌐 Live Demo: https://rococo-paletas-d51f53.netlify.app/

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Open%20App-0e7490?style=for-the-badge)](https://rococo-paletas-d51f53.netlify.app/)
![No build](https://img.shields.io/badge/Build-None%20required-334155?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-15803d?style=for-the-badge)

</div>

---

ATS Score Engine first checks whether an applicant tracking system (ATS) can read your resume at all. If it can, you get a score out of 100, the reason behind every point, and a list of fixes. The built-in resume builder exports a PDF with real, selectable text, which an ATS can parse.

## Features

| Feature | What it does |
|---|---|
| Formatting gatekeeper | A 5-step check covers parsing, text readability, contact details and section structure. If a check fails, the app stops and explains how to fix it. |
| Score out of 100 | Six weighted factors, each shown separately so you can see where every point comes from. |
| Job description matching | Paste a job posting to see which of its keywords your resume contains and which are missing, as a percentage. |
| Skill detection | More than 100 skills in 11 categories, including aliases such as `k8s` for Kubernetes and `nodejs` for Node.js. Matching respects word boundaries, so "Java" does not match "JavaScript" and "Git" does not match "GitHub". |
| Role detection | Recognises 11 roles (Frontend, Backend, Full Stack, Data Analyst, Data Scientist, ML, DevOps, Mobile, UI/UX, QA, Product Manager) and lists the core skills each role usually expects. |
| Language analysis | Counts action verbs, flags weak phrases such as "responsible for" and "worked on", and suggests replacements. |
| 14-point checklist | Email, phone, LinkedIn, GitHub or portfolio, each standard section, date ranges, bullet points, icon-font glyphs and page count. |
| Prioritised fixes | Recommendations are sorted into high, medium and low priority. |
| Resume builder | Single column layout with a live preview. Drafts are saved in the browser. Exports a text-based PDF made with jsPDF. |
| Fix it in the builder | Loads an analysed resume into the builder, split into sections, so you can edit it and export a clean PDF. |
| Downloadable report | Saves the full analysis as a PDF. |
| Job search links | Opens searches for the detected role on LinkedIn, Naukri, Indeed, Glassdoor and Google Jobs. |
| Input formats | PDF, DOCX, TXT (up to 5 MB) or pasted text. |

## How it works

```
[ Parse ] --> [ Readability ] --> [ Contact ] --> [ Sections ] --> [ ATS score ]
                    |                 |               |
                    v                 v               v
              Stop and explain the fix (scanned PDF, no email or phone, no standard headings)
```

Gatekeeper rules

1. Readability: the resume must contain at least 100 characters of selectable text. Scanned or image-only PDFs fail.
2. Contact: it must contain a valid email address or a phone number with 10 to 13 digits. Year ranges such as `2019-2023` are not counted as phone numbers.
3. Structure: it must have at least 2 of Experience, Education, Skills and Projects. A section gets full credit when its heading is on its own line, and half credit when the word only appears in the text.

Score breakdown (100 points)

| Factor | Points | Measured by |
|---|---:|---|
| Section structure | 25 | Headings for Summary, Experience, Education, Skills and Projects |
| Keywords and skills, or JD match | 20 | Skills found and coverage of the role's core skills, or the share of job description keywords matched |
| Quantified impact | 15 | Lines with numbers such as %, ₹ or $, "2,000+ users", "10k requests", "3x" |
| Action-oriented language | 15 | Distinct action verbs, minus weak phrases and heavy use of "I", "me" and "my" |
| Length and readability | 15 | Word count (best between 250 and 950) and page count (2 or fewer) |
| Contact completeness | 10 | Email, phone, LinkedIn, GitHub or portfolio |

> The score is an estimate based on how ATS software commonly parses resumes. It is not produced by, or affiliated with, any ATS vendor.

## Run it locally

You do not need Node.js, npm or a build step. A browser is enough.

```bash
git clone https://github.com/Vikash185/ATS-Resume.git
cd ATS-Resume
```

Option A: Python local server (recommended)

```bash
python run_app.py          # opens http://localhost:8000, or the next free port
python run_app.py 9000     # use a specific port
```

Option B: open the file directly

```bash
start index.html      # Windows
open index.html       # macOS
xdg-open index.html   # Linux
```

## Deploy

The site is a single static file, `index.html`. Upload only that file, so that `README.md`, `run_app.py` and the `.git` folder are not published.

Netlify

1. Put `index.html` in a zip file, or in an empty folder.
2. In Netlify, open the site, go to Deploys, and drop the zip or folder onto the upload area.
3. Open the live URL and check that the new version loads.

It works the same way on any static host, such as Vercel or GitHub Pages.

## Tech stack

| Purpose | Library |
|---|---|
| UI | HTML5, JavaScript (ES2020+), Tailwind CSS (CDN) |
| Icons | Lucide (pinned to v0.460.0) |
| PDF reading | PDF.js 3.11, with line-aware text reconstruction |
| DOCX reading | Mammoth.js 1.6 |
| PDF creation | jsPDF 2.5, which writes real text |
| Local server | Python 3 standard library |

## Project structure

```
ATS-Resume/
├── index.html    # The whole app: UI, parsing, gatekeeper, scoring, builder, PDF export
├── run_app.py    # Local server that falls back to the next free port
├── README.md
└── LICENSE
```

## Privacy

Parsing, scoring and PDF creation all run on your device, and the resume you check is never uploaded. Builder drafts stay in your browser's `localStorage`. The page loads its libraries and fonts from public CDNs (cdn.tailwindcss.com, unpkg.com, cdnjs.cloudflare.com, Google Fonts), so those services see a normal page request. Your resume content is not sent to them.

## Contributing

1. Fork the repository and create a branch: `git checkout -b feature/my-idea`
2. Commit your changes: `git commit -m "Add my idea"`
3. Push the branch and open a pull request.

Good first contributions: add skills or roles to `SKILL_GROUPS` or `ROLES` in `index.html`, or add new checks to the checklist.

## License

Released under the [MIT License](LICENSE).
