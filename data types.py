# String
a ='who "is" this'
b ="who 'is' this"
c ='''who is 
this '''
print(a)
print(b)
print(c)
d = "who \"is\" this"
e = 'who \'is\' this'
f = "who 'is' this \"doesn't\" "
g = 'who \'is\' this "doesn\'t" '
print(d)
print(e)
print(f)
print(g)

print(a+b)
print(a*3)
print(a,b)

print('C:\some\name')
print(r'C:\some\name')

a ="hello"
print(a[-1])
print(len(a))
print(a[2])
print(a[ : :2])
print(a[ : :-1])
print(a[ 4: :-1])
print(a[ 4: 0:-1])
print(a[ :2])

s = " Hello, World! " 
print(len(s))

x = s.strip()
print(x,len(x))

txt = ",,,,,rrttgg.....banana.,...rrr,,"
x = txt.strip(",rtg.")
print(x)

s = "HELLO WORLD !"
d =s.lower()
print(d)

print(d.upper())

s= "herllo world!"
print(s.replace('l','m'))

txt = "welcome to the jungle"
x = txt.split()
print(x)

print(" ".join(["hello","world","bye" ]))

s ="heleo"
print(s.count("e"))

name ="python"
salary = 4523.2

print(f" your name is {name}  and your salary is {salary} salary")

a =input("")
b= ord(a)
print(b)
