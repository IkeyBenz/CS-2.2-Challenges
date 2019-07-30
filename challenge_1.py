from util import file_to_graph
from sys import argv

if __name__ == '__main__':
    assert argv[1] is not None, "Need data file path"

    graph = file_to_graph(argv[1])
    print(f"# Vertices: {graph.num_vertices}")
    print(f"# Edges: {len(graph.edges)}")
    print("Edge List:")
    print("\n".join(str(edge) for edge in graph.edges))
