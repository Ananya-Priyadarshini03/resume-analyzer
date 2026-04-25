from flask import Flask, render_template, request, jsonify
import PyPDF2
from docx import Document
import io, os
import spacy
from dotenv import load_dotenv
from openai import OpenAI

# 🔥 Load .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load NLP
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

class ResumeAnalyzer:

    def extract_text(self, content, filename):
        try:
            if filename.endswith(".pdf"):
                pdf = PyPDF2.PdfReader(io.BytesIO(content))
                return " ".join([p.extract_text() or "" for p in pdf.pages])

            elif filename.endswith(".docx"):
                doc = Document(io.BytesIO(content))
                return " ".join([p.text for p in doc.paragraphs])
        except:
            return ""
        return ""

    def calculate_score(self, text):
        keywords = ["python","sql","react","aws","java","html","css"]
        score = sum(12 for k in keywords if k in text.lower())
        return min(score + (20 if len(text.split()) > 300 else 0), 100)

    def detect_skills(self, text):
        skill_map = {
            "Python":["python"],
            "SQL":["sql"],
            "React":["react"],
            "AWS":["aws"],
            "Java":["java"],
            "HTML":["html"],
            "CSS":["css"]
        }

        results=[]
        t=text.lower()

        for skill,keys in skill_map.items():
            for k in keys:
                if k in t:
                    count=t.count(k)

                    if count>3:
                        level="Advanced"; percent=90
                    elif count>1:
                        level="Intermediate"; percent=70
                    else:
                        level="Beginner"; percent=40

                    results.append({
                        "name":skill,
                        "level":level,
                        "percent":percent
                    })
                    break
        return results

    def get_roles(self,text):
        text=text.lower()
        roles=[]

        if "python" in text: roles.append("Python Developer")
        if "react" in text or "html" in text: roles.append("Frontend Developer")
        if "aws" in text: roles.append("Cloud Engineer")
        if "sql" in text: roles.append("Data Analyst")

        return roles or ["Software Developer"]

    def ai_feedback(self,text):
        if not os.getenv("OPENAI_API_KEY"):
            return "⚠️ API key missing"

        prompt=f"""
You are an ATS system.

Give:
1. Strengths
2. Weaknesses
3. Improvements

Resume:
{text[:2000]}
"""

        try:
            res=client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role":"user","content":prompt}]
            )
            return res.choices[0].message.content
        except Exception as e:
            print("AI Error:", e)
            return "⚠️ AI not available"

    def analyze(self,content,filename):
        text=self.extract_text(content,filename)

        if not text.strip():
            return {"success":False,"error":"Cannot read file"}

        return {
            "success":True,
            "score":self.calculate_score(text),
            "skills":self.detect_skills(text),
            "roles":self.get_roles(text),
            "ai_feedback":self.ai_feedback(text)
        }

analyzer=ResumeAnalyzer()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze",methods=["POST"])
def analyze():
    file=request.files.get("resume")
    if not file:
        return jsonify({"success":False,"error":"No file uploaded"})

    result=analyzer.analyze(file.read(),file.filename)
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)