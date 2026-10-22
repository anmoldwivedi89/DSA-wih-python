class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hmap={}
        s = s.split()
        seen= set()
        if len(pattern)!=len(s):
            return False
        for pat,word in zip(pattern,s):

            if pat in hmap:
                if hmap[pat]!=word:
                    return False
            else:
                if word in seen:
                    return False
                hmap[pat]=word
                seen.add(word)
        return True
            
            

        