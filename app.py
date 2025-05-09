from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
from groq import Groq

app = Flask(__name__)
app.secret_key = os.urandom(24)

# MongoDB connection
client = MongoClient("mongodb+srv://alasylkhh:admin@cluster0.6fmla.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['auth_db']
users = db['users']

questions = client['questions']
questions_algebra = questions['algebra']

groq_client = Groq(api_key='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')

def ask_groq_ai(exercise, user_message):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant for teaching math. When answering math questions, you will: 1. Write formulas using plain Markdown formatting (e.g., a^2 + b^2 = c^2) 2. Explain each step of the solution clearly and logically 3. Keep explanations concise but complete—neither too short nor too long 4. Give examples when useful, but stay focused on the main problem 5. Use simple, clear language appropriate for a student audience 6. Always explain why each step is taken, not just what to do 7. Be honest if you're unsure, and guide the user on how to find the answer."
        },
        {"role": "user", "content": f"Exercise: {exercise}\nUser question: {user_message}"}
    ]
    chat_completion = groq_client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=1000,
    )
    return chat_completion.choices[0].message.content

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('signin'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if user already exists
        if users.find_one({'username': username}):
            flash('Username already exists!')
            return redirect(url_for('signup'))
        
        # Create new user
        hashed_password = generate_password_hash(password)
        users.insert_one({
            'username': username,
            'password': hashed_password
        })
        
        flash('Account created successfully! Please sign in.')
        return redirect(url_for('signin'))
    
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = users.find_one({'username': username})
        
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!')
            return redirect(url_for('signin'))
    
    return render_template('signin.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('signin'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/signout')
def signout():
    session.pop('username', None)
    return redirect(url_for('signin'))

@app.route('/algebra/<topic>', methods=['GET', 'POST'])
def algebra_topic(topic):
    exercises = list(questions_algebra.find({'topic': topic}))
    feedback = {}
    if request.method == 'POST':
        for ex in exercises:
            user_answer_idx = request.form.get(f'answer_{ex["_id"]}')
            if user_answer_idx is not None:
                try:
                    user_answer_idx = int(user_answer_idx)
                    is_correct = ex['options'][user_answer_idx] == ex['answer']
                    feedback[str(ex['_id'])] = 'correct' if is_correct else 'incorrect'
                except Exception:
                    feedback[str(ex['_id'])] = 'incorrect'
            else:
                feedback[str(ex['_id'])] = 'unanswered'
    return render_template('algebra_topic.html', topic=topic, exercises=exercises, feedback=feedback)

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    data = request.get_json()
    exercise = data.get('exercise', '')
    user_message = data.get('message', '')
    try:
        ai_response = ask_groq_ai(exercise, user_message)
        return jsonify({'response': ai_response})
    except Exception as e:
        return jsonify({'response': 'Sorry, there was an error with the AI service.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
