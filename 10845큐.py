from csv import list_dialects
from re import A
import sys
from collections import Counter
sys.stdin = open("./nn.txt", mode='r')


import sys

tc = int(sys.stdin.readline())
li = []
for j in range(tc):
    data = list(map(str,sys.stdin.readline().split()))

    if data[0] == 'push':
        li.append(int(data[1]))
    
    elif data[0] == 'pop':
        if li: 
            print(li.pop(0))
        else:
            print(-1)

    elif data[0] == 'size':
        print(len(li))

    elif data[0] == 'empty':
        if len(li) == 0:
            print(1)
        else:
            print(0)

    elif data[0] == 'front':
        if len(li) == 0:
            print(-1)
        else:
            print(li[0])
    
    elif data[0] == 'back':
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])
    
    
    