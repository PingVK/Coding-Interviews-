class BinTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def left_child(self):
        return self._root.left

    def right_child(self):
        return self._root.right

    def set_root(self, root_node):
        self._root = root_node

    def set_left(self, left_child):
        self._root.left = left_child

    def set_right(self, right_child):
        self._root.right = right_child


#  递归遍历
def preorder(t):
    if t is None:
        return
    print(t.val, end=' ')
    preorder(t.left)
    preorder(t.right)


def inorder(t):
    if t is None:
        return
    inorder(t.left)
    print(t.val, end=' ')
    inorder(t.right)


def postorder(t):
    if t is None:
        return
    postorder(t.left)
    postorder(t.right)
    print(t.val, end=' ')


#  非递归遍历
def preorder_nonrec(t):
    s = list()
    while t is not None or s:
        while t is not None:
            yield t.val
            s.append(t.right)
            t = t.left
        t = s.pop()


def inorder_nonrec(t):
    s = list()
    while t is not None or s:
        if t:
            s.append(t)
            t = t.left
        else:
            t = s.pop()
            yield t.val
            t = t.right


def postorder_nonrec(t):
    s = list()
    while t is not None or s:
        while t is not None:
            s.append(t)
            t = t.left if t.left is not None else t.right
        t = s.pop()
        yield t.val
        if s and s[-1].left == t:
            t = s[-1].right
        else:
            t = None
