# 🧠 Smart AI Resume Analyzer & AI Mock Interview Platform

## 🎓 Final Year Project 

An AI-powered web application built using Streamlit that helps users:

- Analyze resumes with ATS scoring
- Identify keyword gaps and skill gaps
- Build professional resumes
- Practice AI-generated mock interviews
- Receive automated evaluation & feedback

---

# 🚀 Project Overview

This system consists of two main modules:

---

## 1️⃣ AI Resume Analyzer

The Resume Analyzer evaluates uploaded resumes and provides:

- 📊 ATS Compatibility Score  
- 🔍 Keyword Gap Analysis  
- 🧠 Skills Gap Identification  
- 🎯 Role-Based Recommendations  
- 📈 Resume Performance Metrics  

Users can upload a PDF resume and receive structured AI-driven insights.

---

## 2️⃣ AI Mock Interview Platform

The AI Mock Interview platform allows users to:

- 📄 Upload Resume  
- 🤖 Automatically Generate Interview Questions (based on resume content)  
- 🎙 Record Answers directly in browser  
- 📝 Get Automatic Speech-to-Text Transcription  
- 📊 Receive AI Evaluation & Scoring  

### Evaluation Includes:

- Technical Score  
- Communication Score  
- Confidence Score  
- Detailed Feedback Per Question  

This module simulates a real interview experience.

---

# 🛠 Tech Stack

## Frontend
- Streamlit
- HTML
- CSS

## Backend
- Python

## AI & NLP
- Ollama (Mistral / Llama Models)
- Whisper (Speech-to-Text)
- spaCy
- NLTK

## Database
- SQLite3

---

# ⚙️ How It Works

### Resume Analyzer Flow

1. Upload Resume (PDF)
2. Extract text
3. Perform NLP analysis
4. Generate ATS & skill scores
5. Display insights

---

### AI Mock Interview Flow

1. Upload Resume
2. Select number of questions (1 / 2 / 5)
3. Generate AI-based interview questions
4. Record answer in browser
5. Transcribe using Whisper
6. Evaluate using LLM
7. Show final performance report

---

# 🗄 Database

The system stores:

- Interview scores
- Evaluation results
- Resume analysis data

Database used: `SQLite (resume_analysis.db)`

---

# 💻 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone <your-repository-link>
cd Smart-AI-Resume-Analyzer
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## 5️⃣ Install & Run Ollama

Download Ollama and run:

```bash
ollama pull mistral
```

Then warm the model:

```bash
ollama run mistral
```

Exit after loading.

---

## 6️⃣ Run Application

```bash
 python -m streamlit run app.py
```

---

# 📁 Project Structure

```
Smart-AI-Resume-Analyzer/
│
├── app.py
├── resume_analysis.db
├── voice_interview/
│   ├── question_generator.py
│   ├── evaluator.py
│   ├── voice_engine.py
│
├── utils/
├── dashboard/
├── jobs/
├── style/
└── requirements.txt
```

---

# 🎯 Objective of the Project

To create an intelligent career preparation platform that:

- Improves resume quality
- Simulates real interview scenarios
- Provides AI-driven feedback
- Enhances job readiness

---
