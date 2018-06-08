# Paste your function here
def closest_power(base, num):
    if num < base:
        return 0
    i = 2

    diff = num - base**i
    while True:
        if diff > 15:
            i += 1
            diff = num - base**i
            
        else:
            if abs(num - base**i)  < abs(num - base**(i-1)):
                return i
            else:
                return i-1
                
assert closest_power(2,192.0) == 7
assert closest_power(5,375.0) == 3
assert closest_power(20,210.0) == 1
assert closest_power(4,160.0) == 3
assert closest_power(15,8.0) == 0
assert closest_power(16, 136.0) == 1
assert closest_power(45,1) == 0
assert closest_power(10,550.0) == 2
assert closest_power(7, 196.0) == 2
assert closest_power(11, 66.0) == 1
assert closest_power(4, 62) == 3
assert closest_power(5,22) == 2
assert closest_power(9,75) == 2
assert closest_power(9,70) == 2

