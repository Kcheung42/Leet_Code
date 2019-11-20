class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, array=None):
        self.root = None
        if array:
            self.build_tree(array)

    def inorder(self):
        def recur(result):
            if self.root is None:
                return
            recur(self.root.left)
            result.append(self.root.val)
            recur(self.root.right)

        result = []
        recur(root, result)
        return result

    def build_tree(self, array):

        def get_child_left(i, flag):
            if flag:
                return 2 * i + 1
            return 2 * i + 2

        def build_tree_helper(array, i):
            if i > len(array) - 1 or array[i] == None:
                return None
            node = TreeNode(array[i])
            left_child = get_child_left(i, True)
            right_child = get_child_left(i, False)
            node.left = build_tree_helper(array, left_child)
            node.right = build_tree_helper(array, right_child)
            return node
        i = 0
        node = TreeNode(array[i])
        self.root = node
        left_child = get_child_left(i, True)
        right_child = get_child_left(i, False)
        node.left = build_tree_helper(array, left_child)
        node.right = build_tree_helper(array, right_child)
