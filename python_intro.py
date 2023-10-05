#comments!  This is a comment
print("hello Theives!!!!") # this print statement greets the use

#To-Do
#
#variables
xsajfdhasfdno = 5
number3 = 151515

# 'protected'words/terms  -->be careful with our variable names!!!!
#int = 51651491  <-- Don't redefine protected words!!!
# print(int('5'))

#Datatypes! Starting with nmbers
#Integers AND floats
num1 = 8
print(num1)
print(type(num1))

num2 = 8.0
print(num2)
print(type(num2))

num3 = 5.987435
print(int(num3))

#Math operations!
print('Math!!!\n')

#add +
add = 5 + 5
print(add)

#subtraction -
sub = 10 - 5
print(sub)

#multiplication *
prod = 5 * 5
print(prod)
print(type(prod))

#division /
div = 25 / 5
print(div)
print(type(div))

#exponents **
powerful = 5 ** 5
print(powerful)

#floor division //
fdiv = 26 // 5
print(fdiv)

#modulo %
mod = 26 % 5
print(mod)
    #This will come in handy VERY soon anytime we want to determine odd or even
print(24 % 2 == 0)
print(25 % 2 != 0)

# let's talk about equal signs/equality
# = this is assignment
# == This is an equality check   ///  checking for type AND value equality
print('5' == 5)

#Strings
print('\nSTRINGS\t:')
# they're ordered, immuteable, iterable
# you can use single or double quotes; either is fine BUT watch the interaction

st1 = 'single quote string'
st2 = "double quote string"
st3 = "we've messed this up"
st4 = 'or did we "really?"'
st5 = 'oh no we\'ve messed this up'
st6 = ";sakjdflvaj @hjsanjkn1581"
print(st5)

print(st1[-3])
print(len(st3))
#manipulating strings

# concatenation + interpolation (f-string and maybe don't need to remember this term exaclty)

#concatenation
print(st1 + st4) #simple
print(st2 + ' : : ' + st3) #adding a literal
print(st2 + ' ' + str(mod) + ' ' + '<-- that was a little funky') # complicated example

# f-strings (or interpolation if you're fancy)

f_st = f"This is still just a string BUT we can include pythony things like {mod} or  {st1[-6]}"
print(f_st)

#string methods

print(st5.upper())
print(st5)

# incrementing and decrementing
num5 = 234
num6 = 98734
print(num5 + num6)
print(num5, num6)
num5 = num5 + 6 #long-hand version
print(num5)
num5 += 10 #short-hand version
print(num5)
num5 -= 100 #can be used with other math operators as well
print(num5)

f_st += "I'M ADDING THIS!!!!"
print(f_st)


print('\AND now onto functions vs methods')



# functions vs methods
#syntax  -->  function(arguments)  vs  datatype.method(arguments)

#lists
#indexed, ordered, iterable, muteable, and dynamic
#syntax -->  alist = [1, 2, 3 4]
a_list =[]
print(a_list)
nums_list = [10, 20, 30, 40, 50]
print(nums_list, type(nums_list), len(nums_list), nums_list[0], nums_list[-1])
nums_list[0] = 60986095

print(nums_list)
rando_list = [1, '2', 3.0, True, None, []]
print(rando_list)
print(rando_list[3])

print('list methods:')
# .append()
# adds to the END of the list
a_list.append(5)
print(a_list)
a_list.append(15)
print(a_list)
a_list.append(25)
print(a_list)

# .pop()
# removes an item from the list by position, defaults to the last.  Returns the value so you could save t to a variable. ..
a_list.pop()
print(a_list)
print(a_list.pop(0))
print(a_list)

# .remove()
# remove takes out the FIRST occurence of a VALUE
a_list.append(50)
a_list.append(75)
a_list.append(50)
print(a_list)
a_list.remove(50)
print(a_list)

#sort and sorted
print('\n\nsorted:')
print(sorted(a_list))
print(a_list)
print('\n.sort')
a_list.sort()
print(a_list)


print('\nString example with slicing:')
#   f_st[0] = 'Z'  -->
#slicing --> [start :stop: step] first example -->  [:]
x = 'z' + f_st[1:]
print(x)


print('\nLOOPS')
# 3 types of loops:  for loop, index loop, and while loop
names = ['Eddie', 'Lee', 'Stephen', 'Jeni', 'Gianni', 'Heather', 'Eddie']

print('for loop:')
#for loop --> syntax:
# for item in items:
#   codeblock to run on item
step = 1
for name in names:
    print(name.upper())
    # print(step)
    # step += 1
for a in a_list:
        print(a**8)

# index loop. . . but first, did we talk the range function?
# let's talk about the range function:
for x in range(5):
      print(x)
for x in range(0, 5, 1):
      print(x)
for x in range(50, 10, -10):
      print(x)
for x in range(3):
      print('3 steps taken')

#back to the index loop:
#syntax
# for i ini range(len(iterable)):
#   codeblock
print('\nINDEX loop')
for i in range(len(names)):
      print(i, names[i])

# while loops
# syntax
# while condition:
#   codeblock
while True:
      print('bad idea')
      break

l = 0
while l < len(names):
      print(l, names[l])
      l += 1

#conditionals: if, elif, else
# syntax    if condition:
                #code to execute
if 3 < 1:
      print('duh')
if names[0] == 'Lee':
      print('it is Lee!')
elif names[0] == 'Jeni':
      print('it is Jeni!')
elif names[0] == 'Eddie':
      print('Eddie is in the list!')
else:
      print('we don\'t know this person')

age = 13

if age < 18:
      print('kid')
elif age > 64:
      print('senior')
else:
      print('adult')

#functions
# definition vs calling the function
def hello(name):
    print(f"OMGosh So happy you are here {name.upper()}!")
   

hello('Jeni')
hello('Lee')
hello('stephen')
print(hello(st3))

def adder(a, b):
    return a + b
def subtr(a, b):
    print(a - b)

adder(6, 5)
subtr(10, 5)
subtr(adder(6, 5), 6)
# adder(subtr(67, 5), 98)

# user = input('this is what shows on the screen and asks you to type something --->     ')
# print(user)

# if 'a' in user:
#       print('YEP it is!')
print(names)
if 'Jeni' in names:
      print('YEP')
else:
      print('NOT FOUND')






