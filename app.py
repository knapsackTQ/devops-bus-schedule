from flask import Flask, jsonify

app = Flask(__name__)

def get_html(page_title, body_content):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{page_title}</title>
        <style>
            body {{ font-family: 'Segoe UI', system-ui, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
            .card {{ background-color: #1e293b; padding: 40px; border-radius: 16px; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5); border: 1px solid #334155; max-width: 600px; width: 90%; text-align: center; }}
            h1 {{ color: #38bdf8; font-size: 26px; margin-top: 0; }}
            .status-badge {{ display: inline-block; background: #064e3b; color: #34d399; padding: 6px 12px; border-radius: 9999px; font-size: 14px; font-weight: bold; margin-bottom: 20px; border: 1px solid #059669; }}
            .route-box {{ background: #0f172a; border-left: 4px solid #38bdf8; padding: 16px; margin: 15px 0; border-radius: 6px; text-align: left; font-size: 16px; }}
            .route-box strong {{ color: #7dd3fc; display: block; margin-bottom: 4px; }}
            .btn {{ display: inline-block; background-color: #0284c7; color: white; padding: 12px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; margin-top: 20px; transition: 0.2s; border: none; cursor: pointer; }}
            .btn:hover {{ background-color: #0369a1; transform: translateY(-2px); }}
            .footer {{ margin-top: 30px; font-size: 13px; color: #64748b; border-top: 1px solid #334155; padding-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="card">
            {body_content}
            <div class="footer">Developed by Tanishq Dinesh Jadhav</div>
        </div>
    </body>
    </html>
    """

@app.route("/")
def home():
    content = """
        <div class="status-badge">🟢 Live System Active</div>
        <h1>Welcome to the Saraswati College Transit Portal</h1>
        <p style="color: #94a3b8; line-height: 1.6; margin-bottom: 30px;">
            Real-time automated routing system. The next scheduled departure is arriving in exactly 10 minutes.
        </p>
        <a href="/routes" class="btn">View Bus Routes</a>
    """
    return get_html("Transit Home", content)

@app.route("/routes")
def routes():
    content = """
        <h1>Active Bus Routes</h1>
        <div class="route-box">
            <strong>Route A: Morning Express</strong>
            Kharghar Station to Saraswati Campus (8:00 AM)
        </div>
        <div class="route-box">
            <strong>Route B: Evening Return</strong>
            Saraswati Campus to Thane East (5:00 PM)
        </div>
        <a href="/" class="btn" style="background-color: #475569;">Return Home</a>
    """
    return get_html("Live Routes", content)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)