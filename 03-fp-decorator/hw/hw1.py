from functools import reduce


# problems 9
def problem9():
    return [a * b * (1000 - a - b) for a in range(1, 1001) for b in range(a+1, 1001) if a ** 2 + b ** 2 == (1000 - a - b) ** 2][0]
    

# problems 6                
def problem6(nums):
    return sum(nums) ** 2 - sum([i ** 2 for i in nums])


# problem 48
def problem48():
    return sum([i ** i for i in range(1,1001)]) % 10 ** 10

# problem 40
def problem40(args):
    return reduce((lambda x, y : int(x)*int(y)), [''.join(str(i) for i in range(1, args[-1]))[i-1] for i in args])


# results
print(problem6([i for i in range(101)]))
print(problem9())
print(problem48())
print(problem40([1,10,100,1000,10000,100000,1000000]))

