class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def right_rotate(node):
            if not node or not node.left:
                return node
            x = node
            y = node.left
            x.left = y.right
            y.right = x
            return right_rotate(y)  # keep doing right rotations until current root does not have left child
        new_root = right_rotate(root)   # find new root by keep performing right rotations on root
        temp = new_root
        while temp:
            temp.right = right_rotate(temp.right)   # perform right rotations on every right child
            temp = temp.right
        return new_root