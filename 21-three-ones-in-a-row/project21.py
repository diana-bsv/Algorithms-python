n = int(input())

dp = [0, 2, 4, 7]
if n > 3:
  for i in range(4, n+1):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])
print(dp[n])