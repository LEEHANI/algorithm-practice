import heapq

# heap=[]

# # heapq.heapify()

# # heapq.heappush(heap, (2, 2))
# # heapq.heappush(heap, (1, 4))
# # heapq.heappush(heap, (3, 2))
# # heapq.heappush(heap, (5, 6))

# heapq.heappush(heap, (-2, 2))
# heapq.heappush(heap, (-4, 1))
# heapq.heappush(heap, (-3, 7))
# heapq.heappush(heap, (-6, 5))
# heapq.heappush(heap, (-10, 3))

# print(heap)
# tmp=heapq.heappop(heap)
# print(tmp, heap)
    
class Solution:
    def rearrangeBarcodes(self, barcodes):
        arr=[0]*10001
        heap=[]
        answer=[0]*len(barcodes)

        # 숫자 개수 세기
        for barcode in barcodes:
            arr[barcode]+=1

        # 있으면 힙에 넣기
        for i in range(10001):
            if arr[i]:
                heapq.heappush(heap, (-arr[i], i))
        
        # 0번째 답 채우기
        key, value = heapq.heappop(heap)
        answer[0]=value
        heapq.heappush(heap, ((key+1), value))
        
        for i in range(1, len(barcodes)):
            # 힙 추출
            key, value = heapq.heappop(heap)
            
            # 추출한애가 i-1번째에 사용됐으면, 한번 더 pop
            if answer[i-1]==value:
                key2, value2 = heapq.heappop(heap)
                answer[i]=value2
                if key2+1<0: heapq.heappush(heap, ((key2+1), value2))
            else:
                answer[i]=value
                key+=1
            
            if key+1<0: heapq.heappush(heap, (key, value))
        return answer

if __name__=="__main__":
    sol1 = Solution()
    # print(sol1.rearrangeBarcodes([1,1,1,1,2,2,3,3])) 
    print(sol1.rearrangeBarcodes([2,2,2,1,5]))
        

