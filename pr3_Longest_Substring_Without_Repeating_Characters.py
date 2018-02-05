class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        last = {}
        left, ans = 0, 0
        for i in range(len(s)):
            if s[i] in last and last[s[i]] >= left:
                left = last[s[i]] + 1
            ans = max(ans, i-left+1)
            last[s[i]] = i
        return ans