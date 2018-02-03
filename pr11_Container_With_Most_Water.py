class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        if right < 0:
            return 0
        max_contain = 0
        container_height = min(height[left], height[right])
        max_contain = max(((right - left) * container_height), max_contain)
        while right != left:
            if container_height == height[left]:
                left += 1
                container_height = min(height[left], height[right])
                max_contain = max(((right - left) * container_height), max_contain)
            else:
                right -= 1
                container_height = min(height[left], height[right])
                max_contain = max(((right - left) * container_height), max_contain)
        return max_contain