class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1] * (i+1) for i in range(numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                l[i][j] = l[i-1][j]+l[i-1][j-1]
        return l