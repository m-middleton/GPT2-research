from gpt2_client import GPT2Client

gpt2 = GPT2Client('345M')
gpt2.load_model()
my_corpus = './_data/_data_en_es.txt'
genText = gpt2.finetune(my_corpus, return_text=True)