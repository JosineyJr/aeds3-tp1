class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key == node.key:
            return  # Evita inserções duplicadas
        elif key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        comparisons = 1
        if node is None:
            return None, comparisons
        if key == node.key:
            return node, comparisons
        elif key < node.key:
            item, child_comparisons = self._search_recursive(node.left, key)
        else:
            item, child_comparisons = self._search_recursive(node.right, key)
            comparisons += child_comparisons

        return item, comparisons

    def get_all_keys(self):
        keys = []

        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                keys.append(node.key)
                inorder_traversal(node.right)

        inorder_traversal(self.root)
        return keys
