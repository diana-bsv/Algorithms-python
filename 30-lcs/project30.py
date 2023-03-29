len_a = int(input())
a = [0] + list(input().split())
len_b = int(input())
b = [0] + list(input().split())

arr = [[0] * (len_b + 1) for _ in range(len_a + 1)]

for i in range(1, len_a+1):
  for j in range(1, len_b+1):
    if a[i] == b[j]:
      arr[i][j] = arr[i-1][j-1] + 1
    else:
      arr[i][j] += max(arr[i][j-1], arr[i-1][j])


path = []
i = len_a
j = len_b
while i>1 or j>1:
  if (arr[i][j] == arr[i-1][j]) and (i>1):
    i -= 1
  elif (arr[i][j] == arr[i][j-1]) and (j>1):
    j -= 1
  else:
    path.append(a[i])
    i -= 1
    j -= 1
    
if a[1] == b[1]:
  path.append(a[1])

for i in path[::-1]:
  print(i, end = " ")
