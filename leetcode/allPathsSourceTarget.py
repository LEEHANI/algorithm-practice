class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.answer=[]
        self.dfs(graph, 0, '0')
        
        return self.answer

    def dfs(self, graph, select, totalString):
        if select==len(graph)-1:
            self.answer.append(totalString.split(','))
            return 
        
        if graph[select]:
            for i in graph[select]:
                self.dfs(graph, i, totalString + ',' + str(i))
