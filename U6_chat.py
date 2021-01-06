
def read_file(filename):
	dialogue = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			dialogue.append(line.strip())
	return dialogue

def transform(dialogue):
	new = []
	person = None
	for line in dialogue:
		if line == 'Allen':
			person = line
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + '：' + line)
	return new

def output(filename, dialogue):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in dialogue:
			f.write(line + '\n')

def main():
	dialogue = read_file('input.txt')
	dialogue = transform(dialogue)
	output('output.txt', dialogue)

main()
