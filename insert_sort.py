class InsertSort:
    def __init__(self):
        pass

    @classmethod
    def insert_sort(cls, array):
        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                j = i - 1
                if j >= 0:
                    if array[j] < array[j+1]:
                        InsertSort.swap(array[i], array[j])
                        j -= 1

    @classmethod
    def swap(cls, a, b):
        a, b = b, a
        return a, b
