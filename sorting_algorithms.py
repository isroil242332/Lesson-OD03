def bubble_sort(arr):
    """
    Сортировка пузырьком - простой алгоритм, который многократно
    проходит по списку, сравнивая соседние элементы и меняя их местами.
    """
    n = len(arr)
    for i in range(n):
        # Флаг для оптимизации - если за проход не было обменов, массив отсортирован
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если не было обменов, выходим досрочно
        if not swapped:
            break
    return arr



def selection_sort(arr):
    """
    Сортировка выбором - на каждом проходе находим минимальный элемент
    и помещаем его в начало неотсортированной части.
    """
    n = len(arr)
    for i in range(n):
        # Находим индекс минимального элемента в неотсортированной части
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем местами найденный минимальный элемент с первым неотсортированным
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr



def insertion_sort(arr):
    """
    Сортировка вставками - каждый следующий элемент вставляется
    в правильную позицию в уже отсортированной части массива.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Сдвигаем элементы большие key вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(arr):
    """
    Быстрая сортировка - алгоритм 'разделяй и властвуй'.
    Выбираем опорный элемент и разделяем массив на элементы меньше и больше опорного.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Выбираем средний элемент как опорный
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Альтернативная реализация in-place
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Индекс разделения
        pi = partition(arr, low, high)

        # Рекурсивно сортируем элементы до и после разделения
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

    return arr


def partition(arr, low, high):
    """
    Вспомогательная функция для быстрой сортировки in-place.
    """
    pivot = arr[high]  # Опорный элемент
    i = low - 1  # Индекс меньшего элемента

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def merge_sort(arr):
    """
    Сортировка слиянием - алгоритм 'разделяй и властвуй'.
    Разделяем массив пополам, сортируем каждую половину и сливаем обратно.
    """
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две половины
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Сливаем отсортированные половины
    return merge(left, right)


def merge(left, right):
    """
    Вспомогательная функция для слияния двух отсортированных массивов.
    """
    result = []
    i = j = 0

    # Сливаем, пока в обоих массивах есть элементы
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def test_sorting_algorithms():
    # Тестовые данные
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1],
        [],
        [3, 3, 3, 3],
        [5, -1, 0, -8, 2]
    ]

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort
    }

    for name, algorithm in algorithms.items():
        print(f"\n{name}:")
        for i, arr in enumerate(test_arrays):
            test_arr = arr.copy()  # Создаем копию для тестирования
            sorted_arr = algorithm(test_arr.copy()) if name != "Quick Sort" else algorithm(test_arr)
            print(f"  Тест {i + 1}: {arr} -> {sorted_arr}")


if __name__ == "__main__":
    test_sorting_algorithms()