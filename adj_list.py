from queue import Queue
from stack import Stack

# lets do a graph adjacency list
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # if v1 and v2 exist
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # want to use a queue for bft
        # create empty queue and enqueue a starting vertex
        q = Queue()
        q.enqueue(starting_vertex_id)

        # create a set to store the visited vertices
        visited = set()

        # while the queue is not empty:
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()

            # if vertex has not been visited
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of it's neighbors to the back of the queue
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex_id):
        # want to use a stack for dft
        # create empty stack and enqueue a starting vertex
        s = Stack()
        s.push(starting_vertex_id)

        # create a set to store the visited vertices
        visited = set()

        # while the stack is not empty:
        while s.size() > 0:
            #  the first vertex
            v = s.pop()

            # if vertex has not been visited
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of it's neighbors to the top of the stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)

    def bfs(self, starting_vertex_id, target_vertex_id):
        # create an empty queue and enqueue a PATH to the starting vertex ID
        q = Queue()
        # initialize inside list
        q.enqueue([starting_vertex_id])

        # create a set to store the visited vertices
        visited = set()

        # while the queue is not empty:
        while q.size() > 0:
            # dequeue the first PATH
            v = q.dequeue()
            # grab the last vertex from the PATH
            # if vertex has not been visited:
            # is this vertex the target?
            # return the PATH
            # mark the vertex as visited
            # then add a PATH to its neighbors to the back of the queue
            # make a copy of the PATH
            # append the neighbor to the back of the PATH
            # enqueue out new PATH

        # return none
        return None

    def dfs(self, starting_vertex_id, target_vertex_id):
        pass

    def dft_recursive(self, starting_vertex, visited=None):
        visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                self.dft_recursive(v, visited)
