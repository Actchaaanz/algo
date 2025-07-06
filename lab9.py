# รับขนาดเมทริกซ์
n = int(input())

# อ่านเมทริกซ์ A
A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# อ่านเมทริกซ์ B
B = []
for _ in range(n):
    row = list(map(int, input().split()))
    B.append(row)

# คำนวณผลคูณเมทริกซ์ C = A * B
C = []
for i in range(n):
    row = []
    for j in range(n):
        total = 0
        for k in range(n):
            total += A[i][k] * B[k][j]
        row.append(total)
    C.append(row)

# แสดงผลลัพธ์เมทริกซ์ C
for row in C:
    print(' '.join(map(str, row)))
