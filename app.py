from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Jay's Cloud App is Live</h1>
    <p>This is my first cloud deployed app.</p>
    """