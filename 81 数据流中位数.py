# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 11:15:34 2017

@author: Administrator
"""
import numpy as np
import heapq
class Solution:
    
    minHeap, maxHeap = [], []
    numbers = 0
    
    def my_medianII(self, nums):
        # write your code here
        if len(nums) == 0:
            return []
        heap = []
        heap.append(nums[0])
        ret = []
        ret.append(nums[0])
        for i in range(1, len(nums)):
            insert_i = nums[i]
            index_1 = 0
            index_2 = len(heap) - 1
            temp = heap[int((index_1 + index_2) / 2)]
            if insert_i >= heap[index_2]:
                heap.append(insert_i)
            elif insert_i <= heap[index_1]:
                heap.insert(0, insert_i)
            else:
                while insert_i != temp:
                    loc = int((index_1 + index_2) / 2)
                    if insert_i > temp and insert_i < heap[loc + 1]:
                        heap.insert(loc + 1, temp)
                    elif insert_i > temp:
                        index_1 = loc
                    else:
                        index_2 = loc
            ret.append(heap[int((len(heap)-1)/2)])
        return ret

    def medianII(self, nums):
        ans = []
        for item in nums:
            self.add(item)
            ans.append(self.getMedian())
        return ans
    
    def getMedian(self):
        return -self.maxHeap

if __name__ == "__main__":
    Sol = Solution()
    testcase1 = [3,2,4,4,4,4,5]
    ret1 = Sol.medianII(testcase1)
    print(ret1)