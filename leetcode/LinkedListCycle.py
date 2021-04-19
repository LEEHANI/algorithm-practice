# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
토끼와 거북이 알고리즘 (순환구조가 있는지 확인 가능)
- 토끼: 2칸씩 이동, 거북이: 1칸씩 이동 
- 순환구조가 있다면 둘은 언젠가 만나게 되어있음. 만나지 않는다면 순환구조가 없는것
- 순환구조 처음 위치를 알고 싶다면 토끼와 거북이가 만난자리에서 거북이를 처음으로 옮긴뒤 토끼와 거북이 모두 한칸씩 이동하다보면 만나는 지점이 순환구조의 처음위치

ex) 3->2->0->4->2->0->4   (2-0-4 싸이클)
거북이: 3->2->0->4->2->0->4 ...
토끼 : 2->4->0->2->4 ...
거북이와 토끼가 0일때 최초 만남. 

순환구조 처음 위치를 알기위해 위치 변경(거북이->맨처음, 토끼->한칸 앞으로)
거북이: 3->2->0->4
토끼:  4->2->0->...
거북이와 토끼가 2일때 만남. 이 지점이 순환구조 처음 위치임
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node = head
        idx=0
        
        while node:
            if idx>100000:
                return True
            idx+=1
            node=node.next    
        
        return False

    def hasCycle(self, head: ListNode) -> bool:
        node = head
        idx=0
        
        while node:
            if idx>100000:
                return True
            idx+=1
            node=node.next    
        
        return False