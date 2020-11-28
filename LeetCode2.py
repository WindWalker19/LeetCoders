# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode,carry=0) -> ListNode:
        val = l1.val + l2.val + carry
        carry = val//10 # Truncates the fraction part.
        # create a LL
        ret = ListNode(val%10)
        # print(ret)
        if(l1.next != None or l2.next!= None or carry!=0):
            #if the l1.next value is None.
            if(l1.next == None):
                #Set the l1.next value as 0
                l1.next = ListNode(0)
            if(l2.next == None):
                #Set the l2.next value as 0
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,carry)
        return ret

