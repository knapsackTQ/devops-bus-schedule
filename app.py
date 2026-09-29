from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the College Bus Schedule Viewer!</h1><p>Next bus arrives in 10 minutes.</p>"

@app.route("/routes")
def routes():
    return "<h2>Bus Routes</h2><ul><li>Route A: Main Gate to Hostel (8:00 AM)</li><li>Route B: Library to Station (5:00 PM)</li></ul>"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)