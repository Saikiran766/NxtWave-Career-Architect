def get_local_roadmap(role):
    """
    Provides career guidance based on local logic.
    No external API calls are made, keeping user data 100% private.
    """
    # Local Knowledge Base
    database = {
        "Full Stack Developer": (
            "### 🚀 Full Stack Roadmap\n"
            "1. **Frontend**: Master HTML5, CSS3, and modern JavaScript (ES6+).\n"
            "2. **Frameworks**: Learn React.js and Tailwind CSS for styling.\n"
            "3. **Backend**: Build servers with Node.js and Express.\n"
            "4. **Database**: Learn PostgreSQL or MongoDB.\n"
            "5. **Capstone**: Build a full-stack E-commerce site."
        ),
        "Data Scientist": (
            "### 📊 Data Science Roadmap\n"
            "1. **Fundamentals**: Learn Python, NumPy, and Pandas.\n"
            "2. **Visualization**: Master Matplotlib and Seaborn.\n"
            "3. **Statistics**: Understand probability and hypothesis testing.\n"
            "4. **Machine Learning**: Learn Scikit-Learn for regression and classification.\n"
            "5. **Capstone**: Predict house prices using a real-world dataset."
        ),
        "AI/GenAI Engineer": (
            "### 🧠 AI Engineer Roadmap\n"
            "1. **Basics**: Python for AI and Deep Learning fundamentals.\n"
            "2. **NLP**: Master text processing and Transformers.\n"
            "3. **LLMs**: Learn Prompt Engineering and RAG (Retrieval-Augmented Generation).\n"
            "4. **Deployment**: Deploy models using Gradio and Hugging Face.\n"
            "5. **Capstone**: Build a custom PDF-chat assistant."
        )
    }

    return database.get(role, "Role not found. Start by mastering Python fundamentals!")
