'''
    Leetcode 849. Maximize Distance to Closest Person
    https://leetcode.com/problems/maximize-distance-to-closest-person/description/
'''


class Solution(object):

    def maxDistToClosest(self, seats):
        i, j = 0, 1
        max_dist = 0

        while j < len(seats):
            while seats[j] == 0 and j != len(seats) - 1:
                j += 1

            if (seats[i] == 0 or seats[j] == 0) and max_dist < j - i:
                max_dist = j - i
            elif max_dist < (j - i) // 2:
                max_dist = (j - i) // 2

            i, j = j, j + 1

        return max_dist


s = Solution().maxDistToClosest([1,0,0])
print(s)
