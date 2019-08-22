# -*- coding: utf-8 -*-
# Author  : Mr.Lee Ji
# Email   : 470390366@qq.com
# Time    : 2019/8/22 15:04

'''
二分查找
有序数列
最优时间复杂度：O（1）
最坏时间复杂度：O（logn）
'''

def binary_search_merge(alist,item):
    '''递归版本'''
    n = len(alist)
    if n > 0:
        mid = n//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search_merge(alist[:mid],item)
        else:
            return binary_search_merge(alist[mid+1:],item)
    return False


def binary_search_nomerge(alist,item):
    '''非递归版本'''
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid-1
        else:
            first = mid +1
    return False

if __name__ == '__main__':
    li = [17,20,26,31,44,54,55,77,93]
    print(binary_search_merge(li,55))
    print(binary_search_merge(li,100))
    print('****************************')
    print(binary_search_nomerge(li, 55))
    print(binary_search_nomerge(li, 100))