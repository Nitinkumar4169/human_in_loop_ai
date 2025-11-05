import sys, os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, request
from firebase_admin import firestore

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import Firestore client from your Firebase config
from db.firebase_config import db

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"

# ==========================
# ROUTE: Dashboard (Home)
# ==========================
@app.route("/")
def home():
    try:
        requests_ref = db.collection("requests").get()
        requests = []
        for r in requests_ref:
            req = r.to_dict()
            req["id"] = r.id
            requests.append(req)
        requests.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return render_template("dashboard.html", requests=requests)
    except Exception as e:
        flash(f"⚠️ Error loading dashboard: {e}", "danger")
        return render_template("dashboard.html", requests=[])

# ==========================
# ROUTE: View Request Details
# ==========================
@app.route("/request/<id>")
def request_detail(id):
    try:
        doc = db.collection("requests").document(id).get()
        if doc.exists:
            req = doc.to_dict()
            req["id"] = id
            return render_template("request_details.html", req=req)
        else:
            flash("⚠️ Request not found.", "danger")
            return redirect(url_for("home"))
    except Exception as e:
        flash(f"⚠️ Error loading request details: {e}", "danger")
        return redirect(url_for("home"))

# ==========================
# ROUTE: Resolve / Reply
# ==========================
@app.route("/resolve/<id>", methods=["GET", "POST"])
def resolve(id):
    doc_ref = db.collection("requests").document(id)
    try:
        if request.method == "POST":
            answer = request.form.get("answer", "").strip()
            if not answer:
                flash("⚠️ Please enter a valid reply before submitting.", "warning")
                return redirect(url_for("resolve", id=id))

            # Update Firestore document
            doc_ref.update({
                "status": "resolved",
                "answer": answer,
                "resolved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            flash("✅ Query resolved and answer saved successfully!", "success")
            return redirect(url_for("request_detail", id=id))

        # GET method – load existing data
        doc = doc_ref.get()
        if doc.exists:
            data = doc.to_dict()
            data["id"] = id
            return render_template("resolve.html", request_data=data)
        else:
            flash("⚠️ Request not found.", "danger")
            return redirect(url_for("home"))
    except Exception as e:
        flash(f"⚠️ Error resolving request: {e}", "danger")
        return redirect(url_for("home"))

# ==========================
# MAIN ENTRY
# ==========================
if __name__ == "__main__":
    print("✅ Firebase connection successful!")
    print("🚀 Flask Supervisor Dashboard running at http://127.0.0.1:5000")
    app.run(debug=True)
