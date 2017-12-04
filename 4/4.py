import sets
phrases="""asd das""";

rows=phrases.split('\n');
words=[]
for row in rows:
	words.append(row.split(' '))
valid=0;



for row in words:
	wordset=set(row);
	if len(wordset)==len(row):
		valid=valid+1;
	else:
		print(row)
		print(len(wordset))
print valid
