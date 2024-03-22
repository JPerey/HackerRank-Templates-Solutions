def count_substring(string, sub_string):
    string_length = len(string)
    string_len = len(string)
    sub_len = len(sub_string)
    sub_start = sub_string[0]
    matching = True
    pattern_count = 0
    
    for i in range(0,string_length):
        #print(f"i: {i}")
        if string[i] == sub_start:
            #print(f"match found - string[{i}]: {string[i]} || sub_start: {sub_start}")
            matching = True
            for j in range(0,sub_len):
                sumij = i + j
                if sumij < string_len:
                    #print(f"i: {i} || j: {j}")
                    if string[i+j] == sub_string[j]:
                        matching = True
                    else:
                        matching = False
                        break
                else:
                    matching = False
                    break
            if matching == True:
                pattern_count += 1
                    
    #print(f"pattern_count: {pattern_count}")
    return pattern_count