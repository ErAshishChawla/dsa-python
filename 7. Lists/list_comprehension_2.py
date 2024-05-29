my_list = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
print(my_list)

my_list = [f"{i} - even" if i % 2 == 0 else f"{i} - odd" for i in range(1, 11)]
print(my_list)

my_list = [i for i in range(1, 51) if i % 5 == 0 and i % 4 == 0]
print(my_list)


def isPrime(num: int) -> bool:
    factor_count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factor_count += 1
    return factor_count == 2


my_list = [i for i in range(1, 100) if isPrime(i)]
print(my_list)
