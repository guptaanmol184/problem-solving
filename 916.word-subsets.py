#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#
# https://leetcode.com/problems/word-subsets/description/
#
# algorithms
# Medium (52.38%)
# Likes:    1081
# Dislikes: 138
# Total Accepted:    55K
# Total Submissions: 104.4K
# Testcase Example:  '["amazon","apple","facebook","google","leetcode"]\n["e","o"]'
#
# You are given two string arrays words1 and words2.
# 
# A string b is a subset of string a if every letter in b occurs in a including
# multiplicity.
# 
# 
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# 
# 
# A string a from words1 is universal if for every string b in words2, b is a
# subset of a.
# 
# Return an array of all the universal strings in words1. You may return the
# answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 =
# ["e","o"]
# Output: ["facebook","google","leetcode"]
# 
# 
# Example 2:
# 
# 
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 =
# ["l","e"]
# Output: ["apple","google","leetcode"]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words1.length, words2.length <= 10^4
# 1 <= words1[i].length, words2[i].length <= 10
# words1[i] and words2[i] consist only of lowercase English letters.
# All the strings of words1 are unique.
# 
# 
#

# @lc code=start
class Solution:

    # Brute Force
    # Get's TLE
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        out = []
        cache = {}
        for a in words1:
            is_universal_str = True
            a_ctr = Counter()
            for l in a:
                a_ctr[l] += 1
            for i, b in enumerate(words2):
                if b not in cache:
                    b_ctr = Counter()
                    for l in b:
                        b_ctr[l] += 1
                    cache[b] = b_ctr
                b_ctr = cache[b]
                for l in b_ctr.keys():
                    if l not in a_ctr or not a_ctr[l] >= b_ctr[l]:
                        is_universal_str = False
                        break
                if not is_universal_str:
                    break
            if is_universal_str:
                out.append(a)
        
        return out

    # Optimized
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        tempDict = Counter()
        for w in words2:
            tempDict |= Counter(w)
        
        result = []
        for w in words1:
            if not tempDict - Counter(w):
                result.append(w)
        
        return result




        
# @lc code=end

