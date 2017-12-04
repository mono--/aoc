import math
test= "1212";
l=len(test);
s=0;

for i in range(l-1):
    a=int(test[i])
    b=int(test[(i+(l/2) % l])
    #print("a"+ a)
    #print(b)
    if a==b:
        s=s+b;
a=int(test[l-1]);
b=int(test[0]);
if a==b:
        s=s+b;
print(s);

print(5 % 3)
