import sys
sys.setrecursionlimit(200000)

def dfs(graph, visited, visited_old, now, count):
  visited[count].append(now)
  visited_old[now] = count + 1
  for neig in graph[now]:
    if not visited_old[neig]:
      dfs(graph, visited, visited_old, neig, count)

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited_old = [0]*(n+1)
visited = []

for i in range(m):
  f, g = map(int, input().split())
  if f == g:
    continue
  arr[f].append(g)
  arr[g].append(f)

count = -1

for i in range(1, n+1):
  if not visited_old[i]:
    count += 1
    visited.append([])
    dfs(arr, visited, visited_old, i, count)
    
print(count+1)

for ab in range(0, count+1):
    print(len(visited[ab]))
    print(*visited[ab])
