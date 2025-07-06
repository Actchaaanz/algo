n = int(input())
nums = []               
for i in range(n):
    num = int(input())
    nums.append(num)     

sorted_nums = sorted(nums)
print(' '.join(map(str,sorted_nums)))
