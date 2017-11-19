def computepay(hrs, rate):
    #return 42.37
    h = float(hrs)
    r = float(rate)

    if h <= 40:
        return h * r

    else:
        overtimehrs = h - 40
        normalhrs = h - overtimehrs
        normalpay = normalhrs * r
        overtimerate = r * 1.5
        overtimepay = overtimehrs * overtimerate
        return normalpay + overtimepay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs, rate)
print(p)
