def fun():
    bad_chars = [';', ':', ' ', '!', '*']
    string = "py;th* o:n ! ;py * t*h:o !n"

    for char in bad_chars:
        string = string.replace(char, '')

    print(string)


fun()
