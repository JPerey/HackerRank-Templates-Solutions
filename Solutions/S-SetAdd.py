total_stamps = int(input())
amount = set()
amount_len = 0

#print("total_stamps: " + total_stamps)

for i in range(total_stamps):
    country_stamp = input()
    #print(country_stamp)
    amount.add(country_stamp)
    #print(amount)
    
amount_len = len(amount)
print(amount_len)