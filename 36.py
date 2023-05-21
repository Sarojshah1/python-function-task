# 36. Remove bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
string = "py;th* o:n ! ;py * t*h:o !n"
badChars = [';', ':', '!', "*"]
def q36(string,badChars):
    i = 0
    while i < len(badChars):
        if badChars[i] in string:
            string = string.replace(badChars[i],"")
            string = string.replace(" ","")
        i += 1
    print(string)
q36(string, badChars)