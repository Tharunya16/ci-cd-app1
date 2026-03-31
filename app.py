from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

# Dummy login
USERNAME = "admin"
PASSWORD = "1234"

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        return redirect('/dashboard')
    else:
        return "Invalid Credentials ❌"

@app.route('/dashboard')
def dashboard():
    status = random.choice(["Normal Traffic ✅", "Suspicious Activity ⚠️"])
    return render_template("dashboard.html", status=status)

if __name__ == '__main__':
    app.run(debug=True)