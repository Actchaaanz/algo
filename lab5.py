import sys
n = int(sys.stdin.readline())
if n <=0:
    sys.exit()
numc =[]
for i in range(n):
    num = int(sys.stdin.readline())
    numc.append(num)
maxnum = max(numc)
print(maxnum)