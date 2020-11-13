
#Yield used in the place of return, but it will return generator
def topten():

    yield 1;
    yield 5

def toptensqft():
    n=1;
    while n<=10:
        sq = n*n
        yield sq
        n+=1

values = topten()
print(values)
print(values.__next__())
print(values.__next__())

sqValues = toptensqft()
for i in sqValues:
    print(i)