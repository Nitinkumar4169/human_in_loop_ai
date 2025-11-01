# 🧠 Human-in-the-Loop AI Supervisor

### 🚀 Frontdesk Engineering Test — AI Receptionist System

A locally running simulation of an **AI receptionist** that:
- Handles customer queries
- Escalates unknown questions to a **human supervisor**
- Updates its **knowledge base automatically** after learning new answers

---

## 🏗️ Project Overview

This project demonstrates a **human-in-the-loop AI system** where an AI agent collaborates with a human supervisor for decision-making.  
If the AI cannot answer a customer’s query, it escalates to a human, learns the correct answer, and updates its own database for future responses.

The focus is on **clarity, modularity, and reliability**, not polish.

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Python (Flask) |
| **AI Simulation** | LiveKit SDK |
| **Database** | Firebase (Firestore) |
| **Frontend (Admin Panel)** | HTML + Flask Templates |
| **Version Control** | Git & GitHub |
| **Environment** | Local (Python 3.10+) |

---

## 🧩 Features

- 🤖 **AI Agent Simulation** — handles queries & escalates unknown ones  
- 👨‍💼 **Supervisor Panel** — view/respond to pending help requests  
- 🧠 **Knowledge Base Learning** — saves and reuses learned answers  
- 🔄 **Lifecycle Management** — requests move from *Pending → Resolved/Unresolved*  
- ⚙️ **Error Handling** — simple, reliable architecture  

---

## 🧱 Folder Structure

human_in_loop_ai/
│
├── ai_agent/ # AI logic for handling and escalating queries
│ ├── agent.py
│ ├── prompt_data.json
│
├── supervisor_ui/ # Flask app for human supervisor interface
│ ├── app.py
│ ├── templates/
│ │ ├── pending.html
│ │ ├── learned.html
│ │ ├── history.html
│
├── db/ # Firebase configuration and data models
│ ├── firebase_config.py
│ ├── models.py
│
├── config/ # Service account keys and settings
│ ├── firebase_key.json
│
├── README.md
├── requirements.txt
└── .gitignore

yaml
Copy code

---

## ⚡ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Nitinkumar4169/human-in-loop-ai.git
cd human-in-loop-ai
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate     # Windows
# or
source venv/bin/activate  # macOS/Linux
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Configure Firebase
Go to Firebase Console

Create a new project and enable Firestore Database

Generate a Service Account Key

Save it as:

arduino
Copy code
config/firebase_key.json
🧠 How It Works
AI receives a simulated customer call/query

If the query is known → AI responds immediately

If unknown → creates a help request in the database

Supervisor views the request on the web panel → submits an answer

AI follows up with the customer and stores the new information

🧑‍💻 Run the Application
Start the Flask app:

bash
Copy code
python supervisor_ui/app.py
Then open your browser at:

cpp
Copy code
http://127.0.0.1:5000
You’ll see:

Pending Help Requests

Respond Page

Learned Answers

🧩 Example Console Output
text
Copy code
AI: Hello! How can I help you today?
User: Do you offer hair coloring?
AI: Yes, we offer Haircut, Coloring, and Facial services!

User: Do you provide bridal makeup?
AI: Let me check with my supervisor and get back to you.
Supervisor Alert: "Hey, I need help answering: Do you provide bridal makeup?"
🧱 Design Highlights
Modular architecture (AI, UI, and DB separated)

Scales easily from 10 → 1,000+ requests/day

Graceful handling of timeouts and unresolved cases

Clean database relations for request lifecycle

🚀 Future Enhancements
Real phone integration using Twilio

Live call handoff for supervisors

Authentication for supervisors

React/Tailwind-based frontend

Dockerized deployment

🎥 Demo Video (Submission)
Record a short demo showing:

System overview

How the AI escalates and learns

Key design decisions & improvements

👨‍💻 Author
Nitin Kumar
📧 nitinkmr.4169@gmail.com
💼 GitHub Profile

📄 License
This project was created for the Frontdesk Engineering Test.
Free to use for educational and demonstration purposes.

yaml
Copy code

---

### ✅ Instructions
1. Open **VS Code**
2. In the Explorer, right-click → **New File** → name it `README.md`
3. Paste everything above
4. Save (Ctrl + S)
5. Commit & push:
   ```bash
   git add README.md
   git commit -m "Added professional README"
   git push