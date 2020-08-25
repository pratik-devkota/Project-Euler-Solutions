import time
start_time = time.time()
palindromes = []
for i in range(1000, 10000):
    for j in range(1000, 10000):
        k = i * j
        if str(k) == str(k)[::-1]:
            palindromes.append(k)
palindromes.sort()
print(palindromes[-1])
print(f"Program executed in {time.time() - start_time}s.")