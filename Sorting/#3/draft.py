N = int(input())

students = {}

for _ in range(N):
  name, score = input().split()

  students[name] = int(score)

result = sorted(students, key=lambda item : item[1], reverse=True)

for i in result:
  print(i, end=" ")
