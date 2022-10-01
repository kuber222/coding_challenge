
# class Solution:
#     def solveWordWrap(self, nums, k):
#         #Code here

INV = 10**9
class Solution:
    def solveWordWrap(self, A, k):
        def _solve(R):
            if dp[R] != -1: return dp[R]
            L = 0
            ans = INV
            for i in reversed(range(R+1)):
                L+=A[i]
                if L <= k: ans = min( ans, (k-L)**2 + _solve(i-1) )
                else: break
                L += 1
            dp[R] = ans
            return ans
        
        N = len(A)
        ans = INV
        L = 0
        dp = [-1] * N + [0]
        for i in reversed(range(N)):
            L += A[i]
            if L <= k: ans = min(ans, _solve(i-1))
            else: break
            L += 1
        return ans
