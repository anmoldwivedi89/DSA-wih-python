class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current = 0
        for i in range(k):
            
            current += nums[i]
        max = current
        for i in range(1,len(nums)-k+1):
            current = current - nums[i-1]+ nums[i+k-1]
            if current>max:
                max = current
        return max/k
        