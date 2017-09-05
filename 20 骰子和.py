# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:05:39 2017

@author: Administrator
"""

class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        results = []
        f = [[0 for j in range(6 * n + 1)] for i in range(n + 1)]
        
        for i in range(1, 7):
            f[1][i] = 1.0 / 6.0
        for i in range(2, n + 1):
            for j in range(i, 6 * n + 1):
                for k in range(1, 7):
                    if j > k:
                        f[i][j] += f[i - 1][j - k]
                f[i][j] /= 6.0

        for i in range(n, 6 * n + 1):
            results.append((i, f[n][i]))

        return results
    
if __name__ == "__main__":
    sol = Solution()
    a=-2;b=6
    A=[[3,-2,-1],[a,2,-2],[3,b,-1]]
    b= np.linalg.eig(A)
    print(np.linalg.eig(A))
    B=[[9,1,9,9,9],[9,0,9,9,2],[4,0,0,5,0],[9,0,3,9,0],[6,0,0,7,0]]
    B=np.matrix(B)-1
    print(np.linalg.det(B))
#==============================================================================