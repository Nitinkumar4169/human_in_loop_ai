import json
from datetime import datetime
from db.firebase_config import db

# -------------------------------
# Load salon knowledge base
# -------------------------------
with open("ai_agent/prompt_data.json", "r") as f:
    salon_data = json.load(f)

# -------------------------------
# Agent Prompt (for clarity)
# -------------------------------
AGENT_PROMPT = """
# Identity
You are an AI receptionist for GlowUp Salon.
You greet customers, answer questions, and ask for supervisor help when needed.

# Instructions
- Be polite and concise.
- Use only information from the salon data.
- If unsure, respond with: "Let me check with my supervisor and get back to you."
- Never invent information.

# Examples
Customer: What time do you open?
AI: Our working hours are 9 AM - 8 PM.

Customer: Do you offer bridal makeup?
AI: Let me check with my supervisor and get back to you.
"""

# -------------------------------
# Core logic
# -------------------------------
def handle_query(query: str) -> str:
    query = query.lower().strip()

    # Known info checks
    for service in salon_data["services"]:
        if service.lower() in query:
            return f"Yes! We offer {service} services at {salon_data['salon_name']}."

    if "time" in query or "hours" in query:
        return f"Our working hours are {salon_data['hours']}."

    if "location" in query or "where" in query:
        return f"We are located at {salon_data['location']}."

    if "contact" in query or "phone" in query:
        return f"You can reach us at {salon_data['contact']}."

    # Unknown → create help request
    create_help_request(query)
    return "Let me check with my supervisor and get back to you."

# -------------------------------
# Store unresolved queries in Firebase
# -------------------------------
def create_help_request(query: str):
    data = {
        "query": query,
        "status": "pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    db.collection("requests").add(data)
    print(f"📩 Help request created → {query}")

# -------------------------------
# Simulation: terminal-based call
# -------------------------------
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
