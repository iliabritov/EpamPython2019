def collatz_steps(n, count=0):
    return (collatz_steps((n * 3 + 1 if n % 2
                           else n // 2), count=count + 1)) if n > 1 else count


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152
