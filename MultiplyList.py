import sys

for line in sys.stdin:
    list1, list2 = line.strip().split('|')
    result = [int(x) * int(y) for x, y in zip(list1.split(), list2.split())]
    print(*result)
