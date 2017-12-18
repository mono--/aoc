

def A(n):
    d = (n*16807) % 2147483647;
    if d % 4 == 0:
        return d;
    else:
        return A(d);

def B(n):
    d = (n*48271) % 2147483647;
    #print d;
    if d % 8 == 0:
        return d;
    else:
        return B(d);

a=679;
b=771;
#a=65;
#b=8921;

c=0;
for i in range(5000000):
    a=A(a);
#    print a;
    b=B(b);
#    print b;
    if str(bin(a))[2:].zfill(40)[24:]==str(bin(b))[2:].zfill(40)[24:]:
        c += 1;

print c;


