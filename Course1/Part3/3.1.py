hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h > 40:
    overtimehrs = h - 40
    normalhrs = h - overtimehrs
    normalpay = normalhrs * r
    overtimerate = r * 1.5
    overtimepay = overtimehrs * overtimerate
    pay = normalpay + overtimepay

else:
    pay = h * r

print(pay)
