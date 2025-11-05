# create_supervisor.py
import json
import getpass
from werkzeug.security import generate_password_hash

def main():
    email = input("Supervisor email (login): ").strip()
    password = getpass.getpass("Supervisor password: ")
    confirm = getpass.getpass("Confirm password: ")
    if password != confirm:
        print("Passwords do not match.")
        return
    hashed = generate_password_hash(password)
    supervisor = {
        "email": email,
        "password": hashed,
        "role": "supervisor",
        "name": email.split("@")[0]
    }
    try:
        data = {}
        with open("supervisors.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    data[email] = supervisor
    with open("supervisors.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Supervisor {email} saved in supervisors.json")

if __name__ == "__main__":
    main()
