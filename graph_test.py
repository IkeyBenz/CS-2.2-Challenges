import unittest
from util import file_to_graph


class GraphTests(unittest.TestCase):

    def test_breadth_first_search(self):
        graph = file_to_graph('graph_data.txt')
        actual_order = [v for v in graph.breadth_first_traversal(1)]
        expected_order = [1, 2, 4, 3]

        assert actual_order == expected_order

    def test_shortest_path(self):
        graph = file_to_graph('graph_data2.txt')
        actual_path = graph.shortest_path_between(1, 3)
        expected_path = [1, 2, 3]

        assert actual_path == expected_path
