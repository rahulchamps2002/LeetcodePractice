def twoSum(nums, target):
    map={}
    for i, v in enumerate(nums):
        diff = target - v
        if diff in map:
            return [map[diff], i]
        map[v] = i

print(twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],9))

def twosum2(nums, target):
    map={}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in map:
            return [map[diff], i]
        map[nums[i]] = i

print(twosum2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],9))