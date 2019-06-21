"""
FIS Project 1
CSCI 630
@author: Aditi Munjekar
This is an intelligent, informed path finding algorithm which finds the path using heuristics.
"""
import sys
import math

#Maintaining a priority queue to select the node which has the minimum value of "f"
class PQ:
    __slots__ = ('contents')
    def __init__(self):
        self.contents = {}

    def add(self, vertex, cost):
        self.contents[vertex] = cost

    def pop(self):
        cost = None
        result = None
        for v,c in self.contents.items():
            if cost is None or c < cost:
                cost = c
                result = v
        del self.contents[result]
        return result, cost

    def decrease(self, vertex, cost):
        # Coincidentally same implementation as add.
        self.contents[vertex] = cost

    def empty(self):
        return len(self.contents) == 0

#Graph class which maintains the vertices and the edges of the vertices with the costs for each
class Graph:
    __slots__ = ("vertices")

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key ,costs=None):
        if costs is None:
            self.vertices[key] = []
        else:
            self.vertices[key] = costs

#to print the path of tracing
def unwind(steps, begin, end):
    if (begin is end):
        return [begin]
    else:
        return unwind(steps, begin, steps[end]) + [end]

#constant heuristic
def heuristics_constant(currentx, currenty, goalx, goaly):
    return 1

#Manhattan heuristic
def heuristics_manhattan(currentx, currenty, goalx, goaly):
    return abs(currentx - goalx) + abs(currenty - goaly)

#Euclidean heuristic
def heuristics_euclid(currentx, currenty, goalx, goaly):
    return math.sqrt((((currentx - goalx)**2)+((currenty - goaly)**2)))

#random heuristic
def heuristics_random(currentx, currenty, goalx, goaly):
    answer = hash(currenty) * 100
    return answer

#function to find the path from the start
def astar(maze, start, end):

    graph = Graph()

    graph.add_vertex(start)  # adding start vertex
    graph.vertices[start] = [0,0,0]
    graph.add_vertex(end)  # adding goal vertex
    graph.vertices[end] = [0,0,0]
    height_maze = len(maze) #length of the maze
    width_maze = len(maze[0]) #width of the maze
    q = PQ()
    steps = {}
    costs = {start:0}
    q.add(start, 0)
    visited_counter = 0 #counter to maintain the visited nodes
    discovered_node = 0 #counter to maintain the discovered nodes

    #loop to find all elements in the maze
    while not q.empty():
        current_node, current_node_cost = q.pop()
        visited_counter = visited_counter + 1
        if current_node == end:
            # ADD TEXT FOR GOAL
            return visited_counter, discovered_node, len(unwind(steps, start, end)), unwind(steps, start, end)
            print("Goal reached")

        current_node_x , current_node_y = current_node.split(",")[1], current_node.split(",")[0]
        parent_scores_set = graph.vertices[current_node]
        parent_scores_f, parent_scores_g, parent_scores_h = parent_scores_set[0], parent_scores_set[1], parent_scores_set[2]

        ## finding neighbors of the vertex
        for n in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_position_x = int(current_node_x) + int(n[1])
            new_position_y = int(current_node_y) + int(n[0])

            #border of maze constraints
            if new_position_x < 0 or new_position_x > width_maze -1 or new_position_y < 0  or new_position_y > height_maze - 1:
                continue

            # avoiding the obstacle
            if maze[new_position_y][new_position_x] == "1":
                continue

            discovered_node = discovered_node + 1
            child_node = str(new_position_y) +"," + str(new_position_x)
            child_score_g = parent_scores_g + 1
            child_node_x = child_node.strip().split(',')[0]
            child_node_y = child_node.strip().split(',')[1]
            end_x = end.strip().split(',')[0]
            end_y = end.strip().split(',')[1]
            child_score_h = heuristics_random(int(child_node_x), int(child_node_y) , int(end_x), int(end_y))
            child_score_f = child_score_g + child_score_h #weight of the child node
            child_score_set = [child_score_f, child_score_g, child_score_h]
            graph.add_vertex(child_node, child_score_set)

            #calculating cost for every neighbour
            if child_node not in costs:
                q.add(child_node, parent_scores_g+child_score_f)
                costs[child_node] = parent_scores_g + child_score_f
                steps[child_node] = current_node

            #finding a better path
            elif parent_scores_g + child_score_f < costs[child_node]:
                costs[child_node] = child_score_f + parent_scores_g
                steps[child_node] = current_node
                q.decrease(child_node, costs[child_node]) #removing that node from the queue

def main():
    #opening and parsing the file
    filename = open("11", "r")
    maze = []

    for line in filename:
        l = line.strip().split(" ")
        maze.append(l)
    filename.close()
    start = "0,0"
    end = str(len(maze) - 1) + "," + str(len(maze[0])-1)

    print astar(maze, start, end)

if __name__ == '__main__':
    sys.setrecursionlimit(40000)
    main()


