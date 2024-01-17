#list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

mixed_list = [1, "hello", 3.14, ["another", "list"]]
print(type(mixed_list[-1][0]))

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

thislist = ["apple", "banana", "cherry"]
thislist[-1] = "blackcurrant"
print(thislist)

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.append(45)
fruits.append('sezal')
print(fruits)

#Append:
l1 =[10,20,30]
l2=[40,50,60]
l1.append(l2)
print(l1)

#Extend:
l1 =[10,20,30]
l2 =[40,50,60,45,'hello']
l1.extend(l2)
print(l1)

fruits = ['apple',  'banana', 'banana','cherry' ,1]
fruits.remove('cherry')
print(fruits) 
print(fruits.pop())
print(fruits.reverse())
print(fruits.sort())

#print(fruits.clear())
#del fruits
#print(fruits)


## tuple
a,b,c,e = 10,20,30,'hello'
d = a,b,c,e
print(d)
a,b,c,e = d
print(e)
print(list(d))

tuple1 = (0, 1, 2, 3)
tuple2 = ('python',4)
print(type(tuple2))
tuple3=tuple1 + tuple2
print(tuple3)
print(tuple3*3)

tuple1 = (0 ,'hello', 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:])

print(tuple('python45')) 

# Dict
my_dict = {'Name': 'mukesh','age':45,'City': 'chandigarh'}
print(my_dict)
print(my_dict['age'])

v = my_dict.values()
print(v)


# Set
THIS_is_set= {"apple", "banana", "cherry"}
print(THIS_is_set)

var = {"hello", "hey", "bye"}
var.add("good")
var.add(5)
var.add('H')
print(var)

f ={4,2,5,8,'hello'}
r = f.pop()
print(r)
print(f)

s = {1, 2, 3}
t = {3, 4, 5}
u = {5,2,8,4,7}
print(s.union(u))
print(t.intersection(s))

set1 = {"a", "b" , 3,"c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)