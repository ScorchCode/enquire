import unittest
from enquire import Enquire


class TestEnquireSpecs(unittest.TestCase):

    def setUp(self):
        self.enq = Enquire()

    def test_valid_letterspec(self):
        valid_spec = (
            ("a_e", ["", "a", "b", "c", "d", "e"]),
            ("A_E", ["", "a", "b", "c", "d", "e"]),
            ("f_b", ["", "b", "c", "d", "e", "f"]),
            ("t,e,s,t", ["", "t", "e", "s", "t"]),
            ("t , e , s , t ", ["", "t", "e", "s", "t"]),
            ("t,E,s,T", ["", "t", "e", "s", "t"]),
            ("opt1, opt2", ["", "opt1", "opt2"]),
            ("Single valid phrase", ["", "Single valid phrase"]),
            ("", ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        )
        for inp, outp in valid_spec:
            self.assertEqual(self.enq.allowed_letters(inp), outp, f"{inp} should yield {outp}")

    def test_bad_letterspec(self):
        bad_spec = (
            ("ab_c", "a_bc", "1_9", "A_9", "a_", "_z")
        )
        for inp in bad_spec:
            with self.assertRaises(ValueError):
                self.enq.allowed_letters(inp)

    def test_valid_numberspec(self):
        valid_spec = (
            ("1_5", ["", "1", "2", "3", "4", "5"]),
            ("9_5", ["", "5", "6", "7", "8", "9"]),
            ("2,4,6,8", ["", "2", "4", "6", "8"]),
            (" 1 , 3 , 5 , 7 ", ["", "1", "3", "5", "7"]),
            ("", ["", "0", "1", "2", "3", "4",  "5", "6", "7", "8", "9"])
        )
        for inp, outp in valid_spec:
            self.assertEqual(self.enq.allowed_numbers(inp), outp, f"{inp} should yield {outp}")

    def test_bad_numberspec(self):
        bad_spec = (
            ("a_c", "1_7.5", "A_9", "1_", "_9")
        )
        for inp in bad_spec:
            with self.assertRaises(ValueError):
                self.enq.allowed_numbers(inp)


if __name__ == '__main__':
    unittest.main()
