from flask import Blueprint, render_template

student_bp = Blueprint('student', __name__, template_folder='../templates')

@student_bp.route('/')
def student_home():
    return render_template('student_home.html')