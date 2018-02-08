# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# solution 1
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         dummy = ListNode(0)
#         dummy.next = head
#         length = 0
#         first = head
#         while first != None:
#             first = first.next
#             length += 1
#         length -= n
#         first = dummy
#         while length > 0:
#             first = first.next
#             length -= 1
#         first.next = first.next.next
#         return dummy.next

# solution 2
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        second = dummy
        while first != None:
            first = first.next
            length += 1
            if length > n:
                second = second.next
        second.next = second.next.next
        return dummy.next
