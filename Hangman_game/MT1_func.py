def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns keys for only unique values in dict
    '''
    # Your code here
    values = []
    keys = []
    for key,value in aDict.items():
        keys.append(key)
        values.append(value)
    a = []
    for i in values:
        if values.count(i) > 1:
            continue
        else:
            for j in keys:
                if aDict[j] == i:
                    a.append(j)
                    
    
    return a

print(uniqueValues({'a':2,'b':4,'c':4, 'd':2}))
