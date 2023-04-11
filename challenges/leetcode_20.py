'''
    leetcode 20. Valid Parentheses
    -
    https://leetcode.com/problems/valid-parentheses/
'''


class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        closed_brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if not (char in closed_brackets):
                stack.append(char)
            elif not stack or closed_brackets.get(char) != stack.pop():
                return False

        return not stack


def test_solution():
    data = Solution().isValid("()")
    assert data == True, 'Fail'
    print('Ok')

    data = Solution().isValid("()[]{}")
    assert data == True, 'Fail'
    print('Ok')

    data = Solution().isValid("(]")
    assert data == False, 'Fail'
    print('Ok')

    data = Solution().isValid("([{}]{}[])")
    assert data == True, 'Fail'
    print('Ok')

    data = Solution().isValid("(")
    assert data == False, 'Fail'
    print('Ok')

    data = Solution().isValid("]")
    assert data == False, 'Fail'
    print('Ok')


test_solution()
