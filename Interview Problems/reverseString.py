strEx = 'Hi my name is bumba'

if type(strEx) is not str or len(strEx) < 2:
    print('BAD')
else: 
    bckwds = []
    print(len(strEx)-1)
    for i in range(len(strEx)-1,-1,-1):
        bckwds.append(strEx[i])
    print(bckwds)
final = ''.join(bckwds)
print(final)

# Second solution

Ex = 'Hi my name is bumba'
New = Ex[::-1]
print(New)