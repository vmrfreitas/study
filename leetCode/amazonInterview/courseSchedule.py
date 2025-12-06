# https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2983/

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if(not prerequisites):
            return True
        
        visited = set()
        path = set()
        graph = defaultdict(set)
        
        for course, prereq in prerequisites:
            if (course == prereq):
                return False
            graph[course].add(prereq)

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            visited.add(node)

            for child in graph[node]:
                if not dfs(child):
                    return False
                
            path.remove(node)
            return True
            
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False
        
        return True
    
    
    
# this one I had to ask copilot for help again, finding cycles in a directed graph apparently
# requires an extra set to track the current path in the DFS
