from flask import Flask

app = Flask(__name__)

from app.routes import main  # assuming you're using Blueprint
app.register_blueprint(main)
