def is_prime(num):
    if num == 2:
        return True
    elif (num % 2) == 0 and num > 2:
        return False
    else:
        for i in range(
            2, int(num**0.5) + 1
        ):  # Range started from 2 and end with the SQRT of the number +1
            if (num % i) == 0:
                return False
    return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
