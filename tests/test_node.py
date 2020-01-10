import nfem
from numpy.testing import assert_array_almost_equal
import unittest


class TestNode(unittest.TestCase):
    def test_init(self):
        node = nfem._node.Node('Test', 1, 2, 3)

        self.assertEqual(node.key, 'Test')
        self.assertEqual(node.x.value, 1)
        self.assertEqual(node.y.value, 2)
        self.assertEqual(node.z.value, 3)

        self.assertEqual(node.x.initial_value, 1)
        self.assertEqual(node.y.initial_value, 2)
        self.assertEqual(node.z.initial_value, 3)

        assert_array_almost_equal(node.location, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
