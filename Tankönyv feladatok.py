from collections import defaultdict

a = []
file = open(r"C:\Users\Bori\Desktop\test.txt")
for elem in file:
    line = elem.strip().split('|')
    a.append(line)
print(a)



