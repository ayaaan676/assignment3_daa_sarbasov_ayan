
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src" / "Python"))

from algorithms import reconstruct_route


class RouteTests(unittest.TestCase):
    def test_reachable_target(self):
        edges = [[0, 1, 3], [1, 2, -7], [2, 3, 4]]
        parent_edge = [-1, 0, 1, 2]
        self.assertEqual(
            reconstruct_route(0, 3, parent_edge, edges),
            [0, 1, 2, 3]
        )

    def test_source_to_itself(self):
        self.assertEqual(reconstruct_route(0, 0, [-1], []), [0])

    def test_unreachable_target(self):
        self.assertEqual(reconstruct_route(0, 2, [-1, -1, -1], []), [])

    def test_parallel_edges(self):
        edges = [[0, 1, 5], [0, 1, 2], [1, 2, 4]]
        parent_edge = [-1, 1, 2]
        self.assertEqual(
            reconstruct_route(0, 2, parent_edge, edges),
            [0, 1, 2]
        )


if __name__ == "__main__":
    unittest.main()
