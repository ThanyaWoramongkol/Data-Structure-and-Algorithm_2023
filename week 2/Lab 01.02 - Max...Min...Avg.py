"""Lab 01.02 - Max...Min...Avg"""
from json import loads as l

def stat(lst):
    """-"""
    mak, noi = 0, 0
    store = True
    for i in lst:
        if i >= mak:
            mak = i
        if noi == 0 and store:
            noi = mak
            store = False
        if i < noi:
            noi = i

    avg = round(sum(lst) / len(lst), 2)
    mak = round(mak, 2)
    noi = round(noi, 2)
    print("(%s, %s, %s)" % (mak, noi, avg))
stat(l(input()))
