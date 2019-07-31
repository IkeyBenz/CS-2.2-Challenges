from util import file_to_graph
from sys import argv

if __name__ == '__main__':
    assert argv[1] is not None, "Data file path is required."

    assert argv[2] is not None, "'From' vertex is required."
    assert argv[3] is not None, "'To' vertex is required."

    graph = file_to_graph(argv[1])
    start, stop = argv[2], argv[3]

    if start.isdigit():
        start = int(start)
    if stop.isdigit():
        stop = int(stop)

    path = graph.shortest_path_between(start, stop)

    print(path)

    print(f"Vertices in shortest path: {','.join(path)}")
    print(f"Number of edges in shortest path: {len(path) - 1}")
