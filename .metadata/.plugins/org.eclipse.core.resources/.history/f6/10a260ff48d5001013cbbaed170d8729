"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author: Joseph Jatou
ID: 169088805
Email: jato8805@mylaurier.ca
__updated__ = "2025-11-03"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _BST_Node:
    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        
    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            inserted = False

        if inserted:
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:
            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                value = deepcopy(node._value)
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes
        the node if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Parameters:
            node - a bst node to search for key (_BST_Node)
            key - data to search for (?)
        Returns:
            node - the current node or its replacement (_BST_Node)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            return_node = None
            value = None
        elif key < node._value:
            node._left, value = self._remove_aux(node._left, key)
            return_node = node
        elif key > node._value:
            node._right, value = self._remove_aux(node._right, key)
            return_node = node
        else:
            value = node._value
            self._count -= 1

            if node._left is None and node._right is None:
                return_node = None
            elif node._left is None:
                return_node = node._right
            elif node._right is None:
                return_node = node._left
            else:
                pred = self._delete_node_left(node)
                pred._left = node._left
                pred._right = node._right
                return_node = pred

        if return_node is not None and value is not None:
            return_node._update_height()
        return return_node, value

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node.
                This node is the node with the maximum value in the
                deleted node's left subtree (_BST_Node)
        -------------------------------------------------------
        """
        if parent._left._right is None:
            repl_node = parent._left
            parent._left = repl_node._left
        else:
            repl_node = self._delete_node_left_aux(parent._left)
        return repl_node

    def _delete_node_left_aux(self, parent):
        """
        -------------------------------------------------------
        Helper to find the maximum node in left subtree.
        -------------------------------------------------------
        """
        if parent._right._right is None:
            repl_node = parent._right
            parent._right = repl_node._left
        else:
            repl_node = self._delete_node_left_aux(parent._right)
        return repl_node

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """
        node = self._root
        found = False

        while node is not None and not found:
            if key < node._value:
                node = node._left
            elif key > node._value:
                node = node._right
            else:
                found = True
        return found

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """
        if self._root is None:
            h = 0
        else:
            h = self._root._height
        return h

    def __eq__(self, target):
        """
        --------------------------------------------------------
        Determines whether two BSTs are equal.
        Values in self and target are compared and if all values are
        equal and in the same location, returns True, otherwise
        returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a bst (BST)
        Returns:
            equals - True if source contains the same values
                as target in the same location, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equals = self._eq_aux(self._root, target._root)
        return equals

    def _eq_aux(self, node1, node2):
        """
        -------------------------------------------------------
        Helper for equality comparison.
        -------------------------------------------------------
        """
        if node1 is None and node2 is None:
            equals = True
        elif node1 is None or node2 is None:
            equals = False
        elif node1._value != node2._value:
            equals = False
        else:
            equals = self._eq_aux(node1._left, node2._left) and self._eq_aux(node1._right, node2._right)
        return equals

    def parent(self, key):
        """
        --------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        --------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
                key node, None if the key is not found. (?)
        --------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        if self._root._value == key:
            value = None
        else:
            value = self._parent_aux(self._root, key)
        return value

    def _parent_aux(self, node, key):
        """
        -------------------------------------------------------
        Helper for finding parent iteratively.
        -------------------------------------------------------
        """
        parent_value = None
        current = node

        while current is not None and parent_value is None:
            if key < current._value:
                if current._left is not None and current._left._value == key:
                    parent_value = deepcopy(current._value)
                else:
                    current = current._left
            elif key > current._value:
                if current._right is not None and current._right._value == key:
                    parent_value = deepcopy(current._value)
                else:
                    current = current._right
            else:
                current = None
        return parent_value

    def parent_r(self, key):
        """
        --------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        --------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
                key node, None if the key is not found.
        --------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        if self._root._value == key:
            value = None
        else:
            value = self._parent_r_aux(self._root, key)
        return value

    def _parent_r_aux(self, node, key):
        """
        -------------------------------------------------------
        Helper for finding parent recursively.
        -------------------------------------------------------
        """
        if node is None:
            parent_value = None
        elif (node._left is not None and node._left._value == key) or (node._right is not None and node._right._value == key):
            parent_value = deepcopy(node._value)
        elif key < node._value:
            parent_value = self._parent_r_aux(node._left, key)
        else:
            parent_value = self._parent_r_aux(node._right, key)
        return parent_value

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        node = self._root
        while node._right is not None:
            node = node._right
        value = deepcopy(node._value)
        return value

    def max_r(self):
        """
        --------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        --------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        --------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        value = self._max_r_aux(self._root)
        return value

    def _max_r_aux(self, node):
        """
        -------------------------------------------------------
        Helper for finding maximum recursively.
        -------------------------------------------------------
        """
        if node._right is None:
            value = deepcopy(node._value)
        else:
            value = self._max_r_aux(node._right)
        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        node = self._root
        while node._left is not None:
            node = node._left
        value = deepcopy(node._value)
        return value

    def min_r(self):
        """
        --------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        --------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        --------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        value = self._min_r_aux(self._root)
        return value

    def _min_r_aux(self, node):
        """
        -------------------------------------------------------
        Helper for finding minimum recursively.
        -------------------------------------------------------
        """
        if node._left is None:
            value = deepcopy(node._value)
        else:
            value = self._min_r_aux(node._left)
        return value

    def leaf_count(self):
        """
        --------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: count = bst.leaf_count()
        --------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        --------------------------------------------------------
        """
        count = self._leaf_count_aux(self._root)
        return count

    def _leaf_count_aux(self, node):
        """
        -------------------------------------------------------
        Helper for counting leaves.
        -------------------------------------------------------
        """
        if node is None:
            count = 0
        elif node._left is None and node._right is None:
            count = 1
        else:
            count = self._leaf_count_aux(node._left) + self._leaf_count_aux(node._right)
        return count

    def two_child_count(self):
        """
        --------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        count = self._two_child_count_aux(self._root)
        return count

    def _two_child_count_aux(self, node):
        """
        -------------------------------------------------------
        Helper for counting nodes with two children.
        -------------------------------------------------------
        """
        if node is None:
            count = 0
        elif node._left is not None and node._right is not None:
            count = 1 + self._two_child_count_aux(node._left) + self._two_child_count_aux(node._right)
        else:
            count = self._two_child_count_aux(node._left) + self._two_child_count_aux(node._right)
        return count

    def one_child_count(self):
        """
        --------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """
        count = self._one_child_count_aux(self._root)
        return count

    def _one_child_count_aux(self, node):
        """
        -------------------------------------------------------
        Helper for counting nodes with one child.
        -------------------------------------------------------
        """
        if node is None:
            count = 0
        elif (node._left is None and node._right is not None) or (node._left is not None and node._right is None):
            count = 1 + self._one_child_count_aux(node._left) + self._one_child_count_aux(node._right)
        else:
            count = self._one_child_count_aux(node._left) + self._one_child_count_aux(node._right)
        return count

    def node_counts(self):
        """
        --------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        zero, one, two = self._node_counts_aux(self._root)
        return zero, one, two

    def _node_counts_aux(self, node):
        """
        -------------------------------------------------------
        Helper for counting all node types.
        -------------------------------------------------------
        """
        if node is None:
            zero = 0
            one = 0
            two = 0
        else:
            left_zero, left_one, left_two = self._node_counts_aux(node._left)
            right_zero, right_one, right_two = self._node_counts_aux(node._right)

            if node._left is None and node._right is None:
                zero = 1 + left_zero + right_zero
                one = left_one + right_one
                two = left_two + right_two
            elif node._left is not None and node._right is not None:
                zero = left_zero + right_zero
                one = left_one + right_one
                two = 1 + left_two + right_two
            else:
                zero = left_zero + right_zero
                one = 1 + left_one + right_one
                two = left_two + right_two
        return zero, one, two

    def is_balanced(self):
        """
        --------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in height
        between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        --------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        --------------------------------------------------------
        """
        balanced = self._is_balanced_aux(self._root)
        return balanced

    def _is_balanced_aux(self, node):
        """
        -------------------------------------------------------
        Helper for checking if tree is balanced.
        -------------------------------------------------------
        """
        if node is None:
            balanced = True
        else:
            left_height = self._node_height(node._left)
            right_height = self._node_height(node._right)

            if abs(left_height - right_height) > 1:
                balanced = False
            else:
                balanced = self._is_balanced_aux(node._left) and self._is_balanced_aux(node._right)
        return balanced

    def _node_height(self, node):
        """
        --------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        --------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        --------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """
        value = self._retrieve_r_aux(self._root, key)
        return value

    def _retrieve_r_aux(self, node, key):
        """
        -------------------------------------------------------
        Helper for retrieving recursively.
        -------------------------------------------------------
        """
        if node is None:
            value = None
        elif key < node._value:
            value = self._retrieve_r_aux(node._left, key)
        elif key > node._value:
            value = self._retrieve_r_aux(node._right, key)
        else:
            value = deepcopy(node._value)
        return value

    def is_valid(self):
        """
        --------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left
        nodes are smaller than their parent, and the values in all right
        nodes are larger than their parent, and height of any node is
        1 + max height of its children.
        Use: b = bst.is_valid()
        --------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        --------------------------------------------------------
        """
        valid, _, _ = self._is_valid_aux(self._root)
        return valid

    def _is_valid_aux(self, node):
        """
        -------------------------------------------------------
        Helper for validating BST structure.
        -------------------------------------------------------
        """
        if node is None:
            valid = True
            mn = None
            mx = None
        else:
            lv, lmin, lmax = self._is_valid_aux(node._left)
            rv, rmin, rmax = self._is_valid_aux(node._right)

            if not lv or not rv:
                valid = False
                mn = None
                mx = None
            elif lmax is not None and lmax >= node._value:
                valid = False
                mn = None
                mx = None
            elif rmin is not None and rmin <= node._value:
                valid = False
                mn = None
                mx = None
            else:
                expected_height = max((node._left._height if node._left else 0),
                                     (node._right._height if node._right else 0)) + 1
                if node._height != expected_height:
                    valid = False
                    mn = None
                    mx = None
                else:
                    valid = True
                    mn = lmin if lmin is not None else node._value
                    mx = rmax if rmax is not None else node._value
        return valid, mn, mx

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        result = []
        self._inorder_aux(self._root, result)
        return result

    def _inorder_aux(self, node, result):
        """
        -------------------------------------------------------
        Helper for inorder traversal.
        -------------------------------------------------------
        """
        if node is not None:
            self._inorder_aux(node._left, result)
            result.append(deepcopy(node._value))
            self._inorder_aux(node._right, result)
        return

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        result = []
        self._preorder_aux(self._root, result)
        return result

    def _preorder_aux(self, node, result):
        """
        -------------------------------------------------------
        Helper for preorder traversal.
        -------------------------------------------------------
        """
        if node is not None:
            result.append(deepcopy(node._value))
            self._preorder_aux(node._left, result)
            self._preorder_aux(node._right, result)
        return

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        result = []
        self._postorder_aux(self._root, result)
        return result

    def _postorder_aux(self, node, result):
        """
        -------------------------------------------------------
        Helper for postorder traversal.
        -------------------------------------------------------
        """
        if node is not None:
            self._postorder_aux(node._left, result)
            self._postorder_aux(node._right, result)
            result.append(deepcopy(node._value))
        return

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
                (list of ?)
        -------------------------------------------------------
        """
        values = []

        if self._root is not None:
            q = [self._root]

            while q:
                node = q.pop(0)
                values.append(deepcopy(node._value))

                if node._left is not None:
                    q.append(node._left)
                if node._right is not None:
                    q.append(node._right)
        return values

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """
        return self._count

    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)