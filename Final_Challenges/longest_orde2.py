#paste your code here
def longest_run(L):
"""

    A run of monotonically increasing numbers means that a number at position k+1 in the sequence is greater than or equal to the number at position k in the sequence.
    A run of monotonically decreasing numbers means that a number at position k+1 in the sequence is less than or equal to the number at position k in the sequence.

Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
"""
    i_terms = []
    d_terms = []
    temp_i = []
    temp_d = []
    d = False
    i = False

    def summing(k):
        summed = 0
        for num in k:
            summed += num
        return summed

    temp_d.extend(L[:1])
    temp_i.extend(L[:1])
    
    for i in L[1:]:
        if i <= temp_d[-1]:
                temp_d.append(i)
        if i >= temp_i[-1]:
                temp_i.append(i)
        else:
            if len(i_terms) < len(temp_i):
                i_terms = temp_i.copy()
            if len(d_terms) < len(temp_d):
                d_terms = temp_d.copy()
            temp_i = [i]
            temp_d = [i]

    if len(i_terms) == len(d_terms):
        if L.index(i_terms[0]) < L.index(d_terms[0]):
            return summing(i_terms)
    if len(i_terms) > len(d_terms):
        return summing(i_terms)
    return summing(d_terms)

#L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] , increasing: [3, 4, 5, 7, 7], decreasing: [10, 4, 3]
#L = [5, 4, 10] , increasing: [4, 10], decreasing: [5, 4]

a = longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2])
print(a)
