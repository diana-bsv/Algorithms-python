n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if n == 2:
  print(arr[1]-arr[0])
else:
  dp = [-1, (arr[1]-arr[0]), (arr[2] - arr[0])]
  for i in range(3, n):
    dp.append(arr[i] - arr[i-1] + min(dp[i-1], dp[i-2]))
  print(dp[-1])
