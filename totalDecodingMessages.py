
class Solution:
    def CountWays(self, s):
        # Code here
        if s[0] == "0":
            return 0
        
        prev0 = 1
        prev1 = 1
        
        
        for i in range(2,len(s)+1):
            curr = 0
            if s[i-1] != "0":
                curr += prev1
            if s[i-2] == "1" or s[i-2] == "2" and s[i-1] <="6":
                curr += prev0
            
            prev0,prev1 = prev1,curr
         
        return prev1 % (10**9 + 7)
