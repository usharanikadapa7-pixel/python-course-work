Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='     hello     world    '
s
'     hello     world    '
s.strip()
'hello     world'
>>> s.lstrip()
'hello     world    '
>>> s.rstrip()
'     hello     world'
>>> s='strings.py'
>>> s
'strings.py'
>>> s.startswith('str')
True
>>> s.startswith('ghd')
False
>>> s.endswith('js')
False
>>> 'sdfui'.isalpha()
True
>>> 'dfhduwmnjkwndkkkbwhvdwh'
'dfhduwmnjkwndkkkbwhvdwh'
>>> 'dfhduwmnjkwndkkkbwhvdwh'.isalpha()
True
>>> '23456'.isalpha()
False
>>> 'sdfhjklihgd'.isalnum()
True
>>> usha@11134.isalnum()
SyntaxError: invalid syntax
>>> 'ewrtybfd'.islower()
True
>>> 'shiljhsknkjeeikiejekkkknsk@#$'.islower()
True
>>> 'eruhvk#%^*(mdnerkr3l;t;3'.issupper()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    'eruhvk#%^*(mdnerkr3l;t;3'.issupper()
AttributeError: 'str' object has no attribute 'issupper'. Did you mean: 'isupper'?
>>> ' '.isspace()
True
>>> 'hello            '.isspace()
False
>>> 'Py Prg Lan'.istitle()
True
>>> 'Py prg lan'.istitle()
False
>>> 'py_python'.isidentifier()
True
>>> 'py@1234'.isidentifier()
False
