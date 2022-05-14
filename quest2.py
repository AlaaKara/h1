x=int(input('enter a decimal number:'))
resu=[]
while x>0:
    resu.append(x%2)
    x//=2
resu.reverse()
print('the matching binary number is:',resu)
