# optional
A mostly transparent python optional class (works with python 2 and 3)

This was a learning exercise. I have not tested/used this in a project.

Run the tests with 'python3 test_optional.py'.

A couple of implementation details made this harder - 'python3 challenges.py' runs a few tests that hight lights some of them

### Install
    "pip3 install optional"
    or Install by cloning the repo and running "sudo python3 setup.py install"

### See if a value is set, if not set one
    >>> from optional import optional
    >>> optional_value = optional()
    >>> optional_value.is_set
    False
    >>> optional_value = optional_value.set_value('some string')
    >>> optional_value
    'some string'
    >>> optional_value.is_set
    True

### Using a default value
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
### Optional 'becomes' your value
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

### Fedup of:

    >>> def foo(optional_list=None):
    ...     optional_list = optional_list if optional_list is not None else []
    ...     print(optional_list)
    ... 
    >>> foo()
    []

### Instead try:

    >>> def foo(optional_list=None):
    ...     optional_list = optional(optional_list, default=[])
    ...     print(optional_list)
    ... 
    >>> foo()
    []
    >>> foo([1,2,3])
    [1, 2, 3]

### Your own Classes will work too
    >>> class CustomClass(object):
    ...     def __init__(self, random, signature, of_custom_class):
    ...         pass
    ...     var = 'class data'
    ... 
    >>> optional_value = optional(CustomClass(1,2,3))
    >>> optional_value
    <optional.optional(<__main__.CustomClass object at 0x102107668>) object at 0x1021076a0>
    >>> optional_value.var
    'class data'
