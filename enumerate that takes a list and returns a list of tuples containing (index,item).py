def en(li):
    ne=[(li.index(x),x) for x in li]
    return ne
for i,j in en(['a','b',3]):
    print(i,j)
