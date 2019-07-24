def move(a, b):
    print('%s --> %s' % (a, b))


def hanoi(n, x='x', y='y', z='z'):
    if n == 1:
        move(x, z)
    else:
        hanoi(n-1, x, z, y)  # 将前n-1个盘子从x移动到y上
        move(x, z)  # 将最底下的盘子从x移动到z上
        hanoi(n-1, y, x, z)  # 将y上的n-1个盘子移动到z上


hanoi(5)
