class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.findNsum(sorted(nums), target, 4, [], results)
        return results
    def findNsum(self, nums, target, N, result, results):
        if len(nums)<N or N<2 or target<nums[0]*N or target>nums[-1]*N:
            return
        # solve 2-sum problem
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    print(results)
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(nums)-N+1):
                if i == 0 or (i>0 and nums[i] != nums[i-1]):
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return
