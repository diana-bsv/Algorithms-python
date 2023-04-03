import sys
sys.setrecursionlimit(200000)

def dfs(graph, visited, path, flag, now):
  visited[now] = 1
  path.append(now)
  for neig in graph[now]:
    if neig != path[-2] and visited[neig] == 1:
      if flag:
        flag = 0
        start = path.index(neig)
        print("YES")
        print(len(path[start:]))
        print(*path[start:])

    elif not visited[neig]:
      prev = now
      flag = dfs(graph, visited, path, flag, neig)
  visited[now] = 2
  path.pop()
  return flag


f = open("input.txt", 'r')
n = int(f.readline())
arr = [[] for _ in range(n+1)]
visited = [0]*(n+1)
flag = 1
path = [0]
path_true = []
tru = 0

i = -1
for ik in f:
  i += 1
  tmp = list(map(int, ik.split()))
  for j in range(i, n):
    if tmp[j] == 1:
      if i == j:
        flag = 0
        path = [i+1, i+1]
      else:
        arr[i+1].append(j+1)
        arr[j+1].append(i+1)
    elif tmp[j]>1:
      flag = 0
      path = [i+1, j+1]

if flag:
  for i in range(1, n+1):
    if not visited[i]:
      flag = dfs(arr, visited, path, flag, i)

if flag:
  print("NO")
