from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    user_name = "kinza"
    hobbies = ["coding", "reading", "playing with cat"]
    return render_template('welcome.html', name=user_name, hobbies=hobbies)

if __name__ == '__main__':
    app.run(debug=True)    