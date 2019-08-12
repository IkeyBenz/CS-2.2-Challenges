from collections import Counter
from sys import argv
from util import file_to_graph


def has_eulerian_cycle(edge_list):
    verts = []
    for a, b, _ in edge_list:
        verts.extend([a, b])

    vert_hist = Counter(verts)
    for count in vert_hist.values():
        # If eulerian, all vertices should have an even number of neighbors
        if count % 2 != 0:
            return False
    return True


if __name__ == '__main__':
    graph = file_to_graph(argv[1])
    has = has_eulerian_cycle(graph.edges)
    print(f"This graph {'has' if has else 'doesnt have'} an Eulerian cylce.")
