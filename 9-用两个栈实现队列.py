"""
page 68, problem 9
RT
"""


class Solution:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, elem):
        self.stack1.append(elem)

    def pop(self):
        if not self.stack2:
            if not self.stack1:
                raise ValueError('the queue is full !')
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


if __name__ == '__main__':
    case = Solution()
    for i in range(10):
        case.push(i)
    for i in range(10):
        print(case.pop(), end=' ')
