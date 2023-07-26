# given a list of circles (with x,y center coordinates and radius)
# return if all of them are in a single circle group (that is, they are touching or overlapping)

import math

circles = [([1,2], 1),([3,3], 2),([4,4],1),([5,6], 2)]
visited = []

def is_circle_group():
    circle_graph = [[False for col in range(len(circles))] for row in range(len(circles))]
    
    def dfs(node):
        visited.append(node)
        for i in range(len(circle_graph)):
            if i not in visited:
                if circle_graph[node][i]:
                    dfs(i)
    
    for i in range(len(circles)): 
        for j in range(i+1,len(circles)):
            if is_touching(circles[i], circles[j]):
                circle_graph[i][j] = True
                circle_graph[j][i] = True
    
    dfs(0)
    
    if len(visited) == len(circles):
        print("is a group")
    else:
        print("not a group")

def is_touching(circle1, circle2):
    if math.dist(circle1[0], circle2[0]) <= circle1[1] + circle2[1]:
        return True
    return False

is_circle_group()