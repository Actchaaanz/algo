num = int(input())
numbers = []


for i in range(num):
    numc = int(input())
    numbers.append(numc)
avg = sum(map(float,numbers))/num
print(f"{avg:.2f}")