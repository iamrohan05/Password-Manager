username = input("Please, enter your username: ")  # Get initial username
current_pwd = input("Please, enter your master password: ")  # Get initial password

def change_pw(actual_pw):
    current_pw = input("🔒 Please, enter your current password: ")
    if current_pw == actual_pw:
        print("✅ Access Granted.")
        new_pw = input("🔑 Enter your new password: ")
        print("🎉 Your password has been changed successfully!")
        return new_pw
    else:
        print("❌ Password Incorrect!!")
        return actual_pw  # Return old password if wrong

def change_user(actual_pw,old_username):
    entered_pwd = input("🔒 Please, enter your current password to change username: ")
    if entered_pwd == actual_pw:
        new_user = input("👤 Enter your new username: ")
        print("🎉 Your username has been changed successfully!!")
        return new_user
    else:
        print("❌ Password Incorrect!! Username not changed.")
        return old_username  # Return old username if wrong

def view_info():
    print("👀 Viewing your information")
    Name = "Rohan Bhandari"
    Age = 20
    Phone_num = 1234567890
    print("Name: ", Name)
    print("Age: ", Age)
    print("Phone number: ", Phone_num)

while True:
    option = input("Choose an option:\n1. Change Password 🔑\n2. Change Username 👤\n3. View Current Info 📋\n4. Quit ❌\n")

    if option not in ["1", "2", "3", "4"]:
        print("⚠️ Invalid input! Please enter a number between 1 and 4.")
        continue

    option = int(option)

    if option == 1:
        current_pwd = change_pw(current_pwd)

    elif option == 2:
        username = change_user(current_pwd,username)

    elif option == 3:
        view_info()

    elif option == 4:
        print("👋 Exiting!!")
        break

    print("\n🔁 Back to main menu...\n")
