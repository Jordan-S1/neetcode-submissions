class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        re = set()
        l = 0
        for r in range(len(s)):
            while s[r] in re:
                re.remove(s[l])
                l += 1    
            re.add(s[r])
            res = max(res, r - l + 1)
        return res