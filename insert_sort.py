# -*- coding: utf-8 -*-
# Author  : Mr.Lee Ji
# Email   : 470390366@qq.com
# Time    : 2019/8/21 23:21

'''
插入排序
将列表元素与表头（表尾）元素比较
然后组成有序数列
依次循环
最优时间复杂度：O（n）
最坏时间复杂度：O（n^2）
平均时间复杂度：O（n^2）
稳定性：稳定
'''



def insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        # for j in range(i,0,-1): for 循环一样可以实现
        while i>0: #将元素插入到有序的序列中
            if alist[i] <alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i-=1
            else:
                break



if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    insert_sort(li)
    print(li)