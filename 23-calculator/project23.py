n = int(input())

if n == 1:
  print(0)
  print(1)
elif n == 2:
  print(1)
  print(1, 2)
elif n == 3:
  print(1)
  print(1, 3) 
else:
  opers = [-1]*(n+1)
  came_from = [-1]*(n+1)
  opers[0] = n+1
  opers[1] = 0
  opers[2] = 1
  opers[3] = 1
  came_from[0] = -1
  came_from[1] = -1
  came_from[2] = 1
  came_from[3] = 1

  for i in range(4, n+1):

    if i%3 == 0:
      s_1 = opers[i//3]
    else:
      s_1 = n+1

    if i%2 == 0:
      s_2 = opers[i//2]
    else:
      s_2 = n+1

    s_3 = opers[i-1]

    if s_1 < s_2 and s_1 < s_3:
      opers[i] = s_1 + 1
      came_from[i] = i//3
    elif s_2 < s_3:
      opers[i] = s_2 + 1
      came_from[i] = i//2  
    else:
      opers[i] = s_3 + 1
      came_from[i] = i-1

  print(opers[-1])

  opers = [n]
  while (opers[-1] != 1):
    i = came_from[i]
    opers.append(i)

  for i in opers[::-1]:
    print(i, end = " ")
