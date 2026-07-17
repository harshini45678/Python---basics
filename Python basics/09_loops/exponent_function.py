def power_of_number(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result
print(power_of_number(5,3))