import math;
std=[147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70];

state=range(256);

cur_pos=0;
skip=0;
shifts=std;
for i in shifts:
	#swap beginning at cur_pos; length i
	for j in range(int(math.floor(float(i)/2))):
		#print int(math.floor(float(i)/2));
		buff=state[(cur_pos+j) % 256 ];
		state[(cur_pos+j) % 256 ] = state[(cur_pos+ i-j-1) % 256 ];
		state[(cur_pos+ i-j-1) % 256 ] = buff;
	cur_pos = (cur_pos + skip + i ) % 256;
	skip = (skip + 1 ) % 256;

print state[0]*state[1];

