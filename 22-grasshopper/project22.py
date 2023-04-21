n, k = map(int, input().split())

arr = [0] * n
arr[0] = 1

if(n > k):
  for i in range(k):
    arr[i] = sum(arr)

  for i in range(k, n):
    arr[i] = sum(arr[i-k:])
else:
  for i in range(n):
    arr[i] = sum(arr)

print(arr[-1])
