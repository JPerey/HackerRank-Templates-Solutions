def swap_case(s):
    #print(f"s: {s}")
    final_string = ""

    for n in s:
        if n.isupper():
            lowercased = n.lower()
            final_string += lowercased
        elif n.islower():
            uppercased = n.upper()
            final_string += uppercased
        else:
            final_string += n
    #print(f"final string: {final_string}")
    return final_string
