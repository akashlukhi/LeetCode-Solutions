class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 0
        while i < len(intervals)-1:
            if intervals[i][0] == intervals[i+1][0]:
                maxi = max(intervals[i][1], intervals[i+1][1])
                intervals[i][1] = maxi
                intervals.pop(i+1)
                i -= 1
            else:
                if intervals[i+1][0] <= intervals[i][1]:
                    maxi = max(intervals[i][1], intervals[i+1][1])
                    intervals[i][1] = maxi
                    intervals.pop(i+1)
                    i -= 1
            i += 1
        return intervals