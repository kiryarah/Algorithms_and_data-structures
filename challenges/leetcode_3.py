'''
    3. Longest Substring Without Repeating Characters
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) < 2:
            return len(s)

        sub_seq, sub_len, left = set(), 0, 0

        for right in range(len(s)):
            while s[right] in sub_seq:
                sub_seq.remove(s[left])
                left += 1

            sub_seq.add(s[right])
            sub_len = max(sub_len, right - left + 1)
        return sub_len


def test_solution():
    data = Solution().lengthOfLongestSubstring("abcabcbb")
    assert data == 3, '1st - fail'
    print('1st - ok')

    data = Solution().lengthOfLongestSubstring("bbbbb")
    assert data == 1, '2st - fail'
    print('2st - ok')

    data = Solution().lengthOfLongestSubstring("pwwkew")
    assert data == 3, '3st - fail'
    print('3st - ok')


test_solution()
