from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return f"hello, {name}!this was submitted by post"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
