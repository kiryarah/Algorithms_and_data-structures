'''
    1. Two Sum
    https://leetcode.com/problems/two-sum/
'''

class Solution(object):
    def twoSum(self, nums, target):
        seq = {}

        for index, num in enumerate(nums):
            if num in seq:
                return [seq.get(num), index]
            seq[target - num] = index


def test_solution():
    data = Solution().twoSum([2,7,11,15], 9)
    assert data == [0, 1], 'Fail'
    print('1st - ok')

    data = Solution().twoSum([3,2,4], 6)
    assert data == [1, 2], 'Fail'
    print('2nd - ok')

    data = Solution().twoSum([3,3], 6)
    assert data == [0, 1], 'Fail'
    print('3d - ok')


test_solution()
