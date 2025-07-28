# Python-Session-2025

 Open Command prompt for Windows or Terminal for Macbook 

 Navigate to the folder you want to clone 

 Copy and paste the below commant in Command Prompt 

              > git clone https://github.com/a8hok/Python-session-2025.git
              
Make sure Python installed 

              > python3 --version

Install Visual Studio Code

Open the cloned folder in Visual Studio code

Open the terminal

Make the you're in the right folder path

Then run the following python files

                > python3 students.py

                > python3 employee.py

Verify the outputs

Explore the code line by line.

Practice on the same.


# Python Basics

A beginner-friendly guide to core Python concepts with brief explanations and working examples.

---

## Keywords

Python keywords are reserved words that cannot be used as identifiers.

```python
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
```

---

## Data Types

Python supports multiple built-in data types such as:

* int
* float
* str
* bool
* list
* tuple
* set
* dict

```python
val1 = 10 # Integer
print(type(val1))

bool1 = True # Boolean
print(type(bool1))
```

---

## Variables

Variables are containers for storing data values.

```python
intvar , floatvar , strvar = 10, 2.57, "Python Language"
print(intvar)
print(floatvar)
print(strvar)
```

```python
p = 20
print(p, id(p), type(p), hex(id(p)))
```

---

## Integer

Integer values are whole numbers.

```python
a = 6
b = 7
c = a + b
print('Addition of {} and {} will give: {}'.format(a,b,c))

print(f"Addition of {a} and {b} will give: {c}")
```

---

## String

Strings store sequences of characters.

```python
str1 = 'HELLO PYTHON'
print(str1[0:4])

s1 = "Hello"
s2 = "Asif"
s3 = s1 + " " + s2
print(s3)

mystr2 = 'Woohoo '
mystr2 = mystr2*5
print(mystr2)
```

```python
mystr1 = "Hello Everyone"
for i in mystr1:
    print(i, 'hai')

for i in enumerate(mystr1):
    print(i)

print('Hello' in mystr1)
print('Everyone' in mystr1)
print('Hi' in mystr1)
```

```python
str5 = "Natural language processing with Python and R and Java"
L = str5.partition("and")
print(L)

str6 = "apple, test, orange"
L = str6.partition(", ")
print(L)
```

```python
mystr = "My favourite series is \"Game of Thrones\""
print(mystr)
```

---

## List

Lists are ordered, mutable collections.

```python
mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
print(mylist[0:3])
print(mylist[2:5])
print(mylist[:3])
print(mylist[-3:])

mylist.insert(8,'ten')
print(mylist)

mylist.pop(3)
print(mylist)

mylist.remove("seven")
print(mylist)
```

List Comprehension:

```python
mylist1 = [i for i in range(40) if i % 2 == 0]
print(mylist1)

list1 = [2,3,4,5,6,7,8]
list1 = [i*10 for i in list1]
print(list1)
```

---

## Tuple

Tuples are immutable sequences.

```python
mytuple = ('one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight')
print(mytuple[2:5])
```

---

## Set

Sets are unordered collections with no duplicate items.

```python
myset = {1,2,3,4,5}
print(myset)

my_set = {1,1,2,2,3,4,5,5,9,9}
print(my_set)
```

---

## Dictionary

Dictionaries store key-value pairs.

```python
mydict = {1:'one' , 'A':'two' , 3:'three'}
print(mydict.keys())
print(mydict.values())
print(mydict.items())

mydict1 = {'Name':'Asif' , 'ID': 74123 , 'DOB': 1991 , 'job' :'Analyst'}
print(mydict1['Name'])

mydict1['DOB'] = 1992
mydict1['Address'] = 'Delhi'
mydict1['Job'] = 'Analyst'
mydict1.pop('Job')

for i in mydict1:
    print(i , ':' , mydict1[i])

print('Name' in mydict1)
print('Asif' in mydict1)
```

Dictionary Comprehension:

```python
double = {i:i*2 for i in range(10)}
```

---

## \*args

Used to pass a variable number of non-keyword arguments.

```python
def myfunc(*args):
    print(args)

myfunc(1, 2, 3)
```

```python
def myfunc(*args, city):
    print(f"City: {city}")

myfunc(1, 2, 3, city="Chennai")
```

```python
def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)

my_list = [2, 3]
some_args(1,*my_list)
```

---

## \*\*kwargs

Used to pass a variable number of keyword arguments.

```python
def myfunc(**kwargs):
    print(kwargs)

myfunc(name="Ashok", age=30)
```

---

## Mixed Args and Kwargs

```python
def myfunc(a, b, *args, city, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("city:", city)
    print("kwargs:", kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

myfunc(1, 2, 3, 4, 5, city="Chennai", pin=600001, country="India")
```

---

## Functions

Functions are blocks of reusable code.

```python
def myfunc():
    print("Hello Python Lovers")

myfunc()


def details(name, userid, country):
    print('Name :- ', name)
    print('User ID is :- ', userid)
    print('Country :- ',country)

details('Asif' , 'asif123' , 'India')
```

Even/Odd Check:

```python
def even_odd(num):
    if num % 2 == 0:
        print(num, 'is even number')
    else:
        print(num, 'is odd number')

for i in range(100,105):
    even_odd(i)
```

---

## Lambda Functions

Used to create anonymous functions.

```python
square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(10, 20))
```

---

## Map and Filter

Apply functions to collections.

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, nums))
print(squared)

nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)
```

---

## Control Flow

Control statements like `continue` and `break` alter the loop execution.

```python
for i in range(5):
    if i == 3:
        continue
    if i == 4:
        break
    print('value', i)
```

---

## String Formatting

```python
name = "Ashok"
age = 34
print(f"Name: {name}, Age: {age}")
print("Name: {}, Age: {}".format("Ashok", 34))
```

---

## Multi-line Comments

Use triple quotes for documentation strings.

```python
"""
Multiple
line
comment
"""
```

