
"""
참고 : Escape Code
\n : a new line
\t : tap
\\ : String
\' : String
\" : String 
\000 : Null Character
"""

#print

print('Python Start!')
print("Python Start!")
print("""Python Start!""")
print('''Pyhton Start!''')

print()

# separator_option
print('P','Y','T','H','O','N', sep=' ')
print('010','1234','5678', sep = '-')
print('7rieden','gmail.com', sep = '@')

print()

#end_option
print('Welcome to', end = ' ')
print('Python', end = ' ')
print('World')

print()

#file_option
import sys
print('Learning Python', file=sys.stdout)

print()

#format_option
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one', 'two')) # two one

# %s
print('%10s' % ('nice',))
print('{:>10}'.format('nice'))
print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice')) #------nice
print('{:_<10}'.format('nice')) #nice------

print('{:^10}'.format('nice')) # center alignment

print('%5s' % ('nice')) #nice-
print('%.5s' % ('nice')) #-nice

print('%.5s' % ('slicing')) #slici
print('{:10.5}'.format('slicing')) #slici-----

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42)) #--42
print('%4d' % (42123123123))

print('{:4d}'.format(42)) #--42

# %f
print('%f' % (3.141592653589793)) #3.141593 (6 places of decimals)
print('{:f}'.format(3.141592653589793))

print('%1.8f' % (3.141592653589793))

print('%06.2f' % (3.141592653589793)) # 2nd decimal places in 6 digit = 003.14
print('{:06.2f}'.format(3.141592653589793))

print('%05.2f' % (3.141592653589793)) # 2nd decimal places in 5 digit = 03.14
print('{:05.2f}'.format(3.141592653589793))
print()

#Chapter02-2
n = 700
print(n)

x = y = z =700
print(x, y, z)

var = 75
print(var)
print(type(var))

print()

#Object References

print(300)

# n -> 777
n = 777

print(n)
print(type(n))

m = n

# m -> 777 <- n

print(m,n)
print(type(m),type(n))

m = 400
# m -> 400, 777 <- n
print(m)
print(type(m))

print()

# Checking Identity

m = 800
n = 655

print(id(m))
print(id(n))

n = 800

print(id(m))
print(id(n))

# Define Variables

# Camel Case (Method) : numberOfCollegeGraduates 
# Pascal Case (Class) : NumberOfCollegeGraduates
# Snake Case (Variable) : number_of_college_graduates

age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# Reserved Words
'''
False   def     if        raise
None    del     import    return
True    elif    in        try
and     else    is        while
as      except  lambda    with  
assert  finally nonlocal  yield
break   for     not 
class   from    or 
continue        global    pass
'''

