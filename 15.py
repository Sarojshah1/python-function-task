# 15. Program to check given number is palindrome or not
string = input("Enter the string: ")
def q15(string):
    reverse = ""
    i = 0
    while i < len(string):
        reverse = string[i] + reverse
        i += 1
    if reverse == string:
        print("The given string is palindrome..")
    else:
        print("The given string is not a palindrome..")
q15()

