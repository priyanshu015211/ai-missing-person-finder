# ai-missing-person-finder# 🌍 AI-Powered Missing Person Finder for Disaster Relief

> Reuniting families faster during floods, earthquakes, and large-scale evacuations — using AI-powered face matching instead of paper lists and word-of-mouth.

[![Status](https://img.shields.io/badge/status-early--stage-yellow)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)]()

---

## 🧭 Overview

During disasters, families often get separated in the chaos. Traditional search methods — paper lists, word-of-mouth, physically visiting relief camps — don't scale to the size of a large-scale crisis.

**AI-Powered Missing Person Finder** aims to close that gap:

1. 📸 A family member uploads a photo of a missing loved one.
2. 🏕️ Relief camps and shelters log photos of the people they register (with consent).
3. 🤖 The system cross-matches the missing-person photo against the camp/shelter database.
4. ✅ Matches are surfaced to relief coordinators (and, where appropriate, the family) — cutting search time from days to minutes.

This project started as part of an **AI for Social Impact challenge**, exploring how AI can be a force for humanity, not just business efficiency.

---

## ⚠️ Project Status

This is an **early-stage / concept project**. Nothing here is production-ready or currently deployed in a real disaster-response setting. Treat this repo as a starting point for prototyping, not a live tool. See [Ethical & Safety Considerations](#-ethical--safety-considerations) before doing anything with real people's data.

---

## ✨ Core Features (Planned)

- [ ] **Photo upload portal** for families searching for a missing person
- [ ] **Camp/shelter intake tool** for relief workers to log photos of registered individuals
- [ ] **Face-matching engine** to compare uploaded photos against the shelter database
- [ ] **Match review dashboard** for relief coordinators to confirm/reject candidate matches
- [ ] **Notification system** to alert families when a likely match is found
- [ ] **Multi-camp / multi-region support** so searches aren't limited to a single shelter
- [ ] **Offline-first / low-bandwidth mode** for use in areas with limited connectivity
- [ ] **Audit logging** for every match action, for accountability and consent tracking

---

## 🏗️ Proposed Architecture

```
┌─────────────────┐        ┌──────────────────┐        ┌────────────────────┐
│  Family Upload    │        │   Camp Intake     │        │  Coordinator        │
│  Web / Mobile App │  --->  │   Web / Mobile App│  --->  │  Review Dashboard   │
└─────────────────┘        └──────────────────┘        └────────────────────┘
          \                          /
           \                        /
            v                      v
        ┌───────────────────────────────┐
        │        Backend API             │
        │  (auth, storage, orchestration)│
        └───────────────────────────────┘
                        │
                        v
        ┌───────────────────────────────┐
        │   Face Matching / ML Service   │
        │ (embedding + similarity search)│
        └───────────────────────────────┘
                        │
                        v
        ┌───────────────────────────────┐
        │   Encrypted Photo/Data Store   │
        └───────────────────────────────┘
```

This is a starting sketch, not a locked-in design — refine it as the project develops.

---

## 🛠️ Suggested Tech Stack

| Layer | Options to Consider |
|---|---|
| Frontend (family + camp apps) | React / React Native, Flutter |
| Backend API | Node.js (Express/NestJS) or Python (FastAPI) |
| Face matching | Open-source models (e.g. FaceNet, ArcFace, InsightFace) via a Python ML service |
| Vector similarity search | FAISS, Milvus, or pgvector |
| Database | PostgreSQL for structured data |
| Photo storage | Encrypted object storage (e.g. S3-compatible) with strict access controls |
| Deployment | Docker + a cloud provider or NGO-hosted infrastructure |
| Offline sync | PouchDB/CouchDB or similar for low-connectivity camps |

Pick what fits your skills and what relief organizations you partner with can realistically host and maintain.

---

## 🚀 Getting Started

> These are placeholder instructions — update them once the actual codebase exists.

```bash
# Clone the repository
git clone https://github.com/priyanshu015211/ai-missing-person-finder.git
cd ai-missing-person-finder

# Install dependencies (example for a Node/Python split repo)
cd backend && npm install
cd ../ml-service && pip install -r requirements.txt

# Set up environment variables
cp .env.example .env

# Run locally
docker-compose up
```

---

## 🗺️ Roadmap

- **Phase 1 — Prototype**
  - Build a basic upload + match demo using a public face-matching library
  - Validate matching accuracy on a small, consented test dataset
- **Phase 2 — Pilot design**
  - Partner with an NGO or relief organization (e.g. InAmigos Foundation) to co-design real workflows
  - Define consent, data retention, and takedown processes with them
- **Phase 3 — Field pilot**
  - Small-scale pilot at a single shelter/camp with strict oversight
  - Human-in-the-loop review for every match before it's shared with a family
- **Phase 4 — Scale**
  - Multi-camp support, offline mode, notification system

---

## 🔐 Ethical & Safety Considerations

Face recognition of vulnerable people in a crisis is high-stakes. Before building further, plan explicitly for:

- **Informed consent** — people at shelters must clearly understand their photo may be used for matching, and be able to opt out.
- **Data minimization & retention** — store only what's needed, for as short a time as possible, and define deletion policies.
- **Human-in-the-loop matching** — never auto-reunite based on an AI match alone; a human should always confirm before any action is taken (especially around children).
- **Bias & accuracy** — face-matching models can perform unevenly across skin tones, ages, and image quality; test rigorously and disclose limitations.
- **Security** — photos and match data are sensitive; use encryption at rest and in transit, and strict access controls.
- **Vulnerable populations** — add extra safeguards for unaccompanied minors, and coordinate with child-protection protocols (e.g. those used by the Red Cross, UNHCR, or local authorities).
- **Legal compliance** — biometric data laws vary by country/state (e.g. GDPR, BIPA); consult local regulations before any real-world use.
- **Partner with relief experts** — organizations like the Red Cross, UNHCR, or local NGOs already have reunification protocols; this tool should support, not replace, their expertise.

---

## 🤝 Contributing

Contributions, ideas, and critiques are welcome — especially from people with disaster-relief, ML fairness, or humanitarian-data experience.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-idea`)
3. Commit your changes
4. Open a pull request describing the change and why it helps

If you're from a relief organization and want to advise on real-world workflows, please open an issue — that kind of input is more valuable than code right now.

---

## 📄 License

This project is intended to be released under the [MIT License](LICENSE) — add a `LICENSE` file to formalize it.

---

## 🙏 Acknowledgments

- Built out of an **AI for Social Impact challenge**
- Inspired by the real, ongoing work of disaster-relief organizations reuniting families in crisis

---

## 📬 Contact

Add your preferred contact method here (email, LinkedIn, X/Twitter) so collaborators and potential NGO partners can reach you.
