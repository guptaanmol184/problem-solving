# Does not work, gives TLE

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        ans = [0]
        def dfs(i, s, mask):
            if i == len(s):
                p = [c for c, m in zip(s, mask) if m == 1]

                valid = True
                for i in range(1, len(p)):
                    if abs(ord(p[i-1]) - ord(p[i])) > k:
                        valid = False
                        break

                if valid:
                    if len(p) > ans[0]:
                        ans[0] = len(p)
            else:
                mask[i] = 1
                dfs(i+1, s, mask)
                mask[i] = 0
                dfs(i+1, s, mask)
            
        mask = [0] * len(s)
        dfs(0, s, mask)
    
        return ans[0]

s = Solution()
out = s.longestIdealString("acfgbd", 2) 
print(out)