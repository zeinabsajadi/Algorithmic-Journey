def insert_order(sorted_orders, new_order):
    sorted_orders.append(new_order)  # اضافه کردن سفارش جدید به انتهای لیست
    i = len(sorted_orders) - 2  # شروع از عنصر قبل از آخر
    
    # جابجایی سفارش جدید به جایگاه صحیح
    while i >= 0 and sorted_orders[i] > new_order:
        sorted_orders[i + 1] = sorted_orders[i]  # جابجایی به راست
        i -= 1
    
    sorted_orders[i + 1] = new_order  # درج نهایی
    return sorted_orders

# تست
orders = [100, 250, 400]  # لیست مرتب‌شده
new_order = 300
print(insert_order(orders, new_order))  # خروجی: [100, 250, 300, 400]