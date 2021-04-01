# Memoization is when cached version is returned\
# We want cache to live inside function

def memoize():
    cache = {}
    def closure(n): #Use closure to keep cache as function variable -> code efficiency
        if n in cache:
            print('cached')
            return cache[n]
        else:
            print('not cached')
            cache[n]=n+80
            return cache[n]
    return closure

memoized = memoize()
print('1',memoized(5))
print('2',memoized(6))
print('3',memoized(5))

# Fibonacci + DP
def fib(n): 
    if n<2:
        return n
    return fib(n-1)+fib(n-2)

def fibDynamic():
    cache = {}
    def fibClosure(n):
        if n in cache:
            print('cached')
            return cache[n]
        else:
            print('not cached yet')
            if n < 2:
                return n
            else:
                cache[n] = fibClosure(n-1)+fibClosure(n-2)
                return cache[n]
    return fibClosure
            
fasterFib = fibDynamic()
print(fasterFib(10))