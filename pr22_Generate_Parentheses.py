class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n <= 0: return res
        self.generateAll(res, '', n, n)
        return res

    def generateAll(self, res, s, l, r):
        # print(res)
        if l == 0 and r == 0:
            res.append(s)
            return
        if l > 0:
            # print('pre:', s)
            self.generateAll(res, s + '(', l - 1, r)
        if r > 0 and l < r:
            # print('beh:', s)
            self.generateAll(res, s + ')', l, r - 1)


if __name__ == '__main__':
    s = Solution()
    ans = s.generateParenthesis(3)
    print(ans)
