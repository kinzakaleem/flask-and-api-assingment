from flask import Flask, session, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = 'supersecretkey123'  # Required to use sessions

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username  # Store username in session
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile.html', username=session['username'])
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove session data
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)