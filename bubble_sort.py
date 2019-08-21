# -*- coding: utf-8 -*-
# Author  : Mr.Lee Ji
# Email   : 470390366@qq.com
# Time    : 2019/8/21 0:44

'''
冒泡排序
列表从头（尾）俩个元素
依次比较排放
依次循环
最优时间复杂度：O（n）
最坏时间复杂度：O（n^2）
平均时间复杂度：O（n^2）
稳定性：稳定
'''

def bubble_sort(alist):

    n = len(alist)
    for j in range(n-1):
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]



if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    bubble_sort(li)
    print(li)