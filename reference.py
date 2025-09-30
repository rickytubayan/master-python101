#Reference Assignment

# "a_tool" is now a name for the reference to the object "an_electric_lawnmower"

a_tool = 'an_electric_lawnmower'

#Multiple Variable Assignment

a, b, c = 1, 2, 3

print(a, b, c)

#Unwanted Values Assignment

a, b, _ = 1, 2, 3 

print(a,b)

#Multiple Variables Single Value

a = b = c = 10

print (a,b,c)

#Cascade Values Assignment

a = b = c = 20

print (a,b,c)

b = 100

print (a,b,c)

#Immutable types (int,str,tuple)

x = v = [7, 8, 9]
x = [13, 8, 9]
print(v)

#Modifying Object Refers To Assigned Values

x = v = [7, 8, 9]
x[0] = 50
print(x)