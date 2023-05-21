# 12. Python program to check the validity of username and password input by users.
username = input("Enter your username: ")
password = input("Enter your new password: ")
def check_username(username,password):
    i = 0
    while i < 4:
        confirm_password = input("Confirm Your Password: ")
        if confirm_password == password:
            print("Account Successfully Created.")
            break
        else:
            print(f"Password didn't match! {3-i} attempts left...")
        if (3-i) < 1:
            print("You are blocked!")
        i += 1
check_username(username, password)

