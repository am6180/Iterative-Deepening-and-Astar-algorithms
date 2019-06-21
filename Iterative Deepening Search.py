"""
FIS Project 1
CSCI 630
@author: Aditi Munjekar
This is an unformed path finding algorithm which finds the path by exploring all the nodes at a particular depth until it finds the goal.
"""
import sys

class Graph:
    __slots__ = ("vertices")

    def __init__(self):
        self.vertices = {}
    #adds an edge to the node in the graph
    def add_edge(self, u, v):
        self.graph[u].append[v]

    #function to go upto a particular depth and explore all the nodes at that depth
    def DLS(self, maze, start, goal, maxDepth, current_depth=0, visited=None):
        if maxDepth < 0:
            return None, 0

        if visited is None:
            visited = {}

        if(current_depth >= maxDepth):
            return None, len(visited)

        width_maze = len(maze[0])
        height_maze = len(maze)
        current_node = start

        if start == goal:
            print ("Goal found...............")
            print current_node
            return [goal], len(visited)

        current_node_x, current_node_y = current_node.split(",")[1], current_node.split(",")[0]
        visited[current_node] = current_depth

        #neighbours of a particular cell in the maze
        for n in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_position_x = int(current_node_x) + int(n[1])
            new_position_y = int(current_node_y) + int(n[0])

            if new_position_x < 0 or new_position_x > width_maze - 1 or new_position_y < 0 or new_position_y > height_maze - 1:
                continue

            # avoiding the obstacle
            if maze[new_position_y][new_position_x] == "1":
                continue

            child_node = str(new_position_y) + "," + str(new_position_x)
            if child_node not in visited or (child_node in visited and visited[child_node] > current_depth + 1):
                 path, count = self.DLS(maze,child_node,goal,maxDepth, current_depth + 1, visited)
                 if path is not None:
                    return [start] + path, len(visited)
        return None, len(visited)

    #function to call DLS upto a particular depth
    def IDFS(self, maze, start, end, max_depth):
        total_count = 0
        for i in range(max_depth+1):
            print("Current depth *********************** ,", i)
            result = self.DLS(maze, start, end, i)
            total_count+=result[1]
            if result[0]:
                return total_count, result

def main():
    #reading and parsing the file
    filename = open("11", "r")
    maze = []

    for line in filename:
        l = line.strip().split(" ")
        maze.append(l)
    filename.close()
    start = "0,0"
    end = str(len(maze) - 1) + "," + str(len(maze[0]) - 1)

    g = Graph()
    print start, end
    print g.IDFS(maze, start, end, len(maze)*len(maze[0]))

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    main()
