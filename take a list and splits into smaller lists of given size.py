def group(lst, size):
    a = []
    for i in range(0,len(lst)+1, size):
        a.append(lst[i:i + size])    
    return a
print(group([1, 2, 3, 4, 5, 6, 2], 3))
