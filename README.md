# IntelliAssess – AI Assessment Intelligence Dashboard

IntelliAssess is an AI-powered system designed to evaluate online assessments by combining:

- Objective exam performance analysis
- Behavioral confidence and stress indicators
- Subjective answer evaluation using LLMs and semantic similarity

## Key Features
- Candidate confidence profiling
- Explainable AI-based feedback
- Subjective answer scoring with semantic similarity
- Interactive Gradio dashboard

## Tech Stack
- Python
- Gradio
- Transformers (Flan-T5)
- Sentence Transformers
- Scikit-learn

## How It Works
1. Objective metrics are analyzed to estimate confidence and stress.
2. Subjective answers are evaluated by combining:
   - Semantic similarity
   - LLM-based examiner feedback
3. Results are displayed through an interactive dashboard.

## Running Locally
```bash
pip install -r requirements.txt
python app.py
