# from csv import list_dialects
# from re import A
# import sys
# from collections import Counter
# sys.stdin = open("./nn.txt")

# m,n = map(int,input().split())
m=13
n=26
count = 0
for i in range(m, n+1) :

    if i == 1 :
        continue   
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0 :
            break
    else:
        print(i)
        # count = count +1
# print(count)

