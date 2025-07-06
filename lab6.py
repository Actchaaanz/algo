n = int(input())
box = []
for i in range(n):
    num = int(input())
    box.append(num)

evennum = [i for i in box if i % 2 == 0]

total = sum(evennum)
print(total)
    

        