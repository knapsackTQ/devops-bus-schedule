from flask import Flask, jsonify

app = Flask(__name__)

# Modern CSS styling
CSS = """
<style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f4f8; color: #333; text-align: center; padding: 50px; }
    h1 { color: #2c3e50; font-size: 2.5em; margin-bottom: 10px; }
    h2 { color: #34495e; }
    .container { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.1); max-width: 650px; margin: auto; }
    ul { list-style-type: none; padding: 0; }
    li { background: #e1e8ed; margin: 12px 0; padding: 15px; border-radius: 8px; font-weight: bold; font-size: 1.1em; color: #2c3e50; }
    a { text-decoration: none; color: #fff; background-color: #3498db; padding: 10px 20px; border-radius: 6px; font-weight: bold; margin-top: 20px; display: inline-block; transition: 0.3s; }
    a:hover { background-color: #2980b9; }
    .subtitle { color: #7f8c8d; font-size: 1.2em; margin-bottom: 30px; }
</style>
"""

@app.route("/")
def home():
    return f"{CSS}<div class='container'><h1>Welcome to the College Bus Schedule Viewer!</h1><p class='subtitle'>Your smart transit companion. Next bus arrives in 10 minutes.</p><a href='/routes'>View Bus Routes</a></div>"

@app.route("/routes")
def routes():
    return f"{CSS}<div class='container'><h2>Bus Routes</h2><ul><li>🚍 Route A: Main Gate to Hostel (8:00 AM)</li><li>🚍 Route B: Library to Station (5:00 PM)</li></ul><a href='/'>Back to Home</a></div>"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)