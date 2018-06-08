
##Created on Thu Dec 07 02:50 2017
##@author: jamespeter


def genFib():
    """ This generates fibonacci series, yields the next finbonacci number
        upon each subsequent call. Starting with 1,then second number returned
        is 2, then 3 which is 2 + 1 and next 5 which is 3 + 2, so on, as along
        it is being called by using the next on the generator object like
        next(generator_object). And to generated certain amount of fibonacci,
        next(generator_object) can be used in a loop to generate the sequence.
        The fibonacci series starts with 1, 1, 2, 3, 5...
        
        function call: gen_fib = genFib() --> gen_fib.__next__() or next(gen_fib)
    """
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
