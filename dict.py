#Dict
d = {1: 'one',
     2: 'two'}

d2 = {'a': [1, 2, 3],
      'b': 'A String'}

#Use print to see output

#Dictionaries
state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}
#Value Refers To Key
ca_capital = state_capitals['California']
print(ca_capital)

#Loops Using Values As Key 
for k in state_capitals.keys():
 print('{} is the capital of {}'.format(state_capitals[k], k))