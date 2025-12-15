# https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2986/

from pyparsing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        trees = {}
        visited = set()

        def find_trees(x, y):
            if x > (len(forest)-1) or x < 0 or y > (len(forest[0])-1) or y < 0:
                return
            node = forest[x][y]
            if(node == 0 or node in visited):
                return
            visited.add(node)
            if(node != 1):
                trees[node] = (x,y)

            find_trees(x+1,y)
            find_trees(x-1,y)
            find_trees(x,y+1)
            find_trees(x,y-1)

        find_trees(0,0)
        for row in forest:
            for node in row:
                if node != 0 and node not in visited:
                    return -1 # there are paths you cant reach
        sorted_keys = sorted(trees)
        


        def find_path(x,y,index, path):
            node = forest[x][y]
            if x > (len(forest)-1) or x < 0 or y > (len(forest[0])-1) or y < 0 or node == 0:
                return
            
            if(index == len(sorted_keys)):
                return path

            destination = trees[sorted_keys[index]]
            if(x == destination[0] and y == destination[1]):
                return find_path(x,y,index+1, path)

            hor = x - destination[0]
            ver = y - destination[1]

            if hor < 0:
                return find_path(x+1, y, index, path+1)
            elif hor > 0:
                return find_path(x-1, y, index, path+1)
                
            if ver < 0:
                return find_path(x, y+1, index, path+1)
            elif ver > 0:
                return find_path(x, y-1, index, path+1)

        return find_path(0,0,1,0)
    
# I tried a greedy approach but it failed on some test cases
# I didn't know what the algorithm was of finding the shortest path in a grid with obstacles
# Gemini told me about BFS and I'll implement below soon