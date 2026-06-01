Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=20
a
a=20
b=20
a+b
40
a-b
0
a*b
400
a/b
1.0
a//b
1
9/2
4.5
9//2
4
a**2
400
6**3
216
a%b
0
17%4
1
a
20
b
20
a=20
b=10
a
20
b
10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True

y=5
y
5
y=y+5
y
10
y+=10
y
20
y+=10
y
30
y+=5
y
35
y-=5
y
30
y*=4
y
120
y//=10
y
12
y%=2
y
0
y/=2
y
0.0
y//=3
y
0.0
y+=
SyntaxError: invalid syntax
y+=10
y
10.0

a=20
b=10
a
20
b
10
a%10==0
True
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
True
a%20==0 and b%20==0 and a<\b
SyntaxError: unexpected character after line continuation character
a%20==0 and b%20==0 and a<b
False
not a>b
False

a='python programing'
a
'python programing'
'y' in a
True
'g' in a
True
'q' in a
False
l=['java' , 'python' , 'mysql' , 'c' , 'html']
l
['java', 'python', 'mysql', 'c', 'html']
'mysql' in l
True
'c' in l
True
t=('laptop' , 'mobile' , 'mouse' , 'keyboard']
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
t=('laptop' , 'mobile' , 'mouse' , 'keyboard')
t
('laptop', 'mobile', 'mouse', 'keyboard')
'laptop' in t
True
'mouse' in t
True
t={1,2,3,4,9,8,6,7}
t
{1, 2, 3, 4, 6, 7, 8, 9}
5 in t
False
3 in t
True
d={'egg':8 , 'oil':120 , 'sugar':80 }
d
{'egg': 8, 'oil': 120, 'sugar': 80}
'oil' in d
True
8 in d
False
'egg' in d
True


l=[1,2,3,4,5]
m=[6,7,8,9,0]
l==m
False
>>> n=m
>>> n
[6, 7, 8, 9, 0]
>>> n==m
True
>>>  l is m
...  
SyntaxError: unexpected indent
>>> n is m
True
>>> l is m
False
>>> id(l)
1948131943552
>>> id(n)
1948130929024
>>> id(m)
1948130929024
>>> l is not m
True
>>> m is not n
False
>>> 8&14
8
>>> 8|7
15
>>> 10^11
1
>>> ~14
-15
>>> ~26
-27
>>> 8>>2
2
>>> 15>>1
7
>>> 15>>2
3
>>> 15>>4
0
>>> 15>>3
1
>>> 16<<1
32
>>> 4<<2
16
