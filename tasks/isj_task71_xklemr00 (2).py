#!/usr/bin/env python3

# minitask 7.1
# f is a general iterator, for example a file
f = open('students.txt')
it = f.readlines()
header = it[0]
for line in it[1:]:
    line = line.rstrip
    print(line)
