def weird_n():
    """
    Given an integer, , perform the following conditional actions:

    If n is odd, print Weird
    If n is even and in the inclusive range of  to , print Not Weird
    If n is even and in the inclusive range of  to , print Weird
    If n is even and greater than , print Not Weird
    """

    n = int(input().strip())
    s = ''
    if n % 2 == 1:
        s = 'Weird'
    else:
        s = 'Weird'
        if 2 <= n <= 5:
            s = 'Not ' + s
        elif 6 <= n <= 20:
            pass
        elif 20 < n:
            s = 'Not ' + s
        else:
            s = ''
    return s


def






if __name__ == '__main__':
    print(weird_n())



