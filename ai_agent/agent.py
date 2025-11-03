import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from datetime import datetime
from db.firebase_config import db


# Load static salon data
with open("ai_agent/prompt_data.json", "r") as f:
    salon_data = json.load(f)

# Load dynamic knowledge from Firebase
def load_resolved_knowledge():
    docs = db.collection("requests").where("status", "==", "resolved").get()
    knowledge = {}
    for doc in docs:
        data = doc.to_dict()
        question = data.get("query", "").lower().strip()
        answer = data.get("answer", "")
        if question and answer:
            knowledge[question] = answer
    print(f"🧠 Loaded {len(knowledge)} learned answers from Firebase.")
    return knowledge

resolved_knowledge = load_resolved_knowledge()

def handle_query(query: str) -> str:
    q = query.lower().strip()

    # Check learned responses
    if q in resolved_knowledge:
        return resolved_knowledge[q]

    # Check predefined salon info
    for service in salon_data["services"]:
        if service.lower() in q:
            return f"Yes! We offer {service} services at {salon_data['salon_name']}."
    if "time" in q or "hours" in q:
        return f"Our working hours are {salon_data['hours']}."
    if "location" in q or "where" in q:
        return f"We are located at {salon_data['location']}."
    if "contact" in q or "phone" in q:
        return f"You can reach us at {salon_data['contact']}."

    # Unknown → send to Firebase help request
    create_help_request(q)
    return "Let me check with my supervisor and get back to you."

def create_help_request(query: str):
    data = {
        "query": query,
        "status": "pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    db.collection("requests").add(data)
    print(f"📩 Help request created → {query}")

def simulate_call():
    print("📞 Call started — type a query (or 'exit' to end):")
    while True:
        user_input = input("Customer: ")
        if user_input.lower() in ["exit", "quit"]:
            print("📴 Call ended.")
            break
        print("AI:", handle_query(user_input))

if __name__ == "__main__":
    simulate_call()
