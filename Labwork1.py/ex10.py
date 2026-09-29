def print_divisors(n):
    print(f"Divisors of {n}:", end=" ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()

num = int(input("Enter a number: "))
print_divisors(num)