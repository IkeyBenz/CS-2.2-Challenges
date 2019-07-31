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
        self.directional = g_type in ['d', 'D']
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
            self.add_vertex(start)
        if end not in self.vertices:
            self.add_vertex(end)

        self.get_vertex(start).add_neighbor(end, cost)
        if not self.directional:
            self.get_vertex(end).add_neighbor(start, cost)

        self.edges.append((start, end, cost))

    def get_vertices(self):
        """ Returns all the vertices in the graph """

        return self.vertices.keys()

    def breadth_first_traversal(self, start):
        """
           Returns a generator of vertices in breadth-first order
           from a start vertex
        """

        queue = [start]  # A 'queue' for storing vertices to check later
        seen = {start}  # A set of all the seen vertices

        yield start
        while len(queue):
            for vertex in self.vertices[queue.pop(0)].get_neighbors():
                if vertex not in seen:
                    yield vertex
                    seen.add(vertex)
                    queue.append(vertex)

    def shortest_path_between(self, start, end):
        """
            Returns a list of vertices that represent the shortest path
            between start and end vertices.
        """
        path = [start]
        start_neighbors = list(self.vertices[start].get_neighbors())

        if end in start_neighbors:
            return path + [end]
        else:
            # Arbitrarily pick the first vertex in list of neighbors as next link in path
            the_rest = self.shortest_path_between(start_neighbors[0], end)
            path.extend(the_rest)

        return path

    def depth_first_traversal(self, start, end, visit, seen=None):
        """
            Uses depth first search to traverse the graph from a
            start vertex.
        """

        if seen is None:
            seen = {start}

        vert = self.vertices[start]
        yield vert

        for neighbor in vert.get_neighbors():
            if neighbor not in seen:
                if neighbor is end:
                    yield self.vertices[end]
                else:
                    seen.add(neighbor)
                    return self.depth_first_traversal(neighbor, end, visit, seen)

    def __iter__(self):
        """
            Iterates over the vertex objects in the graph.
            Allows sytax: for v in g
        """
        return iter(self.vertices.values())
