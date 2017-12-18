import math;

standard_shift=[147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70];

def hash_str(s):
	state=range(256);
	cur_pos=0;
	skip=0;
	ints=[];
	for letter in s:
		print ord(letter);
		ints.append(ord(letter));
	ints.extend(standard_shift);
	#print ints;
	for r in range(64): #number of rounds
		for i in ints:
			for j in range(int(math.floor(float(i)/2))):
				buff=state[(cur_pos+j) % 256 ];
				state[(cur_pos+j) % 256 ] = state[(cur_pos+ i-j-1) % 256 ];
				state[(cur_pos+ i-j-1) % 256 ] = buff;
			cur_pos = (cur_pos + skip + i ) % 256;
			skip = (skip + 1 ) % 256;
		#print state[0]*state[1];
	return state;



def dense(st):
	den_hs="";
	print st;
	for i in range(16):
		d_num= st[16*i:16*(i+1)];
		print "dnum"
		print d_num;
		d = d_num[0];
		for e in d_num[1:]:
			d = d ^ e;
		if len(hex(d)[2:])==1:
			den_hs = den_hs + "0" + hex(d)[2:];
		else:
			den_hs = den_hs+ hex(d)[2:];
	return den_hs;

print dense(hash_str(""));