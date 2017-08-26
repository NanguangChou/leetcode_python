# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 18:59:02 2017

@author: Administrator
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

from heapq import heappop, heappush
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None
        trav = dummy = ListNode(-1)
        heap = []
        for ll in lists:
            if ll:
                self.heappushNode(heap, ll)
        
        while heap:
            node = heappop(heap)[1]
            trav.next = node
            trav = trav.next
            if trav.next:
                self.heappushNode(heap, trav.next)
        return dummy.next
    
    def heappushNode(self, heap, node):
        heappush(heap, (node.val, node))
        
    def my_mergeKLists(self, lists):
        # write your code here
        len_list = len(lists)
        if len_list == 0:
            return None
        ret = lists[0]
        for i in range(1, len_list):
            if ret is None:
                ret = lists[i]
            elif lists[i] is None:
                continue
            else:
                ret = self.mergeTwolist(ret, lists[i])
        return ret

    def mergeTwolist(self, first, second):
        ret = ListNode(None)
        head = ret
        while first and second:
            if first.val <= second.val:
                ret.val = first.val
                ret.next = ListNode(None)
                ret = ret.next
                first = first.next
                if first is None:
                    while second:
                        ret.val = second.val
                        second = second.next
                        if second:
                            ret.next = ListNode(None)
                            ret = ret.next
                    break
            else:
                ret.val = second.val
                ret.next = ListNode(None)
                second = second.next
                ret = ret.next
                if second is None:
                    while first:
                        ret.val = first.val
                        first = first.next
                        if first:
                            ret.next = ListNode(None)
                            ret = ret.next
                    break
        return head