from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# MongoDB configuration
client = MongoClient("mongodb+srv://alasylkhh:123@cluster0.6fmla.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['users']
users = db['users']

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('home'))
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        # Check if user exists
        if users.find_one({'email': email}):
            flash('Email already registered!')
            return redirect(url_for('signup'))

        # Create new user
        user_data = {
            'email': email,
            'password': password,
            'name': name
        }
        users.insert_one(user_data)
        
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = users.find_one({'email': email, 'password': password})
        if user:
            session['user'] = {
                'email': user['email'],
                'name': user.get('name', '')
            }
            return redirect(url_for('home'))
        
        flash('Invalid email or password!')
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
