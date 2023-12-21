def sort_array(array: list):
    swapped = False
    for i in range(len(array)):
        for k in range(0, len(array) - i - 1):
            if array[k] < array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
                swapped = True
        if not swapped:
            return
