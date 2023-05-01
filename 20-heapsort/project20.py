def extract(heap):
  ans = heap[0]
  heap[0] = heap[-1]
  pos = 0
  while 2*pos+2 < len(heap):
    max_kid = 2*pos+1
    if heap[max_kid] > heap[max_kid+1]:
      max_kid += 1
    if heap[pos] > heap[max_kid]:
      heap[pos], heap[max_kid] = heap[max_kid], heap[pos]
      pos = max_kid
    else:
      break
  heap.pop(-1)
  return ans

def insert(heap, x):
  heap.append(x)
  pos = len(heap)-1
  while(pos > 0)and(heap[pos]<heap[(pos-1)//2]):
    heap[pos], heap[(pos-1)//2] = heap[(pos-1)//2], heap[pos]
    pos = (pos-1)//2

n = int(input())
inp = list(map(int, input().split()))

heap = []

for i in inp:
  insert(heap,i)
 
for i in range(n):
  print(extract(heap), end=" ")
