# implementing dijkstra using the explanation from this video https://www.youtube.com/watch?v=pVfj6mxhdMw&t=222s
#
#
#  A --6-- B --5-- C
#  |      /|       |
#  1    2  2       5
#  |  /    |       |
#  D --1-- E-------


from math import inf

# representation of the graph drawn above as a adjacency matrix
# A is 0, B is 1, C is 2, D is 3, E is 4
graph = [[0,6,0,1,0],[6,0,5,2,2],[0,5,0,0,5],[1,2,0,0,1],[0,2,5,1,0]] 

shortest_distance_from_A = [0, inf, inf, inf, inf]
previous_vertexes = [-1,-1,-1,-1,-1]
start_vertex = 0 # we are starting in the A vertex for this example
visited = set()
unvisited = [0,1,2,3,4] # add all nodes to the unvisited list

while(len(visited)!=len(graph)):
    visiting_vertex = -1
    shortest_dist = inf
    for i in range(len(unvisited)):
        if shortest_distance_from_A[unvisited[i]] < shortest_dist:
            shortest_dist = shortest_distance_from_A[unvisited[i]]
            visiting_vertex = unvisited[i]
            visiting_vertex_index = i
            
    unvisited.pop(visiting_vertex_index)

    visiting_neighbours = graph[visiting_vertex]
    for i in range(0,len(visiting_neighbours)):
        if(visiting_neighbours[i]!=0):
            if i not in visited:
                distance_form_A_to_neighbour = shortest_distance_from_A[visiting_vertex] + visiting_neighbours[i]
                if distance_form_A_to_neighbour < shortest_distance_from_A[i]:
                    shortest_distance_from_A[i] = distance_form_A_to_neighbour
                    previous_vertexes[i] = visiting_vertex

    visited.add(visiting_vertex)

print(shortest_distance_from_A)
print(previous_vertexes)
    
dist_to_C = shortest_distance_from_A[2]
path_to_C = []
previous_vertex = previous_vertexes[2]
path_to_C.append(previous_vertex)
path_to_C.append(2)
while(previous_vertex != 0):
    previous_vertex = previous_vertexes[previous_vertex]
    path_to_C = [previous_vertex] + path_to_C

print("the shortest distance from 0 to 2 is: " + str(dist_to_C))
print("the path taken is:")
print(path_to_C)
