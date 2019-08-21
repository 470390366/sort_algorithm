# -*- coding: utf-8 -*-
# Author  : Mr.Lee Ji
# Email   : 470390366@qq.com
# Time    : 2019/8/22 1:40

'''
快速排序
根据列表 左右两个游标 low high 对列表进行分割
每次拿列表第一个元素 与 low high 的元素大小进行比较
根据比较结果来决定 low high 元素的对调
逐渐缩短low 与 high 的范围
当low 与high 重合时
将第一个元素放入列表的low（high）的位子
然后将列表分为两部分 分别进行以上步骤
进行 递归操作
最优时间复杂度：O（nlogn）步长不同，复杂度不同
最坏时间复杂度：O（n^2）
稳定性：不稳定
'''


def quick_sort(alist,first,last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high =last
    while low <high:
        #high 左移
        while low < high and alist[high] >= mid_value:
            high-=1
        alist[low] = alist[high]
        #low 右移
        while low < high and alist[low] < mid_value:
            low+=1
        alist[high] = alist[low]
    #循环退出时，low=high
    alist[low] = mid_value
    # 对low 左边的列表进行快排排序
    quick_sort(alist,first,low-1)
    # 对low 右边的列表进行快排排序
    quick_sort(alist,low+1,last)








if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)