import gradio as gr
from ai_engine import get_local_roadmap

def ui_handler(job_role):
    # This calls the logic from your ai_engine.py file
    return get_local_roadmap(job_role)

# Define the Interface
demo = gr.Interface(
    fn=ui_handler,
    inputs=gr.Dropdown(
        ["Full Stack Developer", "Data Scientist", "AI/GenAI Engineer"], 
        label="Select Your Target Career Role"
    ),
    outputs=gr.Markdown(label="Your Personalized Roadmap"),
    title="🚀 AI Career Architect",
    description="Select a role to generate a professional learning roadmap. Built for the NxtWave GenAI Workshop.",
    theme="soft"
)

if __name__ == "__main__":
    demo.launch()
