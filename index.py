import os
from flask import Flask
from connect import connect

app = Flask(__name__)


connect();

@app.route("/")
def index():
    return "<h1>Hello World</hi>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

