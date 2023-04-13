n, m = map(int, input().split())
maximum = 101 * max(n,m)
arr = [[]] * (n+1)
for i in range(1, n+1):
  arr[i] = [maximum] + list(map(int, input().split()))
arr[0] = [maximum] * (m+1)

arr[0][0] = 0
arr[0][1] = 0
arr[1][0] = 0

for i in range(1, n+1):
  for j in range(1, m+1):
    arr[i][j] += min(arr[i][j-1], arr[i-1][j])

print(arr[n][m])
