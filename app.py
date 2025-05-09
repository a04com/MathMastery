from flask import Flask, render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# MongoDB connection
client = MongoClient("mongodb+srv://alasylkhh:admin@cluster0.6fmla.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['auth_db']
users = db['users']

questions = client['questions']
questions_algebra = questions['algebra']

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

@app.route('/algebra/<topic>')
def algebra_topic(topic):
    exercises = list(questions_algebra.find({'topic': topic}))
    return render_template('algebra_topic.html', topic=topic, exercises=exercises)

if __name__ == '__main__':
    app.run(debug=True)
