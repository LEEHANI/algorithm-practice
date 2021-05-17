# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        if head == None:
            return None
        
        node = head
        remainMaxThanX = []
        remainMinThanX = []

        while node:
            if node.val == x:
                remainMaxThanX.append(x)
            elif node.val < x:
                remainMinThanX.append(node.val)
            elif node.val > x:
                remainMaxThanX.append(node.val)
            node=node.next

        remainMinThanX.extend(remainMaxThanX)
        
        node2 = ListNode(0)
        answer=node2
        while remainMinThanX:
            node2.val=remainMinThanX.pop(0)
            
            if len(remainMinThanX)>0:
                node2.next = ListNode(0)
                node2=node2.next
        
        return answer
