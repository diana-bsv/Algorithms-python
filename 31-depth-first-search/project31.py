def dfs(graph, visited, now):
  visited[now] = True
  for neig in graph[now]:
    if not visited[neig]:
      dfs(graph, visited, neig)

n, m = map(int, input().split())
arr = [set() for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
  f, g = map(int, input().split())
  if f == g:
    continue
  arr[f].add(g)
  arr[g].add(f)

dfs(arr, visited, 1)

print(sum(visited))
for i in range(1, len(visited)):
    if visited[i]:
      print(i, end = " ")
