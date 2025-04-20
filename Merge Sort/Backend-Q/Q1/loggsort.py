from datetime import datetime

def merge(left, right):
    """تابع ادغام دو لیست مرتب‌شده"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        # تبدیل timestamp به شیء datetime برای مقایسه
        time_left = datetime.strptime(left[i]["timestamp"], "%Y-%m-%d %H:%M:%S")
        time_right = datetime.strptime(right[j]["timestamp"], "%Y-%m-%d %H:%M:%S")
        
        if time_left <= time_right:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # اضافه کردن باقی‌مانده‌های لیست‌ها
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sorted_logs(logs_list):
    """ادغام k لیست مرتب‌شده با الگوریتم Merge Sort"""
    if not logs_list:
        return []
    
    while len(logs_list) > 1:
        merged_logs = []
        
        for i in range(0, len(logs_list), 2):
            if i + 1 < len(logs_list):
                merged = merge(logs_list[i], logs_list[i + 1])
            else:
                merged = logs_list[i]
            merged_logs.append(merged)
        
        logs_list = merged_logs
    
    return logs_list[0]

# تست با داده‌های نمونه
server1_logs = [
    {"id": "A1", "timestamp": "2023-01-10 12:00:00"},
    {"id": "A2", "timestamp": "2023-01-10 12:05:00"}
]

server2_logs = [
    {"id": "B1", "timestamp": "2023-01-10 11:30:00"},
    {"id": "B2", "timestamp": "2023-01-10 12:15:00"}
]

server3_logs = [
    {"id": "C1", "timestamp": "2023-01-10 10:00:00"},
    {"id": "C2", "timestamp": "2023-01-10 13:00:00"}
]

result = merge_sorted_logs([server1_logs, server2_logs, server3_logs])
for log in result:
    print(f"{log['timestamp']} - {log['id']}")