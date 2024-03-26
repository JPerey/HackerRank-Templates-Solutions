if __name__ == '__main__':
    s = input()
    len_s = len(s)
    alphanum_chars = False
    #print(f"aphanum: {alphanum_chars}")
    alpha_chars = False
    digit_chars = False
    lower_chars = False
    upper_chars = False
    #print(f"string: {s}")
    
    for letter in s:
        #print(f"letter: {letter}")
        #if letter == "#" or letter == "$" or letter == "%" or letter == "@" or letter == "^" or letter == "&" or letter == "*" or letter == "~" or letter == "`" or letter == ":" or letter == ";" or letter == "," or letter == "." or letter == " " or letter == "/" or letter == "'":
        if letter.isalnum() and alphanum_chars == False:
            alphanum_chars = True
        if letter.isalpha() and alpha_chars == False:
            alpha_chars = True
        if letter.isdigit() and digit_chars == False:
            digit_chars = True
        if letter.islower() and lower_chars == False:
            lower_chars = True
        if letter.isupper() and upper_chars == False:
            upper_chars = True
    print(f"{alphanum_chars}")
    print(f"{alpha_chars}")
    print(f"{digit_chars}")
    print(f"{lower_chars}")
    print(f"{upper_chars}")