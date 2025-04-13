from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = 'secret123'  # Required for using sessions

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return f"<h1>Welcome, {session['username']}!</h1>"
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)