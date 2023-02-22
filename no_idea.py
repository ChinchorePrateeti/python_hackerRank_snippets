iH = 0
a,b = input().split(" ")
n = int(a)
m = int(b)

arry = input().split()

A = input().split()
B = input().split()

for index in range(n):
    if arry[index] in A:
        iH += 1
    if arry[index] in B:
        iH -= 1
print(iH)

########################

happiness = 0
n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

for i in arr:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1
print(happiness)
