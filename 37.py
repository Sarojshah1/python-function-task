def fun():
    num_list = [2, 5, 7, 8, 10, 13, 15, 16]
    even_count = 0
    odd_count = 0

    for num in num_list:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)


fun()
