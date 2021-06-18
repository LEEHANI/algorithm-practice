'''
아이디어보다 구현이 어려운 문제 ..
'''
class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        answer=0
        #s1 > s2 always
        if sum(nums1)<sum(nums2):
            nums1, nums2=nums2, nums1
        
        # nums counting arr
        n1=[0]*7
        n2=[0]*7
        s1=sum(nums1)
        s2=sum(nums2)
        
        p1=6
        p2=1
        
        for n in nums1:
            n1[n]+=1
        for n in nums2:
            n2[n]+=1
        
        while s1!=s2:
            # edge case
            if n1[1]*1==s1 and n2[6]*6==s2:
                return -1
            
            if p1<=0 or p2>=7:
                return -1

            if n1[p1]==0:
                p1-=1
                continue
            if n2[p2]==0:
                p2+=1
                continue

            if s1-s2>=5:
                if p1>=7-p2:
                    n1[p1]-=1
                    n1[1]+=1

                    s1=s1-p1+1
                else:
                    n2[p2]-=1
                    n2[6]+=1

                    s2=s2+6-p2

            else:
                target=s1-s2

                if p1>=7-p2:
                    if p1-1>=target:
                        return answer+1
                    
                    n1[p1]-=1
                    n1[1]+=1
                    s1=s1-p1+1

                else:
                    if 7-p2-1>=target:
                        return answer+1
                    
                    n2[p2]-=1
                    n2[6]+=1
                    s2=s2-p2+6
                    
            # print(n1[1:], s1, n2[1:], s2)
            answer+=1
                    
            
            
            
        return answer