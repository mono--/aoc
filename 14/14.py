def reverse(text, repeat):
 knot = list(range(256))
 pos = 0
 skip = 0
 for isntevenused in range(repeat):
      for i in text:
         temp = []
         for j in range(i):
             temp.append(knot[(pos+j) % 256])
         for j in range(i):
             knot[(pos+i-1-j) % 256] = temp[j]
         pos += skip + i
         skip += 1
 return knot


def dense(knot):
 dense = [0]*16
 for i in range(16):
     dense[i] = knot[16*i]
     for m in range(1, 16):
         dense[i] ^= knot[16*i+m]
 return dense


def kh(dense):
 knothash = ''
 for i in dense:
     if len(hex(i)[2:]) == 2:
         knothash += hex(i)[2:]
     else:
         knothash += '0' + hex(i)[2:]
 return knothash

def knot_hash(inp):
	text2 = [];
	for i in range(len(inp)):
		text2.append(ord(inp[i]))
	text2 += [17, 31, 73, 47, 23];
	sparse = reverse(text2, 64);
	d = dense(sparse);
	return kh(d);

#print knot_hash('147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70');
inp="stpzcrnm";
dimension = 15;
hex_hashes=[];
for row in range(dimension+1):
	hex_hashes.append(knot_hash(inp+"-"+str(row)));
bin_hashes=[];

for hh in hex_hashes:
	s="";
	for digit in hh:
		s = s + str(bin(int(digit, 16))[2:].zfill(4));
	print s[:dimension+1];
	bin_hashes.append(list(s)[:dimension+1]);
#print len(bin_hashes[0]);


def neighbours(x,y):
	if x == 0: 
		if y == 0:
			return [[1,0],[0,1]];
		if y == dimension:
			return [[0,dimension-1],[1,dimension]];
		else:
			return [[0,y-1],[0,y+1],[1,y]];
	if x == dimension:
		if y == 0:
			return [[dimension-1,0],[dimension,1]];
		if y == dimension:
			return [[dimension,dimension-1],[dimension-1,dimension]];
		else:
			return [[dimension,y-1],[dimension,y+1],[dimension-1,y]];
	else:
		if y == 0:
			return [[x-1,0],[x+1,0],[x,1]];
		if y == dimension:
			return [[x-1,dimension],[x+1,dimension],[x,dimension-1]];
		else:
			return [[x,y-1],[x,y+1],[x-1,y],[x+1,y]];

def evolve(grid, x,y):
	grid[x][y] = '*';
	for nb in neighbours(x,y):
		if grid[nb[0]][nb[1]] == '1':
			grid = evolve(grid,nb[0],nb[1]);
	return grid;

		
count = 0;

for x in range(dimension+1):
	print str(bin_hashes[x]);
	for y in range(dimension+1):
		s="";
		for t in bin_hashes:
			for u in t:
				s=s+u;
			s=s+"\n";
			print s;
		a=raw_input("");
		if bin_hashes[x][y]=='1':
			count += 1;
			bin_hashes[x][y] = '*';
			bin_hashes = evolve(bin_hashes, x , y);

			
print count;