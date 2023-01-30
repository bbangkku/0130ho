from csv import list_dialects
from re import A
import sys
from collections import Counter
sys.stdin = open("./nn.txt")

# li = []

# def bk(m , n):
#     count = 0
#     for i in range(m, n+1) :
#         if i == 1:
#             continue
#         if i>2 and i % 2 == 0:
#             continue    
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0 :
#                 break
#         else:
#             count = count + 1
#     return count

# def aera(m, n):
#     li=[]
#     for i in range(m, n+1) :
#         if i == 1:
#             continue
#         if i>2 and i % 2 == 0:
#             continue    
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0 :
#                 break
  

# while True:
#     a = int(input())
#     if a == 0: 
#         break
#     else:
#         print(bk(a+1, 2*a))
n = 246912
li = [False, False] + [True] * (n-1)
prime = []
for i in range(2, n+1):
    if li[i]:
        prime.append(i)
        for j in range(2*i, n+1, i):
            li[j] = False
while True:
    a = int(input())
    if a == 0: 
        break
    print(sum(li[a+1 : 2*a+1])) 