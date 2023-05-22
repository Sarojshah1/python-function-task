def fun():
    for i in range(3):
        userName, password = input("Enter Username:"), input("Enter Password:")
        if userName == 'username' and password == 'password':
            print('Access Granted')
            break
        elif i == 2:
            print("Account Blocked")
        else:
            print(
                f"Invalid Username or Password,Tried:{i+1} Remaning:{3-(i+1)}")


fun()
