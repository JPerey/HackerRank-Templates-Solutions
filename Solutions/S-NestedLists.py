if __name__ == '__main__':
    score_list = []
    lowest = 100.00
    second_l = 0
    second_l_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([score, name])

    score_list.sort()
    i = 0

    lowest = score_list[0][0]

    for count, student in enumerate(score_list):
        if student[0] == lowest:
            continue
        if student[0] > lowest:
            if second_l == 0:
                second_l = student[0]
                second_l_list.append(student[1])
            elif second_l == student[0]:
                second_l_list.append(student[1])
            else:
                break

    second_l_list.sort()
    for name in second_l_list:
        print(name)
    # print(f"score_list: {score_list}")
    # print(f"second score list: {second_l_list}")
    # print(f"lowest: {lowest} || second lowest: {second_l}")
