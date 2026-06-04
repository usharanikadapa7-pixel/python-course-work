Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,1.2,"tyr")
t
(1, 1.2, 'tyr')
t=(10,20,30,40,50)
h=(90,79,80)
t+h
(10, 20, 30, 40, 50, 90, 79, 80)
t*3
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t[1]
20
t[5]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t[5]
IndexError: tuple index out of range
t[-1]
50
t[:3]
(10, 20, 30)
t[3:]
(40, 50)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::-1]
(50, 40, 30, 20, 10)
t[-1:-4:-1]
(50, 40, 30)
t[:2]
(10, 20)
t[::2]
(10, 30, 50)
30 in t
True
20 not in t
False
50 in t
True
60 in t
False
>>> False
False
>>> len(t)
5
>>> sorted(t)
[10, 20, 30, 40, 50]
>>> max(t)
50
>>> min(t)
10
>>> t.count(10)
1
>>> t.index(10)
0
>>> a,b,c=(1,2,3)
>>> a
1
>>> b
2
>>> c
3
>>> a=(1,3,5)
>>> x,y,z=a
>>> x
1
>>> y
3
>>> z
5
>>> t=(1,2,3,[4,5,6],7,8)
>>> t
(1, 2, 3, [4, 5, 6], 7, 8)
>>> t[2]
3
>>> t[4]
7
>>> t[2]=4
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
>>> t[3]
[4, 5, 6]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
