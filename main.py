import math

# 1
n = int(input("value for n: "))
x = int(input("value for x: "))

terms = lambda n, x, i: (n ** i) / math.factorial(i)
series = [terms(n, x, i) for i in range(x + 1)]
result = sum(series)

print("Result: ", result)

k = 1
result = 0


# 2
def calculate_sum(n):
    global sum_result
    if n == 1:
        sum_result = -1
    else:
        sum_result = 0
        calculate_sum(n - 1)
        sum_result += ((-1) ** (n + 1)) / n


sum_result = 0
calculate_sum(n)
print(sum_result)
