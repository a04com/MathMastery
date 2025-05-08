from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient
import random
from bson import json_util
import json
from groq import Groq

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session management

# MongoDB connection
client = MongoClient("mongodb+srv://alasylkhh:123@cluster0.6fmla.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['questions']
questions_collection = db['algebra']

# Groq AI setup
GROQ_API_KEY = "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"
groq_client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """You are a helpful AI assistant for teaching math.
When answering math questions, you will:
1. Write formulas using plain Markdown formatting (e.g., a^2 + b^2 = c^2)
2. Explain each step of the solution clearly and logically
3. Keep explanations concise but complete—neither too short nor too long
4. Give examples when useful, but stay focused on the main problem
5. Use simple, clear language appropriate for a student audience
6. Always explain why each step is taken, not just what to do
7. Be honest if you're unsure, and guide the user on how to find the answer
"""

def ask_ai(user_question, exercise_context=None):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    if exercise_context:
        messages.append({"role": "user", "content": f"Exercise context: {exercise_context}"})
    messages.append({"role": "user", "content": user_question})

    chat_completion = groq_client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=1000,
    )
    return chat_completion.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_test')
def start_test():
    # Get 5 random questions from the database
    questions = list(questions_collection.aggregate([{'$sample': {'size': 5}}]))
    
    # Convert MongoDB documents to JSON-serializable format
    serialized_questions = json.loads(json_util.dumps(questions))
    
    session['questions'] = serialized_questions
    session['current_question'] = 0
    session['score'] = 0
    return redirect(url_for('question'))

@app.route('/question', methods=['GET', 'POST'])
def question():
    if 'questions' not in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Check the answer
        user_answer = request.form.get('answer')
        current_question = session['questions'][session['current_question']]
        
        if user_answer == current_question['answer']:
            session['score'] += 1
        
        session['current_question'] += 1
        
        if session['current_question'] >= len(session['questions']):
            return redirect(url_for('result'))
        
        return redirect(url_for('question'))
    
    current_question = session['questions'][session['current_question']]
    return render_template('question.html', 
                         question=current_question,
                         question_number=session['current_question'] + 1,
                         total_questions=len(session['questions']))

@app.route('/ask_ai', methods=['POST'])
def handle_ai_question():
    data = request.get_json()
    user_question = data.get('question')
    current_question = session['questions'][session['current_question']]
    
    # Create context from current question
    context = f"Current question: {current_question['question']}"
    
    # Get AI response
    response = ask_ai(user_question, context)
    return jsonify({'response': response})

@app.route('/result')
def result():
    if 'score' not in session:
        return redirect(url_for('index'))
    
    score = session['score']
    total = len(session['questions'])
    percentage = (score / total) * 100
    
    # Clear session data
    session.clear()
    
    return render_template('result.html', 
                         score=score,
                         total=total,
                         percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)
