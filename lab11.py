import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
arr = list(map(int, data[1:n+1]))
k = int(data[-1])

try:
    print(arr.index(k))
except ValueError:
    print(-1)
