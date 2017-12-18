state = 1;
cur_pos=0;

for i in range(50000001)[1:]:
	#print cur_pos;
	cur_pos = (cur_pos + 337) % state;
	if cur_pos == 0:
		print i;
	state += 1;
	cur_pos = (cur_pos +1) % state;