number = int(input("Enter a number? "))
divisors_sum = sum(i for i in range(1, number) if number % i == 0)
if number > 1 and divisors_sum == number:
    print(f"(number) is a perfect number")
else:
    print(f"(number) is a NOT perfect number")