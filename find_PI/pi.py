iterations = int(input())
denomimator = float(1.0)
multiplier = float(1.0)
pi = 4 / denomimator
for i in range(iterations):
    denomimator += 2.0
    multiplier *= -1.0
    pi += ( (4.0 / denomimator) * multiplier )
    print(pi)
