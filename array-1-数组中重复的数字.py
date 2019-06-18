"""
page 39 ，problem 3
Q1:找出数组中重复的数字
Q2:不修改数组找出重复的数字
"""


class Q1:
    def __init__(self, lst):
        self.lst = lst

    def s1(self) -> bool:
        # 时间复杂度n，空间复杂度1
        for i in range(len(self.lst)):
            if self.lst[i] == i:
                continue
            if self.lst[i] != self.lst[self.lst[i]]:
                self.lst[i], self.lst[self.lst[i]] = self.lst[self.lst[i]], self.lst[i]
            else:
                return True
        return False

    def s2(self) -> bool:
        # 只能判断
        s = sum(range(len(self.lst)))
        count = 0
        for i in self.lst:
            count += i
        return True if count != s else False


class Q2:
    def __init__(self, lst):
        self.lst = lst

    def s1(self):
        def countRange(lst, start, end):
            count = 0
            for i in lst:
                if start <= i <= end:
                    count += 1
            return count

        start,  end = 0, len(self.lst)-1
        while end >= start:
            middle = (end + start) // 2 + start
            count = countRange(self.lst, start, middle)
            if end == start:
                if count > 1:
                    return start
                else:
                    break
            if count > end - start + 1:
                end = middle
            else:
                start = middle + 1
        return -1


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 4, 5, 0], 'False, -1'),
        ([2, 3, 5, 4, 3, 2, 6, 7], 'True, 2, 3')
    ]
    for case in cases:
        q1 = Q1(case[0])
        q2 = Q2(case[0])
        print('Output:', str(q1.s1()), '\t\t', 'Expected:', case[1])
        print('Output:', str(q1.s2()), '\t\t', 'Expected:', case[1])
        print('Output:', str(q2.s1()), '\t\t', 'Expected:', case[1])


