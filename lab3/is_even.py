def is_even(num):
    return num % 2 == 0


num = 6
result = is_even(num)
if result:
    print(num, "is even.")
else:
    print(num, "is not even.")