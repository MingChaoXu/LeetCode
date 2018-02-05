class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        print(s)
        start, end = int(0), int(0)
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            length = max(len1, len2)
            print(length)
            #print('len1:{0},len2:{1},length:{2}'.format(len1, len2, length))
            if length > end - start:
                start = i - (length-1)//2
                end = i + length//2 +1
        print('start:{0},end:{1}'.format(start, end))
        return s[start:end]

    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while L>=0 and R<len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1