import sys
sys.setrecursionlimit(200000)

def dfs(graph, visited, now, count):
  for kid in graph[now]:
    if visited[kid] == count:
      visited[0] = "NO"
  visited[now] = count
  count = 3 - count
  for neig in graph[now]:
    if not visited[neig]:
      dfs(graph, visited, neig, count)

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [0]*(n+1)
visited[0] = "YES"

for i in range(m):
  f, g = map(int, input().split())
  if f == g:
    continue
  arr[f].append(g)
  arr[g].append(f)

count = 1

for i in range(1, n+1):
  if not visited[i]:
    #count += 1
    dfs(arr, visited, i, count)
    
print(visited[0])
