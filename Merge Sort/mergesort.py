def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # لیست‌های با صفر یا یک عنصر، خودشون مرتب هستن

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # ترکیب دو لیست مرتب شده
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # اضافه کردن باقی‌مانده‌ها (اگر یکی تموم بشه)
    result.extend(left[i:])
    result.extend(right[j:])

    return result
