class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []
        start1 = intervals[0][0]
        end1 = intervals[0][1]
        for i in range(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if s <= end1:
                end1 = max(end1, e)
            else:
                res.append([start1, end1])
                start1 = s
                end1 = e
        res.append([start1, end1])
        
        return res