'''
    2405. Optimal Partition of String
    https://leetcode.com/problems/optimal-partition-of-string/
'''


class Solution(object):

    def partitionString(self, s):
        if not len(s):
            return 0

        char_dict, count = set(), 0

        for char in s:
            if char in char_dict:
                count += 1
                char_dict.clear()
            char_dict.add(char)

        return count + 1


def test_solution():
    data = "abacaba"
    res = Solution().partitionString(data)
    assert res == 4, 'Fail 1'
    print('1 test - Ok')

    data = "ssssss"
    res = Solution().partitionString(data)
    assert Solution().partitionString(data) == 6, 'Fail 2'
    print('2 test - Ok')

    data = ""
    res = Solution().partitionString(data)
    assert Solution().partitionString(data) == 0, 'Fail 3'
    print('3 test - Ok')

    data = "a"
    res = Solution().partitionString(data)
    assert Solution().partitionString(data) == 1, 'Fail 4'
    print('4 test - Ok')

    data = "aa"
    res = Solution().partitionString(data)
    assert Solution().partitionString(data) == 2, 'Fail 5'
    print('5 test - Ok')


    data = "ab"
    res = Solution().partitionString(data)
    assert Solution().partitionString(data) == 1, 'Fail 6'
    print('6 test - Ok')



test_solution()
