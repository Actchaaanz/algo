n = int(input())
box = []
for i in range(n):
    num = int(input())
    box.append(num)

posi = [i for i in box if i > 0]
if posi :
    avg = sum(posi) / len(posi)
    print(f'{avg:.2f}')
else:
    print("0.00")