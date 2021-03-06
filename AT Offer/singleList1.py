# coding:utf-8

# 从尾到头打印链表

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        newlist = []
        while listNode:
            newlist.append(listNode.val)
            listNode = listNode.next
        return newlist[::-1]