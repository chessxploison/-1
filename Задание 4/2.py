def Task2(A, B):
  if A < B:
    for i in range(A, B + 1):
      print(i)
  else:
    for i in range(A, B - 1, -1):
      print(i)

A = int(input()) 
B = int(input())

print(Task2(A, B))
