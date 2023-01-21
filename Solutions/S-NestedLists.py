if __name__ == '__main__':
    score_list = []
    lowest = 100.00
    second_l = 100.00
    third_l = 100.00
    second_l_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        print(f"score: {score} || lowest: {lowest} || second l: {second_l}")
        score_list.append([score, name])

    score_list.sort()
    i = 0

    while second_l == third_l:
        if i == 0:
            lowest == score_list[i][0]
            second_l == score_list[i][0]
            third_l == score_list[i][0]
        if score_list[i][0] > lowest:
            if score_list[i][0] > second_l:
                third_l = score_list[i][0]
            else:
                second_l = score_list[i][0]
                second_l_list.append(score_list[i][1])

        i += 1

    print(f"score_list: {score_list}")
    print(f"lowest: {lowest} || second lowest: {second_l}")
