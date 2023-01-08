'''
We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of 'x' is equal to the super digit of the sum of the digits of 'x'.
'''
# method #1 - using recursion


# def superDigit(n, k):

#     # base-case: when do we stop recursion? When the input digit is a single digit
#     # logic: 1) split parameter into list of digits, and then sum, and then pass into superDigit
#     # what does it return? a single digit
#     summed_digit = 0
#     n_concat = str(n)
#     if k > 0:
#         for iteration in range(k-1):
#             n_concat = n_concat + str(n)
#         k = 0

#     for digit in n_concat:
#         summed_digit += int(digit)

#     if summed_digit > 9:
#         summed_digit = superDigit(summed_digit, k)

#     return summed_digit


# response = superDigit(123, 3)

# print(f"response: {response}")

# method #2 - using recursion

def superDigit(n, k):
    num_list = list(map(int, n))
    sum_num = sum(num_list)

    result = sum_num*k if k else sum_num

    if result < 10:
        return result

    else:
        return superDigit(str(result), 0)


response = superDigit("123", 3)

print(f"response: {response}")
