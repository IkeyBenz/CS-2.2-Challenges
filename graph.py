#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """Initializes a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with 
          key = vertex,
          value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Adds a neighbor along a weighted edge"""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """Outputs the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def get_neighbors(self):
        """Returns the neighbors of this vertex"""
        return self.neighbors.keys()

    def get_id(self):
        """Returns the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """Returns the weight of this edge"""
        return self.neighbors[vertex]


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertices = {}
        self.numVertices = 0

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        self.numVertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

        return new_vertex

    def get_vertex(self, key):
        """return the vertex if it exists"""
        return self.vertices[key]

    def add_edge(self, f, t, cost=0):
        """ Adds an edge from vertex f to vertex t with a cost """
        if f not in self.vertices:
            self.vertices[f] = Vertex(f)
        if t not in self.vertices:
            self.vertices[t] = Vertex(t)

        self.vertices[f].add_neighbor(self.vertices[t], cost)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertices.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertices.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.getNeighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))
