from p1 import (
    build_tree,
    left_neighbor,
    right_neighbor,
    explode,
    split,
    add,
    reduce,
    magnitude,
)
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.t1 = build_tree([[[[[9, 8], 1], 2], 3], 4])
        self.t2 = build_tree([[6, [5, [4, [3, 2]]]], 1])
        self.t3 = build_tree([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]])

    def test_structure(self):
        self.assertEqual(self.t1.right.val, 4)
        self.assertEqual(self.t1.left.right.val, 3)

        self.assertEqual(self.t1.right.parent, self.t1)
        self.assertEqual(self.t1.left.right.parent, self.t1.left)

        self.assertEqual(self.t1.depth, 0)
        self.assertEqual(self.t1.right.depth, 1)
        self.assertEqual(self.t1.left.left.depth, 2)

    def test_neighbors(self):
        self.assertEqual(left_neighbor(self.t1.right).val, 3)
        self.assertEqual(right_neighbor(self.t1.left).val, 4)
        self.assertEqual(right_neighbor(self.t1.left.left.left.left).val, 1)

        self.assertEqual(left_neighbor(self.t2.left.right.right.right).val, 4)
        self.assertEqual(right_neighbor(self.t2.left.right.right.right).val, 1)

    def test_explode(self):
        explode(self.t1)
        self.assertEqual(self.t1.left.left.left.left.val, 0)
        self.assertEqual(self.t1.left.left.left.right.val, 9)

        explode(self.t2)
        self.assertEqual(self.t2.left.right.right.left.val, 7)
        self.assertEqual(self.t2.left.right.right.right.val, 0)
        self.assertEqual(self.t2.right.val, 3)

    def test_split(self):
        t = build_tree([11, 0])
        split(t)
        self.assertEqual(t.left.left.val, 5)
        self.assertEqual(t.left.right.val, 6)

    def test_reduce(self):
        t = build_tree([[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]])
        reduce(t)
        self.assertEqual(t.right.left.val, 8)
        self.assertEqual(t.right.right.val, 1)

    def test_add(self):
        t = add(build_tree([1, 2]), build_tree([[3, 4], 5]))
        self.assertEqual(t.left.left.depth, 2)
        self.assertEqual(t.right.right.val, 5)

    def test_magnitude(self):
        t = build_tree(
            [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]
        )
        self.assertEqual(magnitude(t), 3488)


if __name__ == "__main__":
    unittest.main()
