from csv import list_dialects
from re import A
from collections import Counter
sys.stdin = open("./nn.txt", mode='r')

import sys
from collections import deque
tc = int(sys.stdin.readline())
a = deque()
for i in range(1,tc+1):
    a.append(tc+1-i)
while len(a) >1:
    a.pop()
    b = a.pop()
    a.appendleft(b)
print(a[0])
 

#위에꺼 1 버리고 그위에꺼 제일 아래로 옮기고
#그다음 위 3 버리고 4를 밑으로 옮기고 24가 되면
#2를 버리면 4남음

# for j in range(tc):
#     data = deque(map(str,sys.stdin.readline().split()))

