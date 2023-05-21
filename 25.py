# 25. Multiplication of a list.
list = eval(input("Enter the elements: "))
def q25(list):
    product = 1
    i = 0
    while i < len(list):
        product *= list[i]
        i += 1
    print(f"The product of given numbers of a list is {product}.")
q25(list)

