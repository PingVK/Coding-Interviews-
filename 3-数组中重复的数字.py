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
        i = 0
        while i < len(self.lst):
            if self.lst[i] == i:
                i += 1
                continue
            j = self.lst[i]
            if self.lst[i] != self.lst[self. lst[i]]:
                self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
            else:
                return True
        return False


class Q2:
    def __init__(self, lst):
        self.lst = lst

    def s1(self):
        dic = dict()
        nums = []
        for i in self.lst:
            if i not in dic:
                dic[i] = 1
            else:
                if dic[i] == 1:
                    nums.append(i)
                dic[i] += 1
        return tuple(nums)


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 4, 5, 0], 'False, ()'),
        ([2, 3, 5, 4, 3, 2, 6, 7], 'True, (2, 3)')
    ]
    for case in cases:
        print('*'*20)
        print(case)
        q1 = Q1(case[0])
        q2 = Q2(case[0])
        print('Output:', str(q1.s1()), '\nExpected:', case[1], '\n')
        print('Output:', str(q2.s1()), '\nExpected:', case[1], '\n')
