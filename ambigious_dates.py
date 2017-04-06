def f(x,y,z):
    l = []
    l.append(x)
    l.append(y)
    l.append(z)
    l.sort(reverse=True)
    yy = l[0]
    mm = l[2]
    dd = l[1]
    if yy > 31 and mm <= 12 and dd > 12:
        print(yy,mm,dd)
    else:
    	print("Ambigious")

        
f(2,11,12)
f(11,22,99)
f(1,2,99)
