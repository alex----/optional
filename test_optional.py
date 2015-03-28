import unittest
import optional


class TestOptional(unittest.TestCase):
    def test_optional_basic_int(self):
        """ Test optional can 'be' and int """
        optional_value = optional.optional(5)
        self.assertTrue(isinstance(optional_value, int))
        self.assertEqual(optional_value + 5, 10)
        self.assertTrue(optional_value.is_set)
        self.assertFalse(optional_value.is_default)

    def test_optional_none_to_int(self):
        """ Test optional can start unset and then 'be' and int """
        optional_value = optional.optional()
        self.assertFalse(optional_value.is_set)
        optional_value = optional_value.set_value(5)
        self.assertTrue(isinstance(optional_value, int))
        self.assertEqual(optional_value + 5, 10)
        self.assertTrue(optional_value.is_set)
        self.assertFalse(optional_value.is_default)

    def test_default(self):
        """ Test that optional can 'be' a default and revert to it when unset """
        default_value, non_default_value = 5, 10
        optional_value = optional.optional(default=default_value)
        self.assertTrue(isinstance(optional_value, int))
        self.assertEqual(optional_value, default_value)
        self.assertFalse(optional_value.is_set)
        self.assertTrue(optional_value.is_default)

        optional_value = optional_value.set_value(non_default_value)
        self.assertEqual(optional_value, non_default_value)
        self.assertTrue(optional_value.is_set)
        self.assertFalse(optional_value.is_default)

        optional_value = optional_value.set_value(None)
        self.assertEqual(optional_value, default_value)
        self.assertFalse(optional_value.is_set)
        self.assertTrue(optional_value.is_default)

    def test_reset_default(self):
        """ Test that the after unsetting a value we go back to default """
        optional_value = optional.optional(default=[])
        optional_value.append(1)
        self.assertEqual(optional_value, [1])
        optional_value = optional_value.set_value([1, 2, 3])
        self.assertEqual(optional_value, [1, 2, 3])
        optional_value = optional_value.set_value(None)
        self.assertEqual(optional_value, [])

    def test_custom_class_custom_init(self):
        class foo():
            def __init__(self, something_a, something_b):
                self.something_a, self.something_b = something_a, something_b

        foo_instance = foo(1, 2)
        optional_value = optional.optional(foo_instance)
        self.assertEqual(optional_value.something_a, 1)
        self.assertEqual(optional_value.something_b, 2)

    def test_optional_as_default_param(self):
        """ Test that we dont have to do it something = something if something else default """
        def foo(something=None):
            something = optional.optional(something, default=[])
            something.append(None)
            return something
        self.assertEqual(len(foo()), 1)

    def test_optional_of_optionals(self):
        value = 'some string'
        optional_value_a = optional.optional(value)
        self.assertEqual(optional_value_a, value)
        optional_value_b = optional.optional(optional_value_a)
        self.assertEqual(optional_value_b, value)
        optional_value_c = optional.optional(optional_value_b)
        self.assertEqual(optional_value_c, value)

if __name__ == '__main__':
    unittest.main()
