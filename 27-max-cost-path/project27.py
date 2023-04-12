n, m = map(int, input().split())
arr = [[]] * (n+1)
for i in range(1, n+1):
  arr[i] = [0] + list(map(int, input().split()))
arr[0] = [0] * (m+1)

for i in range(1, n+1):
  for j in range(1, m+1):
    arr[i][j] += max(arr[i][j-1], arr[i-1][j])

path = []
i = n
j = m
while i>1 or j>1:
  if (j>1)and(arr[i][j-1] >= arr[i-1][j]):
    path.append("R")
    j -= 1
  else:
    path.append("D")
    i -= 1

print(arr[n][m])
for i in path[::-1]:
  print(i, end = " ")
