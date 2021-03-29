class Solution:
    # [[1,3],[3,0,1],[2],[0]]
    def canVisitAllRooms(self, rooms):
        visit = [False]*len(rooms)

        self.visitRooms(0, visit, rooms)

        print(False in visit)
            # return False
        # return True
    
    def visitRooms(self, i, visit, rooms):
        if visit[i]:
            return 

        visit[i] = True

        for v in rooms[i]:
            self.visitRooms(v, visit, rooms)

    

if __name__=="__main__":
    sol1 = Solution()
    # print(sol1.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])) 
    print(sol1.canVisitAllRooms([[1],[2],[3],[]])) 



