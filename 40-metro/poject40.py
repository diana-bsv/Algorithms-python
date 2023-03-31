f = open("input.txt", 'r')
n = int(f.readline())
m = int(f.readline())

inp = [[] for _ in range(m)]

for i in range(m):
  inp[i] = set(map(int, f.readline().split()[1:]))

start, end = map(int, f.readline().split())
ends = []

lines = [[] for _ in range(m)]
visited = [-1] * m
dist = [[]]

for i in range(m):
  for j in range(i+1, m):
    if inp[i] & inp[j]:
      lines[i].append(j)
      lines[j].append(i)
  if start in inp[i]:
    visited[i] = 0
    dist[0].append(i)
  if end in inp[i]:
    ends.append(i)

flag = 1

for i in ends:
  if visited[i] == 0:
    flag = 0
    print(0)
    break

now = 0
if flag:
  ends2 = []
  while(1):
    for i in dist[now]:
      dist.append([])
      for nei in lines[i]:
        if visited[nei] == -1:
          visited[nei] = now + 1
          dist[now + 1].append(nei)
    now += 1
    if dist[now] == []:
      break
  for i in ends:
    ends2.append(visited[i])
  print(min(ends2))
