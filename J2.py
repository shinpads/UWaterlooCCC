nums = []
magic = "magic"
for x in range(4):
    n=input().split()
    n=[int(c) for c in n]
    nums.append(n)

base = sum(nums[0][0:])
for x in range(3):
    if sum(nums[x+1][0:]) != base or sum(nums[0:][x]) != base:
        magic = "not magic"
        break
print(magic)










