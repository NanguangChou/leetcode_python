# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 22:00:10 2017

@author: Administrator
"""

"""
给出一个整数数组，堆化操作就是把它变成一个最小堆数组。

对于堆数组A，A[0]是堆的根，并对于每个A[i]，A [i * 2 + 1]
是A[i]的左儿子并且A[i * 2 + 2]是A[i]的右儿子。

什么是堆？

堆是一种数据结构，它通常有三种方法：push， pop 和 top。其中，“push”添加新的元素进入堆，“pop”删除堆中最小/最大元素，“top”返回堆中最小/最大元素。
什么是堆化？

把一个无序整数数组变成一个堆数组。如果是最小堆，每个元素A[i]，我们将得到A[i * 2 + 1] >= A[i]和A[i * 2 + 2] >= A[i]
如果有很多种堆化的结果？

返回其中任何一个。
"""


import heapq

class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        return heapq.heapify(A)
        
        