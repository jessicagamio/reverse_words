import unittest

def rev(str):
    """reverse string and preserve spaces
    >>> rev("   hello world")
    'world hello   '


    """

    str_list=str.split(' ')

    rev_list=str_list[::-1]
    
    return ' '.join(rev_list)


class testFunc(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual( rev("   hello world"), "world hello  ")



# if __name__=="__main__":
#     from doctest import testmod
#     if testmod().failed == 0:
#         print('***Success**')

if __name__=="__main__":
    unittest.main(verbosity=2)