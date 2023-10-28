import matplotlib.pyplot as plt
import matplotlib.patches as patches


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
            return
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

    def draw(self, filename=None):
        fig, ax = plt.subplots(figsize=(15, 10))
        ax.set_aspect('equal')
        ax.set_axis_off()
        fig.patch.set_facecolor('#d0d0d0')

        self.positions = {}
        self._inorder_position(self.root, 0, 1)

        dy = 0.3
        self._draw_recursive(self.root, ax, 1, dy)

        if filename:
            plt.savefig(filename, bbox_inches='tight', pad_inches=0.1)
        else:
            plt.show()

    def _inorder_position(self, node, x, y):
        if not node:
            return x

        x = self._inorder_position(node.left, x, y - 1)

        self.positions[node] = (x, y)
        x += 1

        x = self._inorder_position(node.right, x, y - 1)

        return x

    def _draw_recursive(self, node, ax, y, dy):
        if not node:
            return

        x, _ = self.positions[node]

        if node.left:
            x_left, _ = self.positions[node.left]
            ax.plot([x, x_left], [y - dy, y - 2 * dy], 'k-')
            self._draw_recursive(node.left, ax, y - 2 * dy, dy)

        if node.right:
            x_right, _ = self.positions[node.right]
            ax.plot([x, x_right], [y - dy, y - 2 * dy], 'k-')
            self._draw_recursive(node.right, ax, y - 2 * dy, dy)

        ax.add_patch(patches.Circle((x, y), 0.3, fill=True))
        ax.text(x, y, str(node.key), va='center', ha='center',
                color='white', fontsize=7)
