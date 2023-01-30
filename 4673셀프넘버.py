def self(n):
    n_1 = int(n)
    n_2 = list(map(int,str(n)))
    return sum(n_2, n_1)

a = [i for i in range(1,10001)]
for i in range(10001):
    if self(i) in a:
        a.remove(self(i))
for i in range(len(a)):
    print(a[i])

# num = 36
# num_2 = list(str(num))
# print(num_2)
