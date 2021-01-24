class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []
        n = len(intervals)
        i = 0
        while (i < n):
            left = intervals[i][0]
            right = intervals[i][1]
            while (i < n - 1 and intervals[i + 1][0] <= right):
                i += 1
                right = max(intervals[i][1], right)
            result.append([left, right])
            i += 1
        return result
