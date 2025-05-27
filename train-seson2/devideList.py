def divide_list(arr):
    arr.sort(reverse=True)  # مرتب‌سازی نزولی
    group1 = []
    group2 = []
    sum1 = sum2 = 0

    for num in arr:
        if sum1 <= sum2:
            group1.append(num)
            sum1 += num
        else:
            group2.append(num)
            sum2 += num
    return group1, group2

