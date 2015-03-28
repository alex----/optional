#!/usr/bin/env python3
import types
import operator
import unittest


class Challenges(unittest.TestCase):
    def test_run_time_add_adition(self):
        """ Implement __add__ for class + 3. But not at runtime """
        class foo(object):
            i = 5

            def __add__(self, other):
                return self.i + other
        foo_instance = foo()
        self.assertEqual(foo_instance.__add__(5), 10)
        self.assertEqual(foo_instance + 5, 10)

        class bar(object):
            i = 5

        bar_instance = bar()
        bar_instance.__add__ = types.MethodType(
            lambda self, other: self.i + other, bar_instance)
        self.assertEqual(bar_instance.__add__(5), 10)
        # __add__ added at run time will not be used.
        self.assertRaises(TypeError, operator.add, bar_instance, 5)

    def test_sometimes_you_can_change_class(self):
        """ Sometimes a class can become another class - but not always """
        class foo(object):
            f = 1

        class bar(object):
            b = 2

        # We can change the type of this instance at run time
        foo_instance = foo()
        self.assertEqual(foo_instance.f, 1)
        bar_instance = bar()
        self.assertEqual(bar_instance.b, 2)
        bar_instance.__class__ = foo
        self.assertEqual(bar_instance.f, 1)
        self.assertRaises(AttributeError, getattr, bar_instance, 'b')
        # But not for all types
        try:
            bar_instance.__class__ = str
            self.fail('Never happens because can not assign str to the __class__')
        except TypeError:
            pass
        # But when you can - you can in a class which is cool/stange

        def change(self, other):
            self.__class__ = other.__class__
        bar_instance = bar()
        bar_instance.change = types.MethodType(change, bar_instance)
        self.assertEqual(type(bar_instance), bar)
        bar_instance.change(foo_instance)
        self.assertEqual(type(bar_instance), foo)

    def test_even_mutable_types_often_cant_have_random_attrs(self):
        """ Test you can random attributes to some but not all types """
        class foo(object):
            pass
        foo_instance = foo()
        foo_instance.random_attr = 0
        self.assertEqual(foo_instance.random_attr, 0)
        bar_instance = str()
        self.assertRaises(AttributeError, setattr, bar_instance, 'random_attr', 0)

if __name__ == '__main__':
    unittest.main()
