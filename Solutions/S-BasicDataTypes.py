if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sum = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    #print(f"student_marks: {student_marks} || n: {n} || query_name: {query_name}")

    query_result = student_marks[query_name]

    #print(f"query_result: {query_result}")
    i = 0
    for number in query_result:
        sum += number
        i += 1
        #print(f"i: {i}")

    average_score = format(sum / i, ".2f")

    print(average_score)
