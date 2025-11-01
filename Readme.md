🧠 Human-in-the-Loop AI Supervisor
🚀 Frontdesk Engineering Test — AI Receptionist System
A locally running simulation of an AI receptionist that:


Handles customer queries


Escalates unknown questions to a human supervisor


Updates its knowledge base automatically after learning new answers



🏗️ Project Overview
This project demonstrates a human-in-the-loop AI system where an AI agent collaborates with a human supervisor for decision-making.
If the AI cannot answer a customer’s query, it escalates to a human, learns the correct answer, and updates its own database for future responses.
It is designed for clarity, modularity, and reliability, focusing on production-ready architecture rather than polish.

⚙️ Tech Stack
LayerTechnology UsedBackendPython (Flask)AI SimulationLiveKit SDK (Python)DatabaseFirebase (Firestore)Frontend (Admin Panel)HTML + Flask TemplatesVersion ControlGit & GitHubEnvironmentLocal (Virtual Environment + Python 3.10+)

🧩 Features Implemented
✅ AI Agent Simulation


Uses LiveKit (or mock simulation) to receive customer “calls”


Responds automatically if it knows the answer


Escalates unknown questions to a human


✅ Human Supervisor Panel


Simple web interface (Flask)
View all pending help requests
Submit answers and mark requests as resolved/unresolved


✅ Knowledge Base Learning

AI automatically saves learned responses
Uses these learned answers in future interactions


✅ Request Lifecycle Management

Tracks requests from Pending → Resolved/Unresolved
Handles timeout gracefully



🧱 Folder Structure
human_in_loop_ai/
│
├── ai_agent/                 # AI logic for handling and escalating queries
│   ├── agent.py
│   ├── prompt_data.json
│
├── supervisor_ui/            # Flask app for human supervisor interface
│   ├── app.py
│   ├── templates/
│   │   ├── pending.html
│   │   ├── learned.html
│   │   ├── history.html
│
├── db/                       # Firebase database configuration and models
│   ├── firebase_config.py
│   ├── models.py
│
├── config/                   # Firebase keys or other configurations
│   ├── firebase_key.json
│
├── README.md                 # Project documentation (this file)
├── requirements.txt          # Python dependencies
└── .gitignore                # Ignored files and directories


⚡ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Nitinkumar4169/human-in-loop-ai.git
cd human-in-loop-ai

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate     # For Windows
# or
source venv/bin/activate  # For macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up Firebase


Go to Firebase Console


Create a project → enable Firestore Database


Generate Service Account Key → download JSON


Place it in:
config/firebase_key.json




🧠 How It Works
AI Flow:


AI receives simulated call/query


If answer found → responds directly


If unknown → creates a “help request” in database


Supervisor views it on web panel → submits answer


AI automatically follows up and updates its knowledge base



🧑‍💻 Run the Application
Start Flask Server:
python supervisor_ui/app.py

Then open your browser at:
👉 http://127.0.0.1:5000
You’ll see:


Pending Help Requests


Respond Page


Learned Answers



🧩 Example Console Output
AI: Hello! How can I help you today?
User: Do you offer hair coloring?
AI: Yes, we offer Haircut, Coloring, and Facial services!

User: Do you provide bridal makeup?
AI: Let me check with my supervisor and get back to you.
Supervisor Alert: "Hey, I need help answering: Do you provide bridal makeup?"


🧠 Design Choices

Modular code structure for scalability
Separated agent, database, and UI logic
Graceful error handling for missing data or timeouts
Designed to scale from 10 to 1,000+ requests/day



📈 Future Improvements


Real phone integration using Twilio API
Supervisor live call handoff (Phase 2)
User authentication for supervisors
Better UI styling using React or Tailwind
Docker deployment setup



📷 Demo Video (For Submission)
🎥 Record a short walkthrough explaining:


How the system works


Your code structure and design


Future improvements



🧑‍🏫 Author
Nitin Kumar
📧 nitinkmr.4169@gmail.com
💼 GitHub: Nitinkumar4169

📄 License
This project was created for the Frontdesk Engineering Test.
Free to use for educational or demonstration purposes only.

Would you like me to make a slightly shorter README version (for interview submission) — one that focuses only on setup + demo instructions (less theoretical text)? It’s ideal if recruiters only skim your GitHub repo.
