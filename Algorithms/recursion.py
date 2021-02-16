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

# Fibbonacci