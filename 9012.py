from csv import list_dialects
from re import A
import sys
from collections import Counter
from collections import deque
# from collections import deque

sys.stdin = open("./nn.txt", mode='r')

import sys


def test(n):
    if (n.count('(')) != (n.count(')')):
        a = 'NO'
        return a
    bb = []
    for j in range(len(n)):
        bb.append(n[j])
        if bb.count('(') >= bb.count(')'):
            a = 'YES'
        else:
            a = 'NO'
            return a
    return a

tc = int(sys.stdin.readline())

for i in range(tc):
    n = list(input())
    print(test(n))