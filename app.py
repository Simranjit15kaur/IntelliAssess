with gr.Blocks() as demo:

    gr.Markdown("""
    # 🧠 IntelliAssess – AI Assessment Intelligence Dashboard
    ### Behavioral Confidence Analysis for Online Exams
    """)

    # ================= OBJECTIVE DASHBOARD =================
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## 🎯 Candidate Selection")
            candidate_id = gr.Dropdown(
                choices=df["candidate_id"].tolist(),
                label="Select Candidate ID"
            )

        with gr.Column(scale=2):
            gr.Markdown("## 📊 Candidate Snapshot")
            confidence = gr.Textbox(label="Final Confidence")
            speed = gr.Textbox(label="Speed Profile")
            stress = gr.Textbox(label="Stress Level")

    gr.Markdown("## 🔍 Explainability")
    explanation = gr.Textbox(lines=4)

    gr.Markdown("## 🧪 AI Signals")
    with gr.Row():
        refined = gr.Textbox(label="Refined Certainty")
        skill = gr.Textbox(label="Skill Score")
        expert_speed = gr.Textbox(label="Expert Speed Score")

    candidate_id.change(
        fn=get_candidate_view,
        inputs=candidate_id,
        outputs=[
            confidence,
            speed,
            stress,
            explanation,
            refined,
            skill,
            expert_speed
        ]
    )

    # ================= SUBJECTIVE DASHBOARD =================
    with gr.Accordion("📝 Subjective Answer Evaluation", open=False):

        gr.Markdown(
            "AI-based evaluation of descriptive answers using "
            "rubric-style scoring and semantic similarity."
        )

        subj_question = gr.Textbox(
            label="Question",
            placeholder="Enter subjective question"
        )

        subj_student_answer = gr.Textbox(
            label="Student Answer",
            lines=5
        )

        subj_model_answer = gr.Textbox(
            label="Model Answer",
            lines=5
        )

        evaluate_btn = gr.Button("Evaluate Subjective Answer")

        with gr.Row():
            subj_score = gr.Number(label="Final Subjective Score")
            subj_similarity = gr.Number(label="Semantic Similarity")

        subj_feedback = gr.Textbox(
            label="AI Feedback",
            lines=3
        )

        evaluate_btn.click(
            fn=final_subjective_evaluation,
            inputs=[
                subj_question,
                subj_student_answer,
                subj_model_answer
            ],
            outputs=[
                subj_score,
                subj_similarity,
                subj_feedback
            ]
        )

# ================= LAUNCH =================
demo.launch(share=True)
