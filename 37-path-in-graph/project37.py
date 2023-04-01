f = open("input.txt", 'r')
n = int(f.readline())
arr = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
dist    = [[] for _ in range(n+1)]

i = -1
for ik in f:
  i += 1
  tmp = list(map(int, ik.split()))
  for j in range(i, n):
    if i == j:
      continue
    else:
      if tmp[j]:
        arr[i+1].append(j+1)
        arr[j+1].append(i+1)

start, end = map(int, ik.split())
if start == end:
  print(0)
else:
  now = start
  count = 0
  dist[0] = [start]
  visited[start] = 0

  while(1):
    for this_dist in dist[count]:
      for neig in arr[this_dist]:
          if visited[neig] == -1:
            visited[neig] = count + 1
            dist[count + 1].append(neig)
    if visited[end] != -1:
      break
    if dist[count] == []:
      break
    count += 1

  count = visited[end]
  print(count)


  if count != -1:
    path = [0]*(count+1)
    now = end
    for i in range(count, 0, -1):
      path[i] = now
      count -= 1
      now = list(filter(lambda x: visited[x] == count, arr[now]))[0]
    path[0] = now
    print(*path)
