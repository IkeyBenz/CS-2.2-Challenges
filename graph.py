#!python

""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""

from vertex import Vertex


class Graph:
    def __init__(self, g_type):
        """ Initializes a graph object with an empty dictionary """
        self.vertices = {}
        self.num_vertices = 0
        self.directional = g_type == 'd'
        self.edges = []

    def add_vertex(self, key):
        """
        Adds a new vertex object to the graph with
        the given key and return the vertex
        """
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

        return new_vertex

    def get_vertex(self, key):
        """ Returns the vertex if it exists """
        return self.vertices[key]

    def add_edge(self, start, end, cost=0):
        """ Adds an edge from vertex f to vertex t with a cost """
        if start not in self.vertices:
            self.vertices[start] = Vertex(start)
        if end not in self.vertices:
            self.vertices[end] = Vertex(end)

        self.vertices[start].add_neighbor(self.vertices[end], cost)
        self.edges.append((start, end, cost))

    def get_vertices(self):
        """ Returns all the vertices in the graph """

        return self.vertices.keys()

    def breadth_first_traversal(self, start, visit):
        """
           Uses breadth first search to find the shortest path
           between two vertices.
        """

        queue = [start]  # A 'queue' for storing vertices to check later
        seen = {start}  # A set of all the seen vertices

        while len(queue):
            for vertice in self.vertices[queue.pop(0)].get_neighbors():
                if vertice not in seen:
                    visit(vertice)
                    seen.add(vertice)
                    queue.append(vertice)

    def depth_first_traversal(self, start, end, visit, seen=None):
        """
            Uses depth first search to traverse the graph from a
            start vertex.
        """

        if seen is None:
            seen = {start}

        vert = self.vertices[start]
        visit(vert)

        for neighbor in vert.get_neighbors():
            if neighbor not in seen:
                if neighbor is end:
                    return visit(self.vertices[end])
                else:
                    seen.add(neighbor)
                    return self.depth_first_traversal(neighbor, end, visit, seen)

    def __iter__(self):
        """
        Iterates over the vertex objects in the graph.
        Allows sytax: for v in g
        """
        return iter(self.vertices.values())
