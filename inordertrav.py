#Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

out = []

def recurs(node):
    global out

    if node == None or node.val == None:
        return
    recurs(node.left)
    out.append(node.val)
    recurs(node.right)

class Solution(object):
    def inorderTraversal(self, root):
        global out
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]

        out = []
        recurs(root)
        return out