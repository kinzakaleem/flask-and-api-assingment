from flask import Flask 
app = Flask(__name__)

@app.route('/')
def home():
    return "hello, welcome to flask"

if __name__ == '__main__':
    app.run(debug=True)
    