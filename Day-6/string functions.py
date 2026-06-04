Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="python programming"
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
>>> max
<built-in function max>
>>> max(s)
'y'
>>> ord(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
>>> ord('a')
97
>>> ord('A')
65
>>> chr(98)
'b'
>>> chr(120)
'x'
>>> chr(25)
'\x19'
>>> chr(16)
'\x10'
>>> chr(7)
'\x07'
>>> chr(35)
'#'
>>> chr(97)
'a'
>>> s="pytho"
>>> s.upper()
'PYTHO'
>>> s.lower()
'pytho'
>>> s1="python programming"
>>> s.upper()
'PYTHO'
>>> s1.upper()
'PYTHON PROGRAMMING'
>>> s1.capitalize()
'Python programming'
>>> s.swapcase()
'PYTHO'
>>> s1.swapcase()
'PYTHON PROGRAMMING'
>>> s1.title()
'Python Programming'
