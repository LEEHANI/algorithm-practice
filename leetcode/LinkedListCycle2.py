# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
토끼와 거북이 알고리즘
'''
class Solution:
    def detectCycle(self, head):
        slow=head
        fast=head
        if head and head.next:
            fast=head.next
        else:
            return None

        while fast.next and fast.next.next:
            if slow==fast:
                break
            
            slow=slow.next
            fast=fast.next.next
            
        if slow!=fast:
            return None

        slow=head 
        fast=fast.next 
        idx=0
        while True:
            if slow==fast:
                return slow
            slow=slow.next
            fast=fast.next
            idx+=1
        