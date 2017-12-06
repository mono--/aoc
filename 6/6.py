banks=[11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11];
#testcase: banks=(0,2,7,0);
b=len(banks);
cfgs=[];

counter=0;
cfgs.append(banks);
trigger=True;
while trigger:
    banks_new=banks[:];
    e=0;
    for i in range(b):
        if banks_new[i] > e:
            biggest=i; #find index of largest entry
            e=banks_new[biggest];
    banks_new[biggest]=0;
    i=biggest+1; #start distributing at i+1
    while e > 0:
        if i < b:
            banks_new[i]=banks_new[i]+1;
            e=e-1;
            i=i+1;
        else:
            banks_new[0]=banks_new[0]+1;
            i=1;
            e=e-1;
    counter=counter+1;
    if banks_new not in cfgs:
        cfgs.append(banks_new);
        banks=banks_new;
    else:
        trigger=False;
print('total iterations')
print(counter)
print('cycle length')
print counter-cfgs.index(banks_new)


