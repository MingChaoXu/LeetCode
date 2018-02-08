# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# solution 1
# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head == None:
#             return
#         dummy = ListNode(0)
#         dummy.next = head
#         n = 2
#         first = dummy
#         second = dummy
#         first_flag = True
#         while first != None:
#             while first != None and n > 0:
#                 first = first.next
#                 n -= 1
#             if n == 0 and first != None:
#                 n = 2
#                 second.next.next = first.next
#                 first.next = second.next
#                 second.next = first
#                 if first_flag:
#                     dummy = second
#                     first_flag = False
#                 first = first.next
#                 second = first
#         return dummy.next

# solution 2
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = ListNode(0), head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
        return head


if __name__ == '__main__':
    s = Solution()
    test = ListNode(1)
    test.next = ListNode(2)
    test.next.next = ListNode(3)
    ans = s.swapPairs(test)
    print(ans)
