inp= """0: 4
1: 2
2: 3
4: 5
6: 8
8: 4
10: 6
12: 6
14: 6
16: 10
18: 6
20: 12
22: 8
24: 9
26: 8
28: 8
30: 8
32: 12
34: 12
36: 12
38: 8
40: 10
42: 14
44: 12
46: 14
48: 12
50: 12
52: 12
54: 14
56: 14
58: 14
60: 12
62: 14
64: 14
68: 12
70: 14
74: 14
76: 14
78: 14
80: 17
82: 28
84: 18
86: 14"""

lines=inp.split('\n');

walls=[];

for line in lines:
	walls.append([int(line.split(": ")[0]),int(line.split(": ")[1])]);


print walls

def depth(i):
	for w in walls:
		if w[0] == i:
			return w[1];
	return 0;




caught= True;
delay=0;
while caught == True:
	s= 0;
	for i in range(87):
		if (((i+delay) % ((depth(i)-1)*2)) == 0) and (depth(i) != 0):
			delay += 1;
			#print delay;
			s += 1;
			break;
			print "t"
	if s==0:
		print delay;
		caught= False;
	
	
	
print "Free at last!"
print delay;
	