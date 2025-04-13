from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Practical 8</h1>"

@app.route('/about')
def about():
    return "<h2>This is the About Page</h2>"

# Error Handler for 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)