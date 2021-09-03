a = [1, 2, 3, 4, 5, 6, 7]

b = [8, 9, 10]

count = 0
for i in range(len(a)):
    b.append(a[i])
    count += 1

b.sort()
del a[0:count]

print(a)
print(b)
