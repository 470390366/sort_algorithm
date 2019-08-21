# -*- coding: utf-8 -*-
# Author  : Mr.Lee Ji
# Email   : 470390366@qq.com
# Time    : 2019/8/22 0:07

'''
希尔排序
相当于插入排序的变种
用步长去将表分为若干份
进行插入比较
依次下降步长循环
最优时间复杂度：O（n）步长不同，复杂度不同
最坏时间复杂度：O（n^2）
稳定性：不稳定
'''


def shell_sort(alist):
    n = len(alist)
    gap = n//2
    while gap>0 :
        #插入排序
        for i in range(gap,n):
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break

        gap//=2







if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    shell_sort(li)
    print(li)