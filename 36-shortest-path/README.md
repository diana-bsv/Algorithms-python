# 36. Длина кратчайшего пути
(задача из тренировок по алгоритмам 3.0 от Яндекса)

В неориентированном графе требуется найти длину минимального пути между двумя вершинами.

Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100). Затем записана матрица смежности (0 обозначает отсутствие ребра, 1 – наличие ребра). Далее задаются номера двух вершин – начальной и конечной.

Выведите L – длину кратчайшего пути (количество ребер, которые нужно пройти).
Если пути нет, нужно вывести -1.
## Пример 1

### Ввод
10  
0 1 0 0 0 0 0 0 0 0  
1 0 0 1 1 0 1 0 0 0  
0 0 0 0 1 0 0 0 1 0  
0 1 0 0 0 0 1 0 0 0  
0 1 1 0 0 0 0 0 0 1  
0 0 0 0 0 0 1 0 0 1  
0 1 0 1 0 1 0 0 0 0  
0 0 0 0 0 0 0 0 1 0  
0 0 1 0 0 0 0 1 0 0  
0 0 0 0 1 1 0 0 0 0  
5 4  
### Вывод
2
## Пример 2

### Ввод
5  
0 1 0 0 1  
1 0 1 0 0  
0 1 0 0 0  
0 0 0 0 0  
1 0 0 0 0  
3 5
### Вывод
3
