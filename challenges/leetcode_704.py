'''
    704. Binary Search
    https://leetcode.com/problems/binary-search/description/
'''


class Solution(object):
    def search(self, nums, target):
        mid = len(nums) // 2
        left, right = 0, len(nums) - 1

        while left <= right:
            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2

        return -1


def test_search():
    data = Solution().search([-1,0,3,5,9,12], target=9)
    assert data == 4, '1st - fail'
    print('1st - ok')

    data = Solution().search([-1,0,3,5,9,12], target=2)
    assert data == -1, '2st - fail'
    print('2st - ok')

test_search()
