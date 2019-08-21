# -*- coding: utf-8 -*-
# Author  : Mr.Lee Ji
# Email   : 470390366@qq.com
# Time    : 2019/8/21 1:17

'''
选择排序
从列表中寻找最大（最小）的数字
放在表头（表尾）依次循环
最优时间复杂度：O（n^2）
最坏时间复杂度：O（n^2）
平均时间复杂度：O（n^2）
稳定性：不稳定
'''


def select_sort(alist):
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(1+j,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j] , alist[min_index] = alist[min_index],alist[j]




if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    select_sort(li)
    print(li)