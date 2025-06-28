from flask import Flask
from app.routes import main

app = Flask(__name__)
app.secret_key = 'secret-key'  # required for session, flash etc.
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
