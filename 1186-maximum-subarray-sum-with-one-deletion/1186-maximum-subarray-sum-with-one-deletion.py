class Solution:
    def maximumSum(self,a):
        noDel = a[0]
        oneDel = float('-inf')
        res = a[0]

        for i in range(1, len(a)):


            oneDel = max(noDel, oneDel + a[i])
            noDel = max(a[i], noDel + a[i])

            res = max(res, noDel, oneDel)

        return res
