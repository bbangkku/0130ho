from csv import list_dialects
from re import A
import sys
from collections import Counter
sys.stdin = open("./nn.txt")


from collections import deque
m,n = map(int,input().split())
q = deque()
li = []
for i in range(1, m+1):
    q.append(str(m+1 - i))

while len(q) > 0:
    q.rotate(n-1)
    a = (q.pop())
    li.append(a)

result = ", ".join((li))
print("<{}>".format(result))


  

# print(n)
