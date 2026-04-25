# 🚀 AI Resume Analyzer

An intelligent web application that analyzes resumes using NLP and AI to provide ATS score, skill insights, job role suggestions, and improvement recommendations.

---

## 🌐 Live Demo

👉[ https://resume-analyzer-3-r9jr.onrender.com](https://resume-analyzer-3-r9jr.onrender.com)

---

## 📌 Features

* 📄 Upload Resume (PDF/DOCX)
* 🧠 AI-based Resume Analysis
* 📊 ATS Score Calculation
* 🛠️ Skills Detection with Levels
* 📈 Skill Visualization (Pie Chart)
* 💼 Suggested Job Roles
* 🤖 AI Feedback (Strengths, Weaknesses, Improvements)
* 📂 Drag & Drop Upload Support

---

## 🖥️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask (Python)
* **NLP:** spaCy
* **AI:** OpenAI API
* **Visualization:** Chart.js
* **Deployment:** Render

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Ananya-Priyadarshini03/resume-analyzer.git
cd resume-analyzer
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Download spaCy model

```bash
python -m spacy download en_core_web_sm
```

---

### 4️⃣ Add Environment Variable

Create `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## ☁️ Deployment (Render)

1. Push code to GitHub
2. Create Web Service in Render
3. Set Build Command:

```bash
pip install -r requirements.txt && python -m spacy download en_core_web_sm
```

4. Set Start Command:

```bash
gunicorn app:app
```

5. Add Environment Variable:

```
OPENAI_API_KEY=your_api_key
```

---

## 📊 How It Works

1. User uploads resume
2. Backend extracts text from PDF/DOCX
3. NLP processes skills and keywords
4. ATS score is calculated
5. AI generates feedback and suggestions
6. Results displayed with charts and insights

---

## 🎯 Output Example

* ✅ ATS Score
* ✅ Skills with Levels
* ✅ Suggested Roles
* ✅ Pie Chart Visualization
* ✅ AI Feedback

---

## 🚀 Future Enhancements

* 📄 Resume Improvement Download
* 🎯 Job Description Matching
* 📊 Advanced Analytics Dashboard
* 🎨 Modern UI/UX Enhancements

---

## 👩‍💻 Author

**Ananya Priyadarshini**
GitHub: https://github.com/Ananya-Priyadarshini03

---


If you like this project, give it a ⭐ on GitHub!
