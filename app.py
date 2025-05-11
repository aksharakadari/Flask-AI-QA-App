from flask import Flask, render_template, request
import difflib  # Import for better matching

app = Flask(__name__)

# Predefined AI-related answers
AI_ANSWERS = {
    "what is artificial intelligence": "Artificial Intelligence (AI) is the simulation of human intelligence in machines that can perform tasks like learning, reasoning, and problem-solving.",
    "what is machine learning": "Machine Learning is a subset of AI that enables systems to learn patterns from data and improve performance over time.",
    "what is deep learning": "Deep Learning is a type of machine learning that uses neural networks to process large amounts of data and recognize complex patterns.",
    "who created AI": "AI research dates back to the 1950s, pioneered by scientists like Alan Turing, John McCarthy, and Marvin Minsky.",
    "how does ai impact creativity": "AI enhances creativity by providing tools for content creation, idea generation, and automation. However, some argue it limits human imagination by automating creative processes."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    user_question = request.form.get('question', '').strip().lower()

    # Find the closest matching question
    closest_match = difflib.get_close_matches(user_question, AI_ANSWERS.keys(), n=1, cutoff=0.6)

    # Get the corresponding answer or default response
    if closest_match:
        answer = AI_ANSWERS[closest_match[0]]
    else:
        answer = "I don't have a perfect answer for that, but AI is evolving every day! Try rephrasing your question."

    return render_template('answer.html', question=user_question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)