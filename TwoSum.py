def twoSum(nums, target):
    map={}
    for i in range(len(nums)):
        n = target - nums[i]
        if n in map:
            return [map[n], i]

print(twoSum([2,7,11,15],9))
