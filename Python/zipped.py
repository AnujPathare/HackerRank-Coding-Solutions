# Enter your code here. Read input from STDIN. Print output to STDOUT

subjects, students = map(int, input().split())

record = []
for i in range(students):
    marks = list(map(float, input().split()))
    record.append(marks)

for subj_mark in zip(*record):
    print(round(sum(subj_mark) / len(subj_mark), 1))