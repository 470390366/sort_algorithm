# -*- coding: utf-8 -*-
# Author  : Mr.Lee Ji
# Email   : 470390366@qq.com
# Time    : 2019/8/22 13:36


'''
归并排序算法
将列表每次拆分一般
直到拆成单一元素
再将每层排序合并
逐层向上排序合并
递归思想
最优时间复杂度：O（nlogn）
最坏时间复杂度：O（nlogn）
稳定性：稳定
'''


def merge_sort(alist):
    n = len(alist)
    if n <= 1 :
        return alist
    mid = n//2
    # left 采用归并排序后形成的有序的新列表
    left_li = merge_sort(alist[:mid])
    # right 采用归并排序后形成的有序的新列表
    right_li = merge_sort(alist[mid:])
    # 将两个两个有序的子序列合并为一个新的整体
    # merge_sort(left,right)
    left_pointer = 0
    right_pointer = 0
    result = []
    while left_pointer<len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer]<= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer+=1
        else:
            result.append(right_li[right_pointer])
            right_pointer+=1
    result+=left_li[left_pointer:]
    result+=right_li[right_pointer:]
    return result










if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    sorted_li = merge_sort(li)
    print(sorted_li)