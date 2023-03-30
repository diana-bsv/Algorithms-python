import sys
sys.setrecursionlimit(200000)

def dfs(graph, visited, now, count):
  visited[now] = count
  for neig in graph[now]:
    if not visited[neig]:
      dfs(graph, visited, neig, count)

f = open("input.txt", 'r')
n, m = map(int, f.readline().split())
inp  = {i:0 for i in range(1, n+1)}
outp = [[] for _ in range(n+1)]
path = []
count = n
flag = 1

for i in f:
  f, g = map(int, i.split())
  if f == g:
    flag = 0
    continue
  outp[f].append(g)
  if g not in inp:
    inp[g] = 0
  inp[g] += 1

if flag:
  while(count):
    cnt = []
    for key, value in inp.items():
      if value == 0:
        for kid in outp[key]:
          inp[kid] -= 1
        cnt.append(key)
        count -= 1
    for i in cnt:
      path.append(i)
      inp.pop(i)
    if cnt == []:
      flag = 0
      break

if flag:
  print(*path)
else:
  print(-1)
