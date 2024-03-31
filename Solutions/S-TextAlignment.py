# Enter your code here. Read input from STDIN. Print output to STDOUT
thickness = int(input())
h_letter = 'H'

# Top Cone
for i in range(thickness):
    print((h_letter * i).rjust(thickness - 1) + h_letter + (h_letter * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((h_letter * thickness).center(thickness * 2) +
          (h_letter * thickness).center(thickness * 6))

# Middle Belt
for i in range(int((thickness + 1) / 2)):
    print((h_letter * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((h_letter * thickness).center(thickness * 2) +
          (h_letter * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((h_letter * (thickness - i - 1)).rjust(thickness) + h_letter +
          (h_letter * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))