n = int(input())
maximum = 300 * n + 1
coupons = 1
days = []
arr = [[maximum]*(n+1) for _ in range(n)]

if n == 1:
  day = int(input())
  print(day)
  print("1 0" if day > 100 else "0 0")
elif n == 0:
  print(0)
  print(0,0)
else:
  day = int(input())
  days.append(day)
  if day > 100:
    arr[0][1] = day
    coupons += 1
  else:
    arr[0][0] = day

  for i in range(n-1):
    day = int(input())
    days.append(day)
    if day > 100:
      for j in range(coupons):
        if j != 0:
          arr[i+1][j-1] = min(arr[i][j], arr[i+1][j-1])
        arr[i+1][j+1] = min(arr[i][j] + day, arr[i+1][j+1])
      coupons += 1
    else:
      for j in range(coupons):
        if j != 0:
          arr[i+1][j-1] = min(arr[i][j], arr[i+1][j-1])
        arr[i+1][j] = min(arr[i][j] + day, arr[i+1][j])

  ind1 = len(arr[-1]) - arr[-1][::-1].index(min(arr[-1])) - 1
  ind = ind1
  print(arr[-1][ind])

  used = []
  for i in range(n-1, -1, -1):
    if arr[i][ind] == arr[i-1][ind+1]:
      ind += 1
      used.append(i+1)
    elif (days[i]!=0)and(arr[i][ind] == arr[i-1][ind-1] + days[i]):
      ind -= 1

  print(ind1, len(used))
  for u in used[::-1]:
    print(u)
