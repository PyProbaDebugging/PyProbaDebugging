def partition(elements, low, high):
    pivot = elements[high]
    i = low - 1
    for j in range(low, high):
        if elements[j] < pivot:
            i += 1
            elements[i], elements[j] = elements[j], elements[i]
    elements[i + 1], elements[high] = elements[high], elements[i + 1]
    return i + 1

def quick_sort(elements, low=0, high=None):
    if high is None:
        high = len(elements) - 1
    if low < high:
        pivot_index = partition(elements, low, high)
        quick_sort(elements, low, pivot_index - 1)
        quick_sort(elements, pivot_index + 1, high)

if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [3, 1, 2],
        [5, 3, 8, 4, 2],
        [10, 7, 8, 9, 1, 5],
        [19, 22, 63, 105, 2, 46],
        [100, -50, 2, 3, 15, 0, 7],
        list(range(1000, 0, -1)),
        [1] * 100
    ]

    for test in test_cases:
        original_test = test.copy()
        quick_sort(test)
        assert test == sorted(original_test), f"Failed to sort the list {original_test}"
