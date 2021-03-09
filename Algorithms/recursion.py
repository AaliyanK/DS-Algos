counter = 0
def inception(counter):
    print(counter)
    if counter > 3:
        return print('done')
    counter += 1
    return inception(counter)

inception(counter)

# Factorial

def findFactRec(number):
    if number == 2:
        return 2
    return number * findFactRec(number-1)

def findFactIter(num):
    answer = 1
    for i in range(2,num+1,1):
        answer = answer * i
    return answer

print(f'{findFactIter(5)} ITERATIVE ANS')
print(f'{findFactRec(5)} Recursive ANS')

# Fibbonacci -> 0, 1, 1, 2, 3, 5, 8, 13, 21, 35...
            # n=0  1  2  3  4  5  6  7   8    9

def FibRecursive(n): # O(2^n) 
    if n < 2: # If we input the n = 0 or 1, just return the index
        return n
    return FibRecursive(n-1) + FibRecursive(n-2) # Adding last 2 numbers in sequence based on index

def FibIter(n):
    arr = [0,1]
    for i in range(2,n+1,1): #O(n) time complexity
        arr.append(arr[i-2]+arr[i-1])
    return arr[n]

print(f'{FibRecursive(8)} RECURSIVE FIB')
print(f'{FibIter(8)} Iterative FIB')

def reverseString(str):
    if str == '':
        return ''
    return reverseString(str[1::]) + str[0]

print(reverseString('aaliyan'))