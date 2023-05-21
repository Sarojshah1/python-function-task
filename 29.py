# 29. Using a while loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
list = eval(input("Enter the elements: "))
def q29(list):
    i = 0
    merit_list = []
    while i < len(list):
        if type(list[i]) == str:
            merit_list.append("Dr." + list[i].capitalize())
        i += 1
    print(merit_list)
q29(list)

