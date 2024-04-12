# Enter your code here. Read input from STDIN. Print output to STDOUT
shoe_amt = int(input())
shoe_size_str = input()
shoe_size_list = list(shoe_size_str.split(" "))
customer_amt = int(input())
current_customer = []
#key: 0 for key in shoe_size_list
shoe_dict = {key: 0 for key in shoe_size_list}
#print(f"shoe_dict before : {shoe_dict}")
# for j in shoe_size_list:
#     key_name = int(shoe_dict[j])
#     key_name = 0

for i in range(customer_amt):
    current_customer.append(tuple(input().split(" ")))
    #print(f"current[{i}][0] : {current_customer[i][0]}")
    if current_customer[i][0] in shoe_size_list:
        #print("theres a pair!")
        current_rev = shoe_dict.get(current_customer[i][0])
        price_increase = int(current_customer[i][1]) + current_rev
        shoe_dict.update({current_customer[i][0] : price_increase})
        #print(f"current rev {current_customer[i][0]}: {shoe_dict.get(current_customer[i][0])}")
        shoe_size_list.remove(current_customer[i][0])



#print(f"shoe_amt: {shoe_amt} || shoe_size_list: {shoe_size_list} || Customer_amt : {customer_amt}")

#print(f"shoe_dict after: {shoe_dict}")
values = shoe_dict.values()
sum_values = sum(values)
print(f"{sum_values}")