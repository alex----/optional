# optional
A mostly transparent python3 optional class

This was an exercise to learn a little more of python3. I have not tested/used this in a project.


>>> from optional import optional
>>> optional_value = optional(None, default=[])
>>> optional_value
[]
>>> optional_value.is_set
False
>>> optional_value.is_default
True
>>> optional_value.append('some string')
>>> optional_value
['some string']

>>> type(optional([]))
<class 'optional.optional([])'>
>>> isinstance(optional([]), list)
True

>>> type(optional('some string'))
<class 'optional.optional(some string)'>
>>> isinstance(optional('some string'), str)
True

>>> optional_value = optional('some string')
>>> optional_value
'some string'
>>> optional_value.is_set
True
>>> optional_value.is_default
False
>>> optional_value = optional_value.set_value(10)
>>> optional_value
10

Fedup of:


>>> def foo(optional_list=None):
...     optional_list = optional_list if optional_list is not None else []
...     print(optional_list)
... 
>>> foo()
[]

instead try:

>>> def foo(optional_list=None):
...     optional_list = optional(optional_list, [])
...     print(optional_list)
... 
>>> foo()
[]


