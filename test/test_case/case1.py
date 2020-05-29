#/usr/bin/python

import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()

class Tests(unittest.TestCase):
    def test_0(self):
        self.assertTrue(self._flag)
        self._flag = False

    # @unittest.skip('skipped test')
    def test_1(self):
        self.fail('should have failed!')

    # @unittest.skipIf(os.name=='posix', 'Not supported on Unix')
    # def test_2(self):
    #     import winreg

    # @unittest.skipUnless(platform.system() == 'Darwin', 'Mac specific test')
    # def test_3(self):
    #     self.assertTrue(True)

    @unittest.expectedFailure
    def test_4(self):
        self.assertEqual(2+2, 5)

if __name__ == "__main__":
    unittest.main()