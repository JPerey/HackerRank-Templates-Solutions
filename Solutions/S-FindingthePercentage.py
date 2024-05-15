if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    

# print(student_marks)
# print(query_name)

for key in student_marks:
    if key == query_name:
        score_sum = sum(student_marks[key])
        #print(f"score_sum : {score_sum}")
        score_avg = float(score_sum)/ float(len(student_marks[key]))
        print(f"{format(score_avg,'.2f')}")