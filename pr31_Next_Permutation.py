class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(len(nums))):
            if i + 1 < len(nums) and nums[i] > nums[i + 1]:
                for j in reversed(range(len(nums))):
                    if nums[j] > nums[i+1]:
                        tmp = nums[i+1]
                        nums[i+1], nums[j] = nums[j], tmp
                        reversed(nums[i:])
                break
            if i == len(nums)-2 and nums[i] < nums[i + 1]:
                reversed(nums)
