"""
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""

even_fibonacci_numbers = []


def calculate_fib(n):
    """iterateive approach"""
    a, b = 0, 1
    while a < n:
        if a % 2 == 0:
            even_fibonacci_numbers.append(a)
        a, b = b, a + b


def solution():
    calculate_fib(4000000)
    final_sum = sum(even_fibonacci_numbers)

    print(f"{final_sum=}")


if __name__ == "__main__":
    solution()
