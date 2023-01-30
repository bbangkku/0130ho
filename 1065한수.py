from csv import list_dialects
from re import A
import sys
sys.stdin = open("./nn.txt")

def fn(n):
    count = 0
    for i in range(1, n+1):
        n_2 = list(map(int,str(i)))
        if len(n_2) == 1 or len(n_2) == 2:
            count = count + 1
        elif n_2[2] - n_2[1] == n_2[1] - n_2[0]:
            count = count +1

    return count

print(fn(int(input())))

