n = int(input())
x = 0
heap = []
for _ in range(n):
  inp = input()
  try:
    tmp = int(inp)
  except ValueError:
    tmp, x = map(int, inp.split())
  
  if tmp: #extract
    print(heap[0])
    heap[0] = heap[-1]
    pos = 0
    while 2*pos+2 < len(heap):
      max_kid = 2*pos+1
      if heap[max_kid] < heap[max_kid+1]:
        max_kid += 1
      if heap[pos] < heap[max_kid]:
        heap[pos], heap[max_kid] = heap[max_kid], heap[pos]
        pos = max_kid
      else:
        break
    heap.pop()
    print()

  else: #insert
    heap.append(x)
    pos = len(heap)-1
    while(pos > 0)and(heap[pos]>heap[(pos-1)//2]):
      heap[pos], heap[(pos-1)//2] = heap[(pos-1)//2], heap[pos]
      pos = (pos-1)//2
