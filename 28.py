# 28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
list = eval(input("Enter the elements: "))
def q28(list):
    i = 0
    while i < len(list):
        if type(list[i]) == str:
            print("Hello! " + list[i].capitalize())
        i += 1
q28(list)