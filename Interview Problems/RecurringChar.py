# First solution:

def firstRec(input):
    for i in range(0,len(input),1):
        for j in range(1,len(input),1):
            if input[i] == input[j]:
                return input[i]
    return None

# O(n^2)

print(firstRec([2,5,1,1,3,5,1,2,4]))


def firstRec2(input):
    # Add each value to dictionary -> Use unique keys

    map = {}
    for i in range(0,len(input),1):
        if input[i] in map:
            return input[i]
        else:
            map[input[i]] = i
    print(map)
    return None

print(firstRec2([2,5,3,1,3,5,1,2,4]))

# O(n) -> Decreased time complexity
# Increased space complexity -> Created new dictionary
# Worst case is that it loops over entire item list