import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'secret-key-for-flash'

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'txt', 'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            flash('No file part in the request')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also submits an empty part
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            return f"File successfully uploaded: {filename}"
        else:
            flash('File type not allowed')
            return redirect(request.url)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)