import unittest
import cap


class test_cap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')


if __name__ == '__main__':
    unittest.main()
