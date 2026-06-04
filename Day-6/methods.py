Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="python programming"
s.center(28,'*')
'*****python programming*****'
s.center(28,'-')
'-----python programming-----'
s.ljust(28,'-')
'python programming----------'
s.rjust(28,'-')
'----------python programming'
'123'.zfill(5)
'00123'
'123'.zfill(10)
'0000000123'
'123'.zfill(3)
'123'
'123'.zfill(3)
'123'
s.find(r)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.find(r)
NameError: name 'r' is not defined
s.find('r')
8
s.find('g')
10
s.rfind('r')
11
s.find('w')
-1
s.index('o')
4
s.rindex('o')
9
s.index(z)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.index(z)
NameError: name 'z' is not defined
s.count('y')
1
s.count('m')
2
>>> s.count('w')
0
>>> 
>>> s
'python programming'
>>> s.replace('python','java')
'java programming'
>>> s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
>>> s.translate(s.maketrans('python','123456'))
'123456 1r5grammi6g'
>>> s='java,python,c,c++'
>>> s.split(',')
['java', 'python', 'c', 'c++']
>>> s.split(',',2)
['java', 'python', 'c,c++']
>>> s.rsplit(',',2)
['java,python', 'c', 'c++']
>>> g='sdfgh'
>>> g='''dfghjk'''
>>> g='''dfghjk
... fghjkl;
... gfhjkl
... drtyuikn'''
>>> g
'dfghjk\nfghjkl;\ngfhjkl\ndrtyuikn'
>>> s.splitlines()
['java,python,c,c++']
>>> g.splitlines()
['dfghjk', 'fghjkl;', 'gfhjkl', 'drtyuikn']
>>> l=['java','python','c','c++']
>>> ''.join(l)
'javapythoncc++'
>>> '-'join(l)
SyntaxError: invalid syntax
>>> '-'.join(l)
'java-python-c-c++'
>>> '@'.join(l)
'java@python@c@c++'
>>> ','.join(l)
'java,python,c,c++'
>>> s.partition(',')
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
('java,python,c', ',', 'c++')
