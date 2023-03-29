f = open("input.txt", 'r')
n, m, s, t, q = map(int, f.readline().split())

max_dist = 2
s += 1
t += 1
arr = [[-2]*(m + 4)] + [[-2]*(m + 4)] + [[-2]*2 + [-1]*m + [-2]*2 for _ in range(n)] + [[-2]*(m + 4)] + [[-2]*(m + 4)]
arr[s][t] = 0
neighbours = lambda x: [[x[0]-2,x[1]+1], [x[0]-1,x[1]+2], [x[0]+1,x[1]+2], [x[0]+2,x[1]+1], [x[0]+2,x[1]-1], [x[0]+1,x[1]-2], [x[0]-1,x[1]-2], [x[0]-2,x[1]-1]]

dist = [[]]
dist[0].append([s,t])

now = 0
flag = 0

while(1):
  for i in dist[now]:
    dist.append([])
    for nei in neighbours(i):
      if arr[nei[0]][nei[1]] == -1:
        arr[nei[0]][nei[1]] = now + 1
        dist[now + 1].append([nei[0], nei[1]])
  now += 1
  if dist[now] == []:
    break

sum = 0
flag = 1
for _ in range(q):
  x, y = map(int, f.readline().split())
  if arr[x+1][y+1] != -1:
    sum += arr[x+1][y+1]
  else:
    flag = 0
    print(-1)
    break

if flag:
  print(sum)
