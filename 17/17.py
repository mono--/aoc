state=[0];
cur_pos=0;

for i in range(50000001)[1:]:
	#print cur_pos;
	cur_pos = (cur_pos + 337) % len(state);
	state = (state[:cur_pos+1] + [i]) + state[cur_pos+1:];
	cur_pos = (cur_pos +1) % len(state);

print state[0];
print state[1];
