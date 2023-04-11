n, m = map(int, input().split())

arr = [[0]*(m+2) for _ in range(n+2)]
arr[0][1] = 1

for i in range(2, n+2):
  for j in range(2, m+2):
    arr[i][j] = arr[i-2][j-1] + arr[i-1][j-2]

print(arr[-1][-1])
