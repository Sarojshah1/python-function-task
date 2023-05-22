def fun():
    str1 = input("Enter a string: ")
    str2 = ""

    for i in range(len(str1)):
        str2 = str1[i] + str2

    if (str2 == str1):
        print('Pallindrome')
    else:
        print('Not a Palindrome')


fun()
