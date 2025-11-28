# https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/894/
# I understood later I could've used dfs over the grid directly

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        adj_list = dict()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                index = j+len(grid[i])*i
                if(grid[i][j] == "1"):
                    adj_list[index] = set()
                    if(i > 0):
                        if(grid[i-1][j] == "1"):
                            adj_list[index].add(j+(len(grid[i])*(i-1))) 
                    if(i < len(grid)-1):
                        if(grid[i+1][j] == "1"):
                            adj_list[index].add(j+(len(grid[i])*(i+1))) 
                    if(j > 0):
                        if(grid[i][j-1] == "1"):
                            adj_list[index].add((j-1)+len(grid[i])*i)
                    if(j < len(grid[i]) -1):
                        if(grid[i][j+1] == "1"):
                            adj_list[index].add((j+1)+len(grid[i])*i)
        
        visited = set()

        def dfs(index):
            for child in adj_list[index]:
                if(child not in visited):
                    visited.add(child)
                    dfs(child)
            
        
        groups = 0
        for node in adj_list:
            if(node not in visited):
                dfs(node)
                groups+=1
        
        return groups
            
        
        
        