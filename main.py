nums = [1, 3, 5, 6]
target = 2

i = 0
while i < len(nums) and nums[i] < target:
    i += 1

print("Index:", i)