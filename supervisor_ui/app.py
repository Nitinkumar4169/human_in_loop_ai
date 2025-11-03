import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, redirect, url_for, flash, request
from db.firebase_config import db
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def home():
    requests_ref = db.collection("requests").get()
    requests = []
    for r in requests_ref:
        req = r.to_dict()
        req["id"] = r.id
        requests.append(req)
    requests.sort(key=lambda x: x["created_at"], reverse=True)
    return render_template("dashboard.html", requests=requests)

@app.route("/resolve/<id>", methods=["GET", "POST"])
def resolve(id):
    doc_ref = db.collection("requests").document(id)
    if request.method == "POST":
        answer = request.form.get("answer", "").strip()
        doc_ref.update({
            "status": "resolved",
            "answer": answer,
            "resolved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        flash("✅ Query resolved and answer saved successfully!", "success")
        return redirect(url_for("home"))
    doc = doc_ref.get()
    if doc.exists:
        data = doc.to_dict()
        data["id"] = id
        return render_template("resolve.html", request_data=data)
    else:
        flash("⚠️ Request not found.", "danger")
        return redirect(url_for("home"))

if __name__ == "__main__":
    print("✅ Firebase connection successful!")
    print("🚀 Flask Supervisor Dashboard running at http://127.0.0.1:5000")
    app.run(debug=True)
