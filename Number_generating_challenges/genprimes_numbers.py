# author @jamespeter created on 08 Dec, 12:19 pm 2017

def genPrimes():
    """ Function to generate prime number one at a time
        when needed or called one at a time using:
        g=genPrimes() ---> g.__next__() or next(g)
        # yields one prime number per call
    """
    base = 2
    while True:
        prime = True
        if base == 2:
            yield 2
        else:
            for n in range(2, base):
                if base%n == 0:
                    prime = False
            if prime == True:
                yield base
        base += 1

