مسئله:
لاگ‌های چندین سرور (به صورت لیست‌های جداگانه) دارید که باید بر اساس timestamp ادغام و مرتب شوند.

def merge_sorted_logs(logs_list):
    # ادغام لیست‌های مرتب‌شده با Merge Sort
    pass

# مثال:
server1_logs = [{"id": "A1", "timestamp": "2023-01-10 12:00:00"}, ...]
server2_logs = [{"id": "B1", "timestamp": "2023-01-10 11:30:00"}, ...]
print(merge_sorted_logs([server1_logs, server2_logs]))

تحلیل:

پیچیدگی: O(n log k) (k = تعداد سرورها).

کاربرد: جمع‌آوری لاگ‌های توزیع‌شده در سیستم‌های میکروسرویس.