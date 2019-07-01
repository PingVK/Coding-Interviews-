"""实现了一些链表结构"""


class LNode:
    """表结点"""
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    """自定义异常类"""
    pass


class LList:
    """单向链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """是否为空"""
        return self._head is None

    def prepend(self, elem):
        """表头插入数据"""
        self._head = LNode(elem, self._head)

    def pop(self):
        """弹出表头数据"""
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        """后端插入数据"""
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        """弹出尾部数据"""
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        if self._head.next is None:
            e = self._head.elem
            self._head = None
            return e
        p = self._head
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        """返回第一个满足条件的元素"""
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def print_all(self):
        """顺序打印链表"""
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print()


if __name__ == '__main__':
    link = LList()
    for i in range(10):
        link.append(i)
    link.print_all()
    print("第一个大于5的值：", link.find(lambda x: x > 5))
    link.prepend(10)
    print(link.pop())
    print(link.pop_last())
    link.print_all()
