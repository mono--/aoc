inp_test= """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d""";

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

#registers

regs0 = {"p":0};
regs1 = {"p":1};


def val0(s):
	if s in "abcdefghijklmnopqrstuvwxyz":
		return int(regs0.get(s, 0));
	else:
		return int(s);

def val1(s):
	if s in "abcdefghijklmnopqrstuvwxyz":
		return int (regs1.get(s, 0));
	else:
		return int (s);

#message queues

qu0 = [];
qu1 = [];

#program counters

i = 0;
j=0;

#waiting for messages

wait0 = False;
wait1= False;

# counting "sends" for thread1
ctr= 0;

#no threat is waiting

while wait0 == False or wait1 == False:
	cmd=lines[i].split(' ');
	if cmd[0]=="set":
		regs0.update({str(cmd[1]):val0(cmd[2])});	
	if cmd[0]=="add":
		buf=regs0.get(cmd[1], 0) + val0(cmd[2]);
		regs0.update ({str(cmd[1]): int(buf)});
	if cmd[0]=="mul":
		buf = int (regs0.get(cmd[1], 0)) * int(val0(cmd[2]));
		regs0.update({str(cmd[1]): buf});
	if cmd[0]=="snd":
		qu1.append(val0(cmd[1]));
	if cmd[0]=="mod":
		buf=regs0.get(cmd[1], 0) % val0(cmd[2]);
		regs0.update ({str(cmd[1]): int(buf)});
	if cmd[0]=="rcv":
		if len(qu0) == 0:
			wait0 = True;
			#dont advance the prg-counter
			i += -1;
		if len(qu0) != 0:
			wait0 = False;
			v=qu0[0];
			qu0=qu0[1:];
			regs0.update({str(cmd[1]):v})

	if cmd[0]=="jgz" and val0(cmd[1]) > 0:
		i += val0(cmd[2]) - 1;
	i += 1;

	cmd=lines[j].split(' ');
	if cmd[0]=="set":
		regs1.update({str(cmd[1]):val1(cmd[2])});
	if cmd[0]=="add":
		buf=int (regs1.get(cmd[1], 0)) + int(val1(cmd[2]));
		regs1.update ({str(cmd[1]): int(buf)});
	if cmd[0]=="mul":
		buf=int (regs1.get(cmd[1], 0)) * int(val1(cmd[2]));
		regs1.update ({str(cmd[1]): int(buf)});
	if cmd[0]=="snd":
		qu0.append(val1(cmd[1]));
		ctr += 1;
	if cmd[0]=="mod":
		buf=int(regs1.get(cmd[1], 0)) % int(val1(cmd[2]));
		regs1.update ({str(cmd[1]): int(buf)});
	if cmd[0]=="rcv":
		if len(qu1) == 0:
			wait1 = True;
			j += -1;
		if len(qu1) != 0:
			wait1 = False;
			v=qu1[0];
			qu1=qu1[1:];
			regs1.update({str(cmd[1]):v})

	if cmd[0]=="jgz" and val1(cmd[1]) > 0:
		j += val1(cmd[2]) - 1;
	j += 1;

print "asd";
print ctr;
	