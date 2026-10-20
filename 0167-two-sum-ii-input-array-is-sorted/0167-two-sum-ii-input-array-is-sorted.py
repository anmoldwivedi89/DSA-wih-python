class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1
        for i in numbers:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left+1,right+1]
            elif current>target:
                right-=1
            else:
                left+=1
            


        