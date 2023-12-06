def Task3(A, B):

while A > B:
  for i in range(A, B - 1, -1):
    if i % 2 != 0:
      print(i)

A = int(input()) 
B = int(input()) 

print(Task3(A, B))
