Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={1,2,3,4}
s
{1, 2, 3, 4}
s=set()
s
set()
s={1,1,1,1,1}
s
{1}
s={324,234,145,34,67,34,89}
s
{145, 34, 67, 324, 89, 234}
s.add(1)
s
{145, 34, 67, 324, 1, 89, 234}
s.add(44.23)
s
{145, 34, 67, 324, 1, 89, 234, 44.23}
s.add("usha")
s
{1, 67, 324, 'usha', 145, 89, 34, 234, 44.23}
s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({1,4,7})
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.add({1,4,7})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add((1,2,3,4))
s
{1, 67, 324, 'usha', (1, 2, 3, 4), 145, 89, 34, 234, 44.23}
4 in s
False
1 in s
True
s.add(False)
s
{False, 1, 67, 324, 'usha', (1, 2, 3, 4), 145, 89, 34, 234, 44.23}
False in s
True
(1,2,3,4) in s
True
a={1,2,3,4,5}
b={3,5,7,8}
a|b
{1, 2, 3, 4, 5, 7, 8}
a.union(b)
{1, 2, 3, 4, 5, 7, 8}
a.intersection(b)
{3, 5}
a&b
{3, 5}
#{1}{2}{3}{5}{1,3}{1,2} this are the subsets in parent sets
a<={1}
False
a>={1}
True
a
{1, 2, 3, 4, 5}
b
{8, 3, 5, 7}
a.isdisjoint(b)
False
a.isdisjoint({190,801})
True
a.add(17)
a
{1, 2, 3, 4, 5, 17}
a.add(14)
a
{1, 2, 3, 4, 5, 17, 14}
a.update({11,12,13})
a
{1, 2, 3, 4, 5, 11, 12, 13, 14, 17}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 11, 12, 13, 14, 17}
a.remove(6)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.remove(6)
KeyError: 6
a.remove(13)
a
{3, 4, 5, 11, 12, 14, 17}
a.remove(17)
>>> a
{3, 4, 5, 11, 12, 14}
>>> a.discard(6)
>>> a
{3, 4, 5, 11, 12, 14}
>>> a.clear()
>>> a
set()
>>> a
set()
>>> a={1,23,4,57,235}
>>> b={1,2,3,4}
>>> a.intersection(b)
{1, 4}
>>> a
{1, 4, 23, 57, 235}
>>> b
{1, 2, 3, 4}
>>> a.intersection_update(b)
>>> a
{1, 4}
>>> b
{1, 2, 3, 4}
>>> c=b
>>> c
{1, 2, 3, 4}
>>> c.add(12)
>>> c
{1, 2, 3, 4, 12}
>>> b
{1, 2, 3, 4, 12}
>>> d=c.copy()
>>> d
{1, 2, 3, 4, 12}
>>> c
{1, 2, 3, 4, 12}
>>> len(c)
5
>>> max(c)
12
>>> min(c)
1
>>> sorted(c)
[1, 2, 3, 4, 12]
>>> sum(c)
22
