
def read_file(filename):
	dialogue = []
	new = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			dialogue.append(line.strip('\n'))
	for line in dialogue:
		s = line.split(' ')
		time = s[0][:5]
		name = s[0][5:]
		new.append(time + ' ' + name + ' ' + s[1])
	return new	


def output(filename, dialogue):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in dialogue:
			f.write(line + '\n')


def main():
	dialogue = read_file('3.txt')
	# transform(dialogue)
	output('3-output.txt', dialogue)


main()
