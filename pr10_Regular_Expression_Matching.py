class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        else:
            for i in range(len(p)):
                if i+1 < len(p) and p[i+1] == '*':

                if s[i] != p[i]:

