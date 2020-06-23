class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.val})"

class BinaryTree:
    def __init__(self, array=None):
        self.root = None
        if array:
            self.build_tree(array)

    def inorder(self):
        def recur(root):
            if root is None:
                return
            recur(root.left)
            result.append(root.val)
            recur(root.right)
        result = []
        recur(self.root)
        return result

    # '[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]'

    def preorder(self):
        def recur(root):
            if root is None:
                result.append(None)
                return
            result.append(root.val)
            recur(root.left)
            recur(root.right)
        result = []
        recur(self.root)
        return result

    def __repr__(self):
        order = self.inorder()
        print(order)
        return f'BinaryTree(Inorder={",".join([str(x) for x in order])})'

    def build_tree(self, array):

        def get_child_left(i, flag):
            looking_left = flag
            if looking_left:
                if i in left_children:
                    return i + 2
                else:
                    return i + 3
            #else looking for right child
            if i in left_children:
                return i + 3
            else:
                return i + 4

        def build_tree_helper(array, i):
            if i > len(array) - 1 or array[i] == None:
                return None
            node = TreeNode(array[i])
            left_child = get_child_left(i, True)
            right_child = get_child_left(i, False)
            node.left = build_tree_helper(array, left_child)
            if node.left:
                left_children.add(left_child)
            node.right = build_tree_helper(array, right_child)
            return node
        i = 0
        node = TreeNode(array[i])
        left_children = set([0])
        self.root = node
        left_child = i+1
        right_child = i+2
        left_children.add(left_child)
        node.left = build_tree_helper(array, left_child)
        node.right = build_tree_helper(array, right_child)
