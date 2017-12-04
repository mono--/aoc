#small example with a 1 factor

spreadsheet="""4	8	3
3	2	2"""


rows=spreadsheet.split('\n');
entries=[];
for row in rows:
	entries.append(row.split('\t'))

s=0;
for row in entries:
	mini=int(row[0])
	maxi=int(row[0])
	for number in row:
		mini=min(mini,int(number))
		maxi=max(maxi,int(number))
	s=s+ (maxi-mini)
print(s);
