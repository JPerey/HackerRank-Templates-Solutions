def split_and_join(line):
    # write your code here
    split_lines = line.replace(" ", "-")

    return split_lines


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
