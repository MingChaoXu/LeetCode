class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0: return 0

        sign = -1 if str[0] == '-' else 1

        ret = 0
        for i in range(len(str)):
            if str[i].isdigit():
                ret = ret * 10 + ord(str[i]) - ord('0')
            else:
                break
        ret *= sign
        return max(-2**31, min(sign * ret,2**31-1))