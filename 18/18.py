inp= """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 622
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19""";

lines=inp.split('\n');

regs0 = {"p":0};
regs1 = {"p":1};


def val0(s):
	if s in "abcdefghijklmnopqrstuvwxyz":
		return int (regs0.get(s, 0));
	else:
		return int (s);

def val1(s):
	if s in "abcdefghijklmnopqrstuvwxyz":
		return int (regs1.get(s, 0));
	else:
		return int (s);



qu0 = [];
qu1 = [];

i = 0;
j=0;

Stop = False;

while i < len(lines) and j < len(lines) and wait0 = False:
	cmd=lines[i].split(' ');
	print cmd;
	if cmd[0]=="set":
		regs0.update({str(cmd[1]):val0(cmd[2])});
		print regs[cmd[1]];		
	if cmd[0]=="add":
		buf=regs0.get(cmd[1], 0) + val0(cmd[2]);
		regs0.update ({str(cmd[1]): int(buf)});
		print regs[cmd[1]];
	if cmd[0]=="mul":
		buf=regs0.get(cmd[1], 0) * val0(cmd[2]);
		regs0.update ({str(cmd[1]): int(buf)});
		print regs0[cmd[1]];
	if cmd[0]=="snd":
		qu1.append(val0(cmd[1]));
		print "qu1=" + str(qu1);
	if cmd[0]=="mod":
		buf=regs0.get(cmd[1], 0) % val0(cmd[2]);
		regs0.update ({str(cmd[1]): int(buf)});
		print regs0[cmd[1]];
	if cmd[0]=="rcv":
		print "rcv";
		if len(qu0) == 0:
			wait0 = True;
			i += -1;
		if len(qu0) != 0:
			v=qu0[0];
			qu0=qu0[1:];
			regs1.update({str(cmd[1]):v})
			#Stop = True;
		######
	if cmd[0]=="jgz" and val0(cmd[1]) > 0:
		i += val0(cmd[2]) - 1;
		print "jumped to "+ str(i);
	print regs;
	i += 1;

	cmd=lines[j].split(' ');
	print cmd;
	if cmd[0]=="set":
		regs0.update({str(cmd[1]):val1(cmd[2])});
		print regs[cmd[1]];		
	if cmd[0]=="add":
		buf=regs0.get(cmd[1], 0) + val1(cmd[2]);
		regs0.update ({str(cmd[1]): int(buf)});
		print regs[cmd[1]];
	if cmd[0]=="mul":
		buf=regs0.get(cmd[1], 0) * val1(cmd[2]);
		regs0.update ({str(cmd[1]): int(buf)});
		print regs0[cmd[1]];
	if cmd[0]=="snd":
		qu0.append(val1(cmd[1]));
		print "qu1=" + str(qu1);
	if cmd[0]=="mod":
		buf=regs0.get(cmd[1], 0) % val1(cmd[2]);
		regs0.update ({str(cmd[1]): int(buf)});
		print regs0[cmd[1]];
	if cmd[0]=="rcv":
		print "rcv";
		if len(qu0) == 0:
			wait0 = True;
			j += -1;
		if len(qu0) != 0:
			v=qu0[0];
			qu0=qu0[1:];
			regs1.update({str(cmd[1]):v})
			#Stop = True;
		######
	if cmd[0]=="jgz" and val1(cmd[1]) > 0:
		i += val1(cmd[2]) - 1;
		print "jumped to "+ str(i);
	print regs;
	j += 1;
	