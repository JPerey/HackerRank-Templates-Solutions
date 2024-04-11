# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def create_top(n,m):
    line_dots = ".|."
    initial_line = "-"*(m-1)
    middle = math.floor(m / 2)
    list_top= []
    half_n = int((n - 1)/2)
    dots_index = 1

    for i in range(0,half_n):
        list_top.append(initial_line[: middle - 1 - (i*3)] + (line_dots*dots_index) + initial_line[middle + 1 + (i*3):])
        dots_index += 2
    return list_top

def create_bot(top):
    list_bot = list(reversed(top))
    
    return list_bot
    
def create_mid(m):
    initial_line = "-"*(m-1)
    middle = math.floor(m / 2)
    welcome = "WELCOME"
    mid_line = initial_line[: middle - 3] + welcome + initial_line[middle + 3:]
    
    return mid_line
    
numbers = input()
nums_split = numbers.split()

n = int(nums_split[0])
m = int(nums_split[1])
#print(f"n: {n} || m: {m}")
top = create_top(n,m)
#print(f"top:{top}")
bot = create_bot(top)
#print(f"bot:{bot}")
mid = create_mid(m)
#print(f"mid:{mid}")

for j in range(len(top)):
    print(top[j])
for l in range(1):
    print(mid)
for k in range(len(bot)):
    print(bot[k])
#print(f"nums_split: {nums_split}")