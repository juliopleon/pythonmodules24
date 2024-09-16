# import unittest and script u want to test
import unittest
import cap

# create a test class


class test_cap(unittest.TestCase):

    # test methods to make sure scripts are working
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')


if __name__ == '__main__':
    unittest.main()
