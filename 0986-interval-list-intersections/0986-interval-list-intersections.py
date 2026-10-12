class Solution:
    def intervalIntersection(
        self, firstList: list[list[int]], secondList: list[list[int]]
    ) -> list[list[int]]:
        res = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            s1 = firstList[i][0]
            e1 = firstList[i][1]
            s2 = secondList[j][0]
            e2 = secondList[j][1]
            if s1 <= s2:
                if e1 >= s2:
                    res.append([max(s1, s2), min(e1, e2)])
            else:
                if e2 >= s1:
                    res.append([max(s1, s2), min(e1, e2)])
            if e1 < e2:
                i += 1
            else:
                j += 1
        print(res)
        return res
