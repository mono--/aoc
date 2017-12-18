def reverse(text, rounds):
 knot = list(range(256))
 pos = 0
 skip = 0
 for r in range(rounds):
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

inp = '147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70';
inpu = [147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70];
input2 = [];

for i in range(len(inp)):
 input2.append(ord(inp[i]))
input2 += [17, 31, 73, 47, 23];

knot = reverse(text, 1)
sparse = reverse(text2, 64)

print str(knot[0]*knot[1])
print kh(dense(sparse))