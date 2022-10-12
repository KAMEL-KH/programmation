# nbr = int(input('Entrez un nombre : '))
# fact = 1
# for i in range(1, nbr+1):
#   fact = fact * i
# print (nbr,' = ',fact)

# 

def somme(n):
if n // 10 == 0:
return n.
else:
return n % 10 + somme( n // 10 )
print( somme (5425) )
