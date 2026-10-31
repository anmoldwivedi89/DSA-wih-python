class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        arr = []
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums

        
        