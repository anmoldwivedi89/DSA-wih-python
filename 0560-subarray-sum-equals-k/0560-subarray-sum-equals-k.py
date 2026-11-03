class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum =0
        dict ={0:1}
        for num in nums:
            prefix_sum +=num
            count += dict.get(prefix_sum-k,0)
            dict[prefix_sum] = dict.get(prefix_sum,0)+1
        return count

        
        
            
             
            
            
        
                
        
            
        

        


            
            

        