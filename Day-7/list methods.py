Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[]
l=list()
type()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
type(l)
<class 'list'>
l=[1,2,3,4]
m=[5,6,7,8]
l+m
[1, 2, 3, 4, 5, 6, 7, 8]
l*4
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l=[10,20,30,40,50]
l
[10, 20, 30, 40, 50]
>>> l[4]
50
>>> l[3]
40
>>> l[-1]
50
>>> l[-5]
10
>>> l[-7]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l[-7]
IndexError: list index out of range
>>> l[:3]
[10, 20, 30]
>>> l[3:]
[40, 50]
>>> l[1:3]
[20, 30]
>>> l[::-1]
[50, 40, 30, 20, 10]
>>> l[-1:-4:-1]
[50, 40, 30]
>>> l[-3::-1]
[30, 20, 10]
>>> l
[10, 20, 30, 40, 50]
>>> 20 in l
True
>>> 50 in l
True
>>> 70 not in l
True
>>> 80 in l
False
>>> l
[10, 20, 30, 40, 50]
>>> l[1]=70
>>> l
[10, 70, 30, 40, 50]
>>> id(l)
2358829171328
>>> l[4]=100
>>> l
[10, 70, 30, 40, 100]
>>> id(l)
2358829171328
l.append(120)
l.append(400)
l
[10, 70, 30, 40, 100, 120, 400]
l.insert(88,5)
l
[10, 70, 30, 40, 100, 120, 400, 5]
l.insert(4,50)
l
[10, 70, 30, 40, 50, 100, 120, 400, 5]
l.insert(7,99)
l
[10, 70, 30, 40, 50, 100, 120, 99, 400, 5]
l.extend([45,66,23)]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
l
[10, 70, 30, 40, 50, 100, 120, 99, 400, 5]
l.extend([45,66,23])
l
[10, 70, 30, 40, 50, 100, 120, 99, 400, 5, 45, 66, 23]
l.pop()
23
l
[10, 70, 30, 40, 50, 100, 120, 99, 400, 5, 45, 66]
l.pop(6)
120
l
[10, 70, 30, 40, 50, 100, 99, 400, 5, 45, 66]
l.remove(5)
l
[10, 70, 30, 40, 50, 100, 99, 400, 45, 66]
l.remove(50)
l
[10, 70, 30, 40, 100, 99, 400, 45, 66]
del l[1]
l
[10, 30, 40, 100, 99, 400, 45, 66]
del l[5]
l
[10, 30, 40, 100, 99, 45, 66]
l.clear()
l
[]
l=[20,34,56,84,546,244,455,54,5]
l
[20, 34, 56, 84, 546, 244, 455, 54, 5]
sorted(l)
[5, 20, 34, 54, 56, 84, 244, 455, 546]
l.sort()
l
[5, 20, 34, 54, 56, 84, 244, 455, 546]
min(l)
5
max(l)
546
l.reverse()
l
[546, 455, 244, 84, 56, 54, 34, 20, 5]
l.sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    l.sorted(reverse=True)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    sorted(reverse=True)
TypeError: sorted expected 1 argument, got 0
sorted(l,reverse=True)
[546, 455, 244, 84, 56, 54, 34, 20, 5]
l.index(244)
2
l.index(34)
6
l.count(455)
1
l.count(5)
1
l
[546, 455, 244, 84, 56, 54, 34, 20, 5]
m=l
m
[546, 455, 244, 84, 56, 54, 34, 20, 5]
l
[546, 455, 244, 84, 56, 54, 34, 20, 5]
m.append(45)\

m.append(45)
SyntaxError: multiple statements found while compiling a single statement
m.append(67)
m
[546, 455, 244, 84, 56, 54, 34, 20, 5, 67]
l
[546, 455, 244, 84, 56, 54, 34, 20, 5, 67]
n=l.copy()
n
[546, 455, 244, 84, 56, 54, 34, 20, 5, 67]
n.append(100)
n
[546, 455, 244, 84, 56, 54, 34, 20, 5, 67, 100]
l
[546, 455, 244, 84, 56, 54, 34, 20, 5, 67]
len(l)
10
sum(l)
1565
any([1,2,3,4,5,6])
True
any([1,2,3,4,0,0,0])
True
any([0,0,0])
False
all([1,2,3,4,5,6])
True
all(1,2,3,0,0])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
all([1,2,3,0,0,0])
False
