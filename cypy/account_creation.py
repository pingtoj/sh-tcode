import bcrypt

user_db = {}

_names = ["tina", "mina", "jina", "sina"]
username = input("Enter username: ").strip().lower()

while True:
    password_input = input("Enter password: ").strip()
    if password_input.lower() in _names:
        print("Invalid! — password cannot be the name of your spouse or girlfriend.")
    else:
        password = password_input.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        user_db[username] = hashed
        print("\n Registration successful! Welcome to the hood!")
        break