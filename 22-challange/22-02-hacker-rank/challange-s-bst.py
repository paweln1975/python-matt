"""
Binary Search Tree
"""
import unittest
import random
from abc import abstractmethod

__all__ = ["Tree", "NonEmptyBST", "EmptyBST"]


class Tree:
    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def cardinality(self) -> int:
        pass

    @abstractmethod
    def is_member(self, element) -> bool:
        pass

    @abstractmethod
    def add(self, element) -> object:
        pass

    @abstractmethod
    def height(self, level: int = 0) ->int:
        pass


class NonEmptyBST(Tree):

    def __init__(self, element, left, right):
        self.data = element
        self.left: Tree = left
        self.right: Tree = right

    def is_empty(self) -> bool:
        return False

    def cardinality(self) -> int:
        return 1 + self.left.cardinality() + self.right.cardinality()

    def is_member(self, element) -> bool:
        if self.data == element:
            return True
        else:
            if element < self.data:
                if isinstance(self.left, NonEmptyBST):
                    return self.left.is_member(element)
            else:
                if isinstance(self.right, NonEmptyBST):
                    return self.right.is_member(element)
        return False

    def add(self, element) -> Tree:
        if self.data == element:
            return self
        else:
            if element < self.data:
                return NonEmptyBST(self.data, self.left.add(element), self.right)

            if element > self.data:
                return NonEmptyBST(self.data, self.left, self.right.add(element))

    def __str__(self):
        space = ' ' * self.cardinality()
        return space + str(self.data) + '\n' + space + '-->' + str(self.left) + '\n' + space + '-->' + str(self.right)

    def __repr__(self):
        return str(self)

    def height(self, level: int = 0) -> int:

        if isinstance(self.left, NonEmptyBST) or isinstance(self.right, NonEmptyBST):
            level += 1
            level = max(self.left.height(level), self.right.height(level))

        return level

class EmptyBST(Tree):

    def height(self, level: int = 0) -> int:
        return 0

    def is_empty(self) -> bool:
        return True

    def cardinality(self) -> int:
        return 0

    def is_member(self, element) -> bool:
        return False

    def add(self, element) -> Tree:
        return NonEmptyBST(element, EmptyBST(), EmptyBST())

    def __str__(self):
        return 'empty'

    def __repr__(self):
        return str(self)




class BSTTest(unittest.TestCase):
    def setUp(self):
        self.tree = EmptyBST()

    def test_simple_create(self):
        tree = self.tree.add(10).add(11).add(12).add(13).add(14).add(15)
        self.assertEqual(6, tree.cardinality(),'Wrong cardinality')

    def test_add_100_elements(self):
        for i in range(100):
            self.tree = self.tree.add(i)
        self.assertEqual(100, self.tree.cardinality(), 'Wrong cardinality')

    def test_is_member_simple(self):
        self.tree = self.tree.add(10)
        self.assertEqual(True, self.tree.is_member(10), 'Wrong membership')

    def test_is_not_member_simple(self):
        self.tree = self.tree.add(10)
        self.assertEqual(False, self.tree.is_member(15), 'Wrong membership')

    def test_is_member_simple_3(self):
        self.tree = self.tree.add(10).add(11).add(12)
        self.assertEqual(True, self.tree.is_member(10), 'Wrong membership')
        self.assertEqual(True, self.tree.is_member(11), 'Wrong membership')
        self.assertEqual(True, self.tree.is_member(12), 'Wrong membership')

    def test_is_not_member_simple_3(self):
        self.tree = self.tree.add(10).add(11).add(12)
        self.assertEqual(False, self.tree.is_member(1), 'Wrong membership')
        self.assertEqual(False, self.tree.is_member(15), 'Wrong membership')

    def test_is_member(self):
        for i in range(100):
            self.tree = self.tree.add(i)
        self.assertEqual(True, self.tree.is_member(50),'Wrong membership')

    def test_performance_add_950(self):
        size = 950
        for i in range(size):
            self.tree = self.tree.add(i)
        self.assertEqual(size, self.tree.cardinality(), 'Wrong cardinality')

    def test_random_create(self):
        random.seed(0)
        values = [random.randint(1, 1000) for _ in range(1000)]
        for value in values:
            self.tree = self.tree.add(value)
        self.assertGreaterEqual(self.tree.cardinality(), 1, "Wrong cardinality")

    def test_add_tree_simple(self):
        values = [13, 20, 15, 11, 14, 17]

        for value in values:
            self.tree = self.tree.add(value)

        self.assertEqual(6, self.tree.cardinality(), "Wrong cardinality")

    def test_height(self):
        values = [7, 3, 5, 2, 1, 4, 6, 7]

        for value in values:
            self.tree = self.tree.add(value)

        self.assertEqual(3, self.tree.height(), "Wrong height")


    def test_height_1(self):
        values = [9, 20, 50, 35, 44, 9, 15, 62, 11, 13]

        for value in values:
            self.tree = self.tree.add(value)

        self.assertEqual(4, self.tree.height(), "Wrong height")

    def test_height_2(self):
        values = [1, 2, 3, 4, 5, 6]

        for value in values:
            self.tree = self.tree.add(value)

        self.assertEqual(len(values) - 1, self.tree.height(), "Wrong height")

    def test_height_simple(self):
        self.tree.add(10)
        self.assertEqual(0, self.tree.height(), "Wrong height")


if __name__ == "__main__":
    unittest.main()
