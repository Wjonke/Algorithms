"""
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
​
​
cache = {0: 1, 1: 1}
def rec_fib(n):
    # base cases
    # if n == 0:
    #     return 1
    # if n == 1:
    #     return 1
    if n in cache:
        return cache[n]
​
    # if it's not in the cache, we must
    n_minus_1 = rec_fib(n-1)
    n_minus_2 = rec_fib(n-2)
    cache[n] = n_minus_1 + n_minus_2
​
    return cache[n]
​
​
print(rec_fib(999))
​
print(rec_fib(1000))
​
# Do more stuff here

"""

'''
Eating cookies whiteboard:
n = 1
1. 1 cookie 1 time
n = 2
1. 1 cookie 1 time 1 cookie 1 time
2. 2 cookie 1 time
n = 3
1. 1 cookie 1 time 1 cookie 1 time 1 cookie 1 time
2. 2 cookie 1 time 1 cookie 1 time
3. 1 cookie 1 time 2 cookie 1 time
4. 3 cookie 1 time
n = 4
1. 1 cookie 1 time 1 cookie 1 time 1 cookie 1 time 1 cookie
2. 2 cookie 1 time 1 cookie 1 time 1 cookie
3. 1 cookie 1 time 2 cookie 1 time 1 cookie
4. 3 cookie 1 time 1 cookie
1. 1 cookie 1 time 1 cookie 1 time 2 cookie
2. 2 cookie 1 time 2 cookie
1. 1 cookie 1 time 3 cookie
n = 5
1. 1 cookie 1 time 1 cookie 1 time 1 cookie 1 time 1 cookie 1 cookie
2. 2 cookie 1 time 1 cookie 1 time 1 cookie 1 cookie
3. 1 cookie 1 time 2 cookie 1 time 1 cookie 1 cookie
4. 3 cookie 1 time 1 cookie 1 cookie
1. 1 cookie 1 time 1 cookie 1 time 2 cookie 1 cookie
2. 2 cookie 1 time 2 cookie 1 cookie
1. 1 cookie 1 time 3 cookie 1 cookie
1. 1 cookie 1 time 1 cookie 1 time 1 cookie 1 time 2 cookie
2. 2 cookie 1 time 1 cookie 1 time 2 cookie
3. 1 cookie 1 time 2 cookie 1 time 2 cookie
4. 3 cookie 1 time 2 cookie
1. 1 cookie 1 time 1 cookie 1 time 3 cookie
2. 2 cookie 1 time 3 cookie

'''