n = int(input())
first = 0
second = 1
for i in range(n + 1):
    result = first + second
    first = second
    second = result
    print(result)
