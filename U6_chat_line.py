
def read_file(filename):
	dialogue = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			dialogue.append(line.strip())
	return dialogue


def transform(dialogue):
	allen_count = 0
	allen_sticker = 0
	allen_pic = 0
	viki_count = 0
	viki_sticker = 0
	viki_pic = 0
	for line in dialogue:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		words = s[2:]
		if name == 'Allen':
			if s[2] == '貼圖':            # 如果使用 words（s[2:]）會讀不到
				allen_sticker += 1
			elif s[2] == '圖片':
				allen_pic += 1
			else:
				for msg in words:
					allen_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':            # 如果使用 words（s[2:]）會讀不到
				viki_sticker += 1
			elif s[2] == '圖片':
				viki_pic += 1
			else:
				for msg in words:
					viki_count += len(msg)
	print('Allen 說了', str(allen_count), '個字，傳了', str(allen_sticker), '個貼圖和', str(allen_pic), '張圖片。')
	print('Viki 說了', str(viki_count), '個字，傳了', str(viki_sticker), '個貼圖和', str(viki_pic), '張圖片。')


def output(filename, dialogue):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in dialogue:
			f.write(line + '\n')


def main():
	dialogue = read_file('LINE-Viki.txt')
	transform(dialogue)
	# output('LINE-Viki-output.txt', dialogue)


main()
