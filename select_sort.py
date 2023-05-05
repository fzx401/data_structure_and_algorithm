class SelectSort:
    def __init__(self):
        pass

    @staticmethod
    def select_sort(array):
        for i in range(len(array) - 1):
            min_vaule = array[i]
            for j in range(i+1, len(array)):
                if array[j] < min_vaule:
                    array[i], array[j] = array[j], array[i]
                    min_vaule = array[j]
        return array

print(SelectSort.select_sort([7, 3, 2, 1, 4, 2, 10, 0]))

