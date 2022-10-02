#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (70.77%)
# Likes:    14157
# Dislikes: 532
# Total Accepted:    1.1M
# Total Submissions: 1.6M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid_paren(parens):
            if parens[0] == ')':
                return false
            
            stack = []
            for paren in parens:
                if paren == '(':
                    stack.append(paren)
                else:
                    if stack[-1] == '(':
                        stack.pop()
            
            return len(stack) == 0

        s = [' '] * (2 * n)
        output = []
        def generate_paren(i):
            if i == len(s):
                if valid_paren(s):
                    output.append(''.join(s))
            else:
                s[i] = '('
                generate_paren(i+1)

                s[i] = ')'
                generate_paren(i+1)
        
        generate_paren(i)


    # Neetcode
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paren, if open count < N
        # only add closed paren, if close count < open
        # valid iff opn count == closed count == n

        stack = []
        res = []
        def backtrack(open_count, closed_count):
            if open_count == closed_count == n:
                res.append("".join(stack))
            else:
                if open_count < n:
                    stack.append('(')
                    backtrack(open_count + 1, closed_count)
                    stack.pop()
                if closed_count < open_count:
                    stack.append(')')
                    backtrack(open_count, closed_count + 1)
                    stack.pop()
        
        backtrack(0, 0)
        return res


        
# @lc code=end

