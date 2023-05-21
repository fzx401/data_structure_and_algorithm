"""
插入排序算法：保证在前n个数字位置上是有序的，有序顺序为从前往后（冒泡是从后往前）
"""
class InsertSort:
    def __init__(self):
        pass

    @classmethod
    def insert_sort(cls, array):
        for i in range(1, len(array)):
            for j in range(i-1, -1, -1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                else:
                    break
        return array

print(InsertSort.insert_sort([4, 2, 5, 7, 3, 6, 1]))