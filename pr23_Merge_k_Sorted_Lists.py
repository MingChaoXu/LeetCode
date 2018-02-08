# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# solution 1: time limit
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         min_id, del_id = 0, 0
#         first = ListNode(0)
#         res = first
#         del_flag = False
#         while lists:
#             # 初始化tmpmin
#             for i in range(len(lists)):
#                 if lists[i]:
#                     first.next = lists[i]
#                     break
#             for i in range(len(lists)):
#                 if lists[i]:
#                     if lists[i].val < first.next.val:
#                         first.next = lists[i]
#                 else:
#                     del_flag = True
#                     del_id = i
#             if first.next:
#                 first = first.next
#             if del_flag:
#                 del lists[del_id]
#                 # print(len(lists))
#                 del_flag = False
#         return res.next

# solution2 优先队列，利用堆排序
from queue import PriorityQueue


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
