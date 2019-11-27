import unittest

from ..main.Diamond import Diamond

class DiamondTest(unittest.TestCase):

    def test_diamond_no_word_found(self):
        diamond = Diamond("12")
        with self.assertRaises(Exception) as context:
            diamond.draw()
        self.assertTrue('No word found' in str(context.exception))

    def test_draw_b_line(self):
        diamond = Diamond("b")
        result = diamond.getLine(1)
        self.assertEqual(result, "b b\n")

    def test_draw_c_line(self):
        diamond = Diamond("c")
        result = diamond.getLine(2)
        self.assertEqual(result, "c   c\n")

    def test_draw_top_lines(self):
        diamond = Diamond("c")
        result = diamond.drawTop(2)
        self.assertEqual(result, "a\nb b\n")

    def test_draw_botton_lines(self):
        diamond = Diamond("c")
        result = diamond.drawBottom(2)
        self.assertEqual(result, "c   c\nb b\na")

    def test_diamond_success_example_case(self):
        letter = "c"
        start = "a\nb b\nc   c\nb b\na"
        diamond = Diamond(letter)
        self.assertEqual(start, diamond.draw())

if __name__ == '__main__':
    unittest.main()