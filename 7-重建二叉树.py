"""
page 62, problem 7
根据前序遍历序列，中序遍历序列重建二叉树
note: 假定无重复元素
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bintree_reconstruct(preorder, inorder):
    if not preorder and not inorder:
        return None
    if set(preorder) != set(inorder):
        return None
    i = inorder.index(preorder[0])
    root = TreeNode(preorder[0],
                    bintree_reconstruct(preorder[1:i+1], inorder[:i]),
                    bintree_reconstruct(preorder[i+1:], inorder[i+1:]))
    return root


if __name__ == '__main__':
    pre_list = [1, 2, 4, 7, 3, 5, 6,8]
    in_list = [4, 7, 2, 1, 5, 3, 8, 6]
    bintree_reconstruct(pre_list, in_list)
