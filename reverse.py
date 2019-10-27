

def rev(str):
    """reverse string and preserve spaces
    >>> rev("hello world")
    'world hello'


    """

    str_list=str.split(' ')

    rev_list=str_list[::-1]

    return ' '.join(rev_list)

if __name__=="__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print('***Success**')