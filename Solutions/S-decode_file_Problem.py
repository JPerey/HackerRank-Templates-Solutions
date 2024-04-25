with open("inputs.txt", "r") as words:
    word_list = words.read().splitlines()

def sort_list(word_list):
    word_dict = {}
    sorted_list = []
    for item in word_list:
        split_item = item.split(" ")
        word_dict[int(split_item[0])] = split_item[1]

    sorted_dict = dict(sorted(word_dict.items()))

    for key, value in sorted_dict.items():
        temp = str(value)
        sorted_list.append(temp)

    return sorted_list

def create_staircase_example(word_list):
    step = 1
    subsets = []
    while len(word_list) != 0:
        if len(word_list) >= step:
            subsets.append(word_list[0:step])
            word_list = word_list[step:]
            step += 1
        else:
            return False
      
    return subsets

sorted_result = sort_list(word_list)

word_staircase = create_staircase_example(sorted_result)
#print(f"word_staircase: {word_staircase}")

#-----------------
#print(word_staircase)
i = 0
str_word = ""
while len(word_staircase) > i:
    str_word = str_word + " " + word_staircase[i][-1]
    
    i +=1

print(str_word)