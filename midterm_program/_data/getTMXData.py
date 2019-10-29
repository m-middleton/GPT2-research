from translate.storage.tmx import tmxfile

with open("output_data_en-es.tmx", 'rb') as fin:
	tmx_file = tmxfile(fin, 'en', 'es')


with open('_data_en_es.txt', 'w') as filePtr:
	for node in tmx_file.unit_iter():
		try:
			filePtr.write(node.getsource() + '=' + node.gettarget() + '\n')
		except:
			print(node.getsource(), node.gettarget())