class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    while l+1 < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r-1 and nums[r] == nums[r-1]:
                        r -= 1
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        return ans