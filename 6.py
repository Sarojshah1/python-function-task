# 6. Multiplication table of a given number.

def q6():
    num = int(input("Enter the number: "))
    i=1
    while i < 11:
        print(num,"*",i,"=",num*i)
        i=i+1
q6()
