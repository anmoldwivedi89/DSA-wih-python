class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        arr = 0
        left = 0
   
        right = 0
        for i in range(len(nums)):
            arr += nums[i]
        for i in range(len(nums)):
            right = arr - left - nums[i]
            if left == right:
                return i
            left +=nums[i]
        return -1
        
        
           
      
    
            
         
           
        
            


        