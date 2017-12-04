import sys

trigger=361527;

#make plenty of space :-)
grid=[]
for i in range(1000):
	grid.append([])
	for j in range(1000):
		grid[i].extend([0])


#initial 1 is at position (500:500)
i=500
j=500
grid[500][500]=1


#counting neighbouring points
def neigh(i,j):
	s=0;
	s=s+(grid[i-1][j-1]);
	s=s+(grid[i-1][j]);
	s=s+(grid[i-1][j+1]);
	s=s+(grid[i][j-1]);
	s=s+(grid[i][j+1]);
	s=s+(grid[i+1][j-1]);
	s=s+(grid[i+1][j]);
	s=s+(grid[i+1][j+1]);
	#if we stumble over the end-trigger: abort
	if s > trigger:
		print s;
		sys.exit();
	return s;

#set the length of a spiral arm
k=1

for counter in range(10): #number of spiral rounds; we start at the lower left side. 
	#go round 1 time
	for t in range(k):
		grid[i+t+1][j]=neigh(i+t+1,j)
	for t in range(k):
		grid[i+k][j+t+1]=neigh(i+k,j+t+1)
	for t in range(k+1):
		grid[i+k-t-1][j+k]=neigh(i+k-t-1,j+k)
	for t in range(k+1):
		grid[i-1][j+k-t-1]=neigh(i-1,j+k-t-1)
	#update lower-left corner coo's and arm-length
	i=i-1
	j=j-1
	k=k+2

