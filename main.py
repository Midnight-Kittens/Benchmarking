
'''
1st iteration. Very simple Fibonacci program to set a baseline
*NOTE* n = 20 was used for these initial runs. Larger numbers will be used later to test memoization
'''
def fibonacci1(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
          return 0

    elif n == 1:
          return 1

    elif n == 2:
          return 1
     
    else:
          return fibonacci1(n-1) + fibonacci1(n-2)

## Results: 0.0022017955780029297 seconds
##          0.001934051513671875 seconds
##          0.00222015380859375 seconds

'''
2nd iteration. Combining n == 1 and n == 2 lines
'''
def fibonacci2(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
         return 0
    elif n == 1 or n == 2:
         return 1
    else:
         return fibonacci2(n-1) + fibonacci2(n-2)

## Results: 0.002237081527709961 seconds
#           0.0017027854919433594 seconds
#           0.0022208690643310547 seconds


fib_array = [0, 1]
def fibonacci3(n):
    if n < 0:
        print("Incorrect input")

    elif n < len(fib_array):
        return fib_array[n]
    else:
        fib_array.append(fibonacci3(n-1) + fibonacci3(n-2))
        return fib_array[n]

## Results: 1.2874603271484375e-05 seconds
##          1.5974044799804688e-05 seconds
##          1.621246337890625e-05 seconds


def fibonacci4(n):
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input")
    
    elif n == 0:
        return 0

    elif n == 1:
        return b
    
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

    
 """
 Final sequence using memoization. This is the big one
 """

fib_cache = {}
def fibonacci5(n):
    if n in fib_cache:
        return fib_cache[n]
    elif n < 0:
        print("Incorrect input")
    elif n == 0:
         return 0
    elif n == 1 or n == 2:
         return 1
    elif n > 2:
        value = fibonacci5(n-1) + fibonacci5(n-2)

    fib_cache[n] = value
    return value





if __name__ == "__main__":
    import time
    # start = time.time()
    # fibonacci1(20)
    # end = time.time()
    # print(f"Time consumed by fib1: {end - start} seconds")

    # start = time.time()
    # fibonacci2(20)
    # end = time.time()
    # print(f"Time consumed by fib2: {end - start} seconds")

    # start = time.time()
    # fibonacci3(20)
    # end = time.time()
    # print(f"Time consumed by fib3: {end - start} seconds")

    # start = time.time()
    # fibonacci4(20)
    # end = time.time()
    # print(f"Time consumed by fib4: {end - start} seconds")

    start = time.time()
    for n in range(1, 1001):
        print("Time in seconds: ", fibonacci5(n))
    end = time.time()
    print(f"Time consumed by fib5: {end - start} seconds")
