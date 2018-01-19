n = int(input().strip())
nums = input().strip().split(' ')
nums = [int(_) for _ in nums ]

for i in range(1, len(nums)):
    j = i - 1
    x = nums[i]
    while j >= 0 and nums[j] > x:
        nums[j+1] = nums[j]
        j -= 1

    nums[j+1] = x
    print(' '.join(str(p) for p in nums))
