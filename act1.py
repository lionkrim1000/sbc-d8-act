import os

# Global variables
credentials_file = "accounts.txt"
users_dict = {}

def accs():
    global users_dict
    if os.path.exists(credentials_file):
        with open(credentials_file, 'r') as file:
            for line in file:
                username, password = line.strip().split(':')
                users_dict[username] = password

def save():
    with open(credentials_file, 'w') as file:
        for username, password in users_dict.items():
            file.write(f"{username}:{password}\n")

def register():
    print("Please enter your details to register.")
    username = input("Enter username: ")
    while username in users_dict:
        print("Username already exists. Please choose another one.")
        username = input("Enter username: ")
    password = input("Enter password: ")
    users_dict[username] = password
    save()
    print("Registration successful!")

def login():
    print("Please enter your login details.")
    username = input("Username: ")
    password = input("Password: ")
    if username in users_dict and users_dict[username] == password:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

def change_password(username):
    new_password = input("Enter your new password: ")
    users_dict[username] = new_password
    save()
    print("Password changed successfully!")

def main():
    accs()
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Change Password")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                pass 
        elif choice == '3':
            if login():
                change_password(username=input("Enter username: "))
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
