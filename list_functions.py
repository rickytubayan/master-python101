#List Names
names = ['Sierra','India','Juliet','Kilo','Lima']
#List Append
names.append('Mike')
print(names)
#List Insert Next To Index Number 
names.insert(1, 'November')
print(names)
#List Remove
names.remove('Sierra')
print(names)

#Length of List
print(len(names))

#Count Occurrence Of Items In List
c = [1,1,3,3,3,3,5,4,7,8,8,9] 
print(c.count(3))

#Reverse a List
r = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(r[::-1])