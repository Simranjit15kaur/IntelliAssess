# 🧠 IntelliAssess – AI Assessment Intelligence Dashboard

**IntelliAssess** is an AI-powered assessment evaluation system designed to analyze **both objective and subjective exam responses**, along with **behavioral confidence indicators**, through a unified and explainable dashboard.

This project simulates how modern **ed-tech platforms and online interview systems** evaluate candidates beyond just right or wrong answers.

---

## 🚀 Why IntelliAssess?

Traditional online exams focus only on final scores.  
**IntelliAssess goes further** by answering critical evaluation questions such as:

- How confident was the candidate while answering?
- Was the performance consistent or stress-driven?
- How good is a subjective answer compared to an ideal response?
- Can AI provide explainable feedback instead of just marks?

---

## 🎯 Key Features

### ✅ Objective Performance Analysis
- Candidate-wise confidence classification  
- Speed profiling (Normal / Fast / Slow)  
- Stress-level inference  
- Explainable behavioral insights  

### ✍️ Subjective Answer Evaluation
- Semantic similarity between student and model answers  
- LLM-based examiner-style feedback  
- Final score combining semantic similarity and reasoning quality  
- Robust fallback logic for stable evaluation  

### 🔍 Explainable AI
- Human-readable explanations for AI decisions  
- Transparent scoring logic (no black-box grading)  

### 🖥 Interactive Dashboard
- Built using **Gradio**  
- Real-time evaluation  
- Clean, intuitive UI suitable for demos, reviews, and interviews  

---

## 🧠 How the System Works

### 1️⃣ Objective Evaluation Pipeline
- Precomputed behavioral metrics are analyzed  
- Confidence, stress, and speed profiles are inferred  
- Results are displayed with explainability  

### 2️⃣ Subjective Evaluation Pipeline
- Student answers are compared with model answers using sentence embeddings  
- Semantic similarity is computed  
- An LLM generates examiner-style feedback  
- A weighted final subjective score is produced  

**Design Choice:**  
The system performs **runtime evaluation**, making it adaptable to **live exams and interviews** without relying on large static datasets.

---

## 🛠 Tech Stack

- **Python**
- **Gradio** – Interactive dashboard
- **Transformers (Flan-T5)** – LLM-based feedback
- **Sentence Transformers** – Semantic similarity
- **Scikit-learn** – Similarity computation
- **Pandas** – Data handling

---

## ▶️ Running the Project Locally

```bash
pip install -r requirements.txt
python app.py
