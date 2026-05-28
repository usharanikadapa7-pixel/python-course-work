Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/usha1/OneDrive/Desktop/python-course-work/Day-3/datatypes.py
a=10
type(a)
<class 'int'>
t=9.99
type(a)
<class 'int'>
c=12+8j
type(c)
<class 'complex'>
s='python'
type(s)
<class 'str'>
s='''sdfsdfsg'''
type(s)
<class 'str'>
id(s)
2346622841648
1=[1,2,3,4,5]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[1,2,3,4]
type(l)
<class 'list'>
l=['post','reels']
>>> type(l)
<class 'list'>
>>> t=()
>>> type(t)
<class 'tuple'>
>>> t=(1,2,3,4)
>>> type(t)
<class 'tuple'>
>>> t=(10)
>>> type(t)
<class 'int'>
>>> t=(10,)
>>> type(t)
<class 'tuple'>
>>> s={1,2,3,4,5}
>>> type(s)
<class 'set'>
>>> s=set()
>>> s={1454455,456757,545,5677}
>>> a
10
>>> s
{545, 456757, 5677, 1454455}
>>> l=[]
>>> type(l)
<class 'list'>
>>> l=[1]
>>> type(l)
<class 'list'>
>>> d={'name':'abc','age':100,'courses':'pfs'}
>>> type(d)
<class 'dict'>
>>> status=True
>>> status=False
>>> type(a)
<class 'int'>
>>> type(status)
<class 'bool'>
>>> status=true
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    status=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a=None
>>> type(a)
<class 'NoneType'>
