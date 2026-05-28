Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
float(a)
10.0
comples(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    comples(a)
NameError: name 'comples' is not defined. Did you mean: 'complex'?
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
bool(a)
True
bool(0)
False
b=10.5
int(b)
10
complex(b)
(10.5+0j)
str(b)
'10.5'
list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
bool(b)
True
bool(0.0)
False
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
s='python'
a='435678'
b='345.678'
int(s)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
int(a)
435678
int(b)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '345.678'
float(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
float(a)
435678.0
float(b)
345.678
list(a)
['4', '3', '5', '6', '7', '8']
list(s)
['p', 'y', 't', 'h', 'o', 'n']
>>> list(b)
['3', '4', '5', '.', '6', '7', '8']
>>> tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
>>> set(s)
{'y', 'o', 'p', 'h', 't', 'n'}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> int(a)
435678
>>> float(a)
435678.0
>>> float(b)
345.678
>>> bool(s)
True
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
>>> complex(a)
(435678+0j)
>>> complex(b)
(345.678+0j)
>>> l=[1,2,3,4,5]
>>> l
[1, 2, 3, 4, 5]
>>> int[l]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int[l]
TypeError: type 'int' is not subscriptable
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
