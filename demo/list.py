#!/usr/bin/python3
# coding: utf-8
vec = [2,4,6]
print([x*x for x in vec])
print([x*x for x in vec if x > 3])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

vec1 = [1,2,3,4]
vec2 = [5,6,7,8]
# vec2 = [5,6,7]
print([x+y for x in vec1 for y in vec2])
print([vec1[i]+vec2[i] for i in range(len(vec1))])

print([str(round(355/113, i)) for i in range(1, 6)])


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)