class Solution:
    def maximumSum(self,a):
        noDel = a[0]
        oneDel = float('-inf')
        res = a[0]

        for i in range(1, len(a)):
            prevNoDel = noDel

            noDel = max(a[i], noDel + a[i])

            oneDel = max(prevNoDel, oneDel + a[i])

            res = max(res, noDel, oneDel)

        return res
