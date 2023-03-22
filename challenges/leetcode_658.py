'''
leetcode 658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/
'''


class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while right - left + 1 > k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1
        return [arr[i] for i in range(left, right + 1)]


s = Solution().findClosestElements([1,2,3,4,5], 4, 3)
print(s)
