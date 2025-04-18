from datetime import datetime

def insertion_sort_users(users):
    for i in range(1, len(users)):  # حلقه از عنصر دوم شروع می‌شود
        key = users[i]  # ذخیره کاربر فعلی برای درج
        j = i - 1  # شروع مقایسه با عنصر قبل
        
        # مقایسه تاریخ‌ها و جابجایی عناصر بزرگ‌تر
        while j >= 0 and datetime.strptime(users[j]["join_date"], "%Y-%m-%d") > datetime.strptime(key["join_date"], "%Y-%m-%d"):
            users[j + 1] = users[j]  # جابجایی به راست
            j -= 1  # حرکت به چپ
        
        users[j + 1] = key  # درج کاربر در جایگاه صحیح
    return users

# تست
users = [
    {"id": 1, "name": "Alice", "join_date": "2023-01-15"},
    {"id": 2, "name": "Bob", "join_date": "2022-11-20"},
    {"id": 3, "name": "Charlie", "join_date": "2023-03-10"}
]
sorted_users = insertion_sort_users(users)
print(sorted_users)