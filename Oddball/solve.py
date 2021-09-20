def bin2text(b):
	return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

o = ''
lines = ''
with open("oddball.txt") as f:
    lines = f.readlines()
for line in lines:
    o += ''.join(line.rstrip().split(' ')[1:])

s = ''
for i in o:
    s += "{0:03b}".format(int(i))

j = 0
txt = ''
while j < len(s):
    j += 2
    txt += s[(j+8):(j+16)]
    txt += s[j:j+8]
    j += 16

print(bin2text(txt))
