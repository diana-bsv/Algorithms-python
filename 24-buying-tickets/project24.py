n = int(input())

a = [4000]*3
b = [4000]*3
c = [4000]*3
dp = [0]*3

for i in range(n):
  a_0, b_0, c_0 = map(int, input().split())
  a.append(a_0)
  b.append(b_0)
  c.append(c_0)

for i in range(3, n+3):
  dp.append(min(a[i] + dp[i-1], b[i-1] + dp[i-2], c[i-2] + dp[i-3]))

print(dp[n+2])
