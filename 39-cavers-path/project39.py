f = open("input.txt", 'r')
n = int(f.readline())
pad = n+2
max_dist = 2

arr = [[[-1]*pad for _ in range(pad)]for _ in range(pad)]
for i in range(n):
  f.readline()
  for j in range(n):
    inp = f.readline()
    for ltr in range(n):
      if inp[ltr] == ".":
        arr[i+1][j+1][ltr+1] = 0
        max_dist += 1
      elif inp[ltr] == "S":
        arr[i+1][j+1][ltr+1] = 1
        tmp = [i+1, j+1, ltr+1]

dist = [[] for _ in range(max_dist)]
dist[1].append(tmp)

neighbours = lambda x: [[x[0],x[1]-1,x[2]], [x[0],x[1]+1,x[2]], [x[0],x[1],x[2]-1], [x[0],x[1],x[2]+1], [x[0]-1,x[1],x[2]], [x[0]+1,x[1],x[2]]]

now = 1
flag = 0

while(1):
  for i in dist[now]:
    for nei in neighbours(i):
      if not arr[nei[0]][nei[1]][nei[2]]:
        arr[nei[0]][nei[1]][nei[2]] = now + 1
        dist[now + 1].append([nei[0], nei[1], nei[2]])
        if nei[0] == 1:
          flag = 1
          tmp = now
  now += 1
  if flag:
    break

print(tmp)
