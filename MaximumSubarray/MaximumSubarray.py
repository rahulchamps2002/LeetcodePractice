def maxSubArray(nums):
    res = nums[0]
    sum = 0
    for i in nums:
        if sum < 0:
            sum = 0
        sum += i
        res = max(sum, res)
    return res


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))