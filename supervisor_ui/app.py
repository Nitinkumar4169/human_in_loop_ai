import sys, os
# 👇 Add parent folder to Python path so Flask can find the "db" module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, redirect, url_for, flash, send_from_directory
from db.firebase_config import db
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for flash messages

# --------------------------
# Dashboard route
# --------------------------
@app.route("/")
def dashboard():
    try:
        requests_ref = db.collection("requests").order_by("created_at").stream()
        requests = []
        for r in requests_ref:
            data = r.to_dict()
            data["id"] = r.id
            requests.append(data)
        return render_template("dashboard.html", requests=requests)
    except Exception as e:
        return f"<h3>🔥 Firebase error: {e}</h3>"

# --------------------------
# Resolve button route
# --------------------------
@app.route("/resolve/<id>")
def resolve(id):
    try:
        doc_ref = db.collection("requests").document(id)
        doc_ref.update({
            "status": "resolved",
            "resolved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        flash("✅ Request marked as resolved!", "success")
    except Exception as e:
        flash(f"⚠️ Error resolving request: {e}", "danger")
    return redirect(url_for("dashboard"))

# --------------------------
# Favicon route (to stop 404 warnings)
# --------------------------
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

# --------------------------
# Run the Flask App
# --------------------------
if __name__ == "__main__":
    print("✅ Firebase connection successful!")
    print("🚀 Flask Supervisor Dashboard running at http://127.0.0.1:5000")
    app.run(debug=True)
