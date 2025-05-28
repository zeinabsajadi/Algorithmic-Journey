def partition(arr, low, high):
    pivot = arr[high]  # از آخر به عنوان pivot استفاده می‌کنیم
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # جا به جا کردن

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # مکان نهایی pivot

def quick_sort_iterative(arr):
    stack = []

    # ابتدا کل بازه آرایه رو توی پشته می‌ریزیم
    stack.append((0, len(arr) - 1))

    while stack:
        low, high = stack.pop()

        if low < high:
            pi = partition(arr, low, high)

            # دو بخش جدا شده رو به پشته اضافه می‌کنیم
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

    return arr
