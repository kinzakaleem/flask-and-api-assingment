from flask import Flask
from student.routes import student_bp

app = Flask(__name__)
app.register_blueprint(student_bp, url_prefix='/student')

@app.route('/')
def home():
    return "<h1>Main App Home Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)