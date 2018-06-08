def longest_run(L):
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
     
    for i in L[2:]:
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



a = longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2])
print(a)
#b = longest_run([5,4,10])
#print(b)
'''
def longest_run(L):
    i_terms = []
    d_terms = []
    for i in range(len(L)):
        if L[i+1] > L[i]:
            i_terms.append(i)
        if L[i+1] < L[i]
            d_terms.append(i)
            '''
