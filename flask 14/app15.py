from flask import Flask
from home import home_bp

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(home_bp)

if __name__ == '__main__':
    app.run(debug=True)