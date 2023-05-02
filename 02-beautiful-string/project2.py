n = int(input())
strr = input()

dictt = {}

for i in range(len(strr)):
    if strr[i] not in dictt:
        dictt[strr[i]] = []
    dictt[strr[i]].append(i)

krasota = 1
for kk, w in dictt.items():
  i = 0
  j = 1
  btw = 0
  
  while j < len(w):
    
    if w[j] - w[i] - 1 <= n + btw:
      tmp = w[j] - w[i] + 1
      if tmp - 2 - btw < n:
        tmp = n + 2 + btw
      if tmp > krasota:
          krasota = tmp
      j += 1
      btw += 1
    else:
      i += 1
      btw -= 1

if krasota <= n :
        krasota = min(n+1, len(strr))
print(krasota)
