def print_formatted(number):
    number = n
    width = len(bin(number)[2:])
    dec_num = 0
    oct_num = ""
    hex_num = 0
    bin_num = 0
    format_list = []
    
    for i in range(number):
        dec_num = str(i + 1)
        octal_i = i + 1
        #octal number section - BEGIN
        while octal_i > 0:
            oct_num = str(octal_i % 8) + oct_num
            octal_i = octal_i // 8
        #octal number section - END
        
        #hexadecimal number section - BEGIN
        hex_num = hex(i + 1)
        split_hex_str = hex_num[2:]
        cap_hex = split_hex_str.upper()
                      
        #hexadecimal number section - END
        
        #binary number section - BEGIN
        bin_num = bin(i + 1)
        split_bin_str = bin_num[2:]
        #binary number section - END
        # adding to list
        format_list.append(dec_num.rjust(width) + " " + oct_num.rjust(width) + " " 
        + cap_hex.rjust(width) + " " + split_bin_str.rjust(width))
        # FOR LOOP - END actions
        oct_num = ""
        split_hex_str = ""
        cap_hex = ""
        dec_num = ""
        split_bin_str = ""
    for k in range(len(format_list)):
        print(format_list[k])


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)