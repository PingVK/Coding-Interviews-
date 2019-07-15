"""
一些排序算法的实现
"""


from random import randint


registry = []
def register(func):
    registry.append(func)
    return func


@register
def bubble_sort(lst):
    """冒泡排序"""
    for i in range(len(lst)-1):
        found = False
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                found = True
        if not found:
            break


@register
def insert_sort(lst):
    """插入排序"""
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x


@register
def select_sort(lst):
    """选择排序"""
    for i in range(len(lst)-1):
        x = i
        for j in range(i, len(lst)):
            if lst[j] < lst[x]:
                x = j
        if i != x:
            lst[i], lst[x] = lst[x], lst[i]


@register
def heap_sort(lst):
    """堆排序"""
    def siftdown(elems, e, begin, end):
        i, j = begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] > elems[j]:
                j += 1
            if e > elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e

    length = len(lst)
    for i in range(length//2, -1, -1):
        siftdown(lst, lst[i], i, length)
    for i in range(length-1, 0, -1):
        e = lst[i]
        lst[i] = lst[0]
        siftdown(lst, e, 0, i)


@register
def quick_sort1(lst):
    """快速排序"""
    def qsort_rec(lst, l, r):
        if l >= r:
            return
        i, j = l, r
        pivot = lst[i]
        while i < j:
            while i < j and lst[j] >= pivot:
                j -= 1
            if i < j:
                lst[i] = lst[j]
                i += 1
            while i < j and lst[i] <= pivot:
                i += 1
            if i < j:
                lst[j] = lst[i]
                j -= 1
        lst[i] = pivot
        qsort_rec(lst, l, i-1)
        qsort_rec(lst, i+1, r)
    qsort_rec(lst, 0, len(lst)-1)


@register
def quick_sort2(lst):
    """快速排序"""
    def qsort_rec(lst, begin, end):
        if begin >= end:
            return
        i = begin
        for j in range(begin+1, end+1):
            if lst[j] < lst[begin]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[begin], lst[i] = lst[i], lst[begin]
        qsort_rec(lst, begin, i-1)
        qsort_rec(lst, i+1, end)
    qsort_rec(lst, 0, len(lst)-1)


@register
def merge_sort(lst):
    """归并排序"""
    def merge(ifrom, ito, low, mid, high):
        i, j, k = low, mid, low
        while i < mid and j < high:
            if ifrom[i] <= ifrom[j]:
                ito[k] = ifrom[i]
                i += 1
            else:
                ito[k] = ifrom[j]
                j += 1
            k += 1
        while i < mid:
            ito[k] = ifrom[i]
            i += 1
            k += 1
        while j < high:
            ito[k] = ifrom[j]
            j += 1
            k += 1

    def merge_pass(ifrom, ito, llen, slen):
        i = 0
        while i+2*slen < llen:
            merge(ifrom, ito, i, i+slen, i+2*slen)
            i += 2*slen
        if i+slen < llen:
            merge(ifrom, ito, i, i+slen, llen)
        else:
            for j in range(i, llen):
                ito[j] = ifrom[j]

    slen, llen = 1, len(lst)
    temp_list = [None]*llen
    while slen < llen:
        merge_pass(lst, temp_list, llen, slen)
        slen *= 2
        merge_pass(temp_list, lst, llen, slen)
        slen *= 2


if __name__ == '__main__':
    case = [randint(-50, 49) for x in range(10)]
    print(case)
    sorted_case = sorted(case)
    print(sorted_case)
    for algorithm in registry:
        case_copy = case[:]
        algorithm(case_copy)
        print('%11s: %r%10r' % (algorithm.__name__, case_copy, case_copy == sorted_case))
