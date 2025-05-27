#سوال:
#محاسبه باقی مانده اعداد توان دار با پیچیدگی زمانی o(logn)
# به روش تقسیم و حل

def mod_exp(x, n, p):
    if n == 0:
        return 1
    half = mod_exp(x, n // 2, p)
    half = (half * half) % p
    if n % 2 == 0:
        return half
    else:
        return (x * half) % p



# درخت بازگشت:
""" 
اگر بخواهیم حاصل 2 به توان 5 را محاسبه کنیم و باقی مانده ان در تقسیم بر 13 را بدست اوریم:
mod_exp(2, 5, 13)
    └── mod_exp(2, 2, 13)
          └── mod_exp(2, 1, 13)
                └── mod_exp(2, 0, 13) → 1
                ← returns: 2
          ← returns: 4
    ← returns: 6
"""