import unittest

# class TestSomething(unittest.TestCase):

#     def test_example(self):
#         self.assertEqual(2 + 2, 4)

# if __name__ == "__main__":
#     unittest.main()


# class TestNotEqual(unittest.TestCase):

#     def test_value(self):
#         self.assertNotEqual(5 * 2, 10)


    

# class TestStrings(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual("python".upper(), "Python")




# class TestException(unittest.TestCase):

#     def test_error(self):
#         with self.assertRaises(ZeroDivisionError):
#             10 / 2
            
            
class TestIn(unittest.TestCase):

    def test_membership(self):
        self.assertIn(4, [1, 2, 3])



if __name__ == "__main__":
    unittest.main()