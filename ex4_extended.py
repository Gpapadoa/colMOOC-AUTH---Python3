def squares(*args):

    d=args[0]

    import statistics as st
    mesos=st.mean(d)

    for k in d:
        yield (mesos-k)**2

    return 

        
alist=[]
while True:

    x=input('Δώσε αριθμό η 0 για έξοδο: ' )

    if x == 'q':
        break
    else:
        alist.append(int(x))

for i in squares(alist):
    print(i)

