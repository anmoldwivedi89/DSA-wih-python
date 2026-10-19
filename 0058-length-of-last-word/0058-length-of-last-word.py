class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
                 # Step 1
        word = s.split()       # Step 2 (list ban gayi)
        
        print(word)           
        
        return len(word[-1])  