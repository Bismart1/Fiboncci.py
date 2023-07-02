def find_fibonacci_index(divisor):
    fib_sequence = [0, 1]
    index = 2
    while True:
        fib_num = fib_sequence[index - 1] + fib_sequence[index - 2]
        if fib_num % divisor == 0 and fib_num != 0:
            return index
        fib_sequence.append(fib_num)
        index += 1
num_test_cases = int(input())
for _ in range(num_test_cases):
    divisors = list(map(int, input().split()))
    indices = []
    for divisor in divisors:
        index = find_fibonacci_index(divisor)
        indices.append(index)
    print(*indices, end=" ")
