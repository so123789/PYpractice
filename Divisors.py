def divisors_brute(n):
    result = []
    print("Brute Force Divisors:")
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

print(divisors_brute(12))


def divisors_optimized(n):
    result = []
    print("Optimized Divisors:")
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:  # Avoid adding the square root twice
                result.append(n // i)
    return sorted(result)
    
print(divisors_optimized(15))