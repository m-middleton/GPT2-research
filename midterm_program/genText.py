from gpt2_client import GPT2Client
gpt2 = GPT2Client('117M')
gpt2.load_model()

#inputText = 'Trump is building a wall. A big wall. To stop CHINA from taking our jobs. Make America Great again!'
genText = gpt2.generate(interactive=True, n_samples=1, return_text=True)
#genText = gpt2.generate(return_text=True)

with open('test.txt', 'a') as filePtr:
    #filePtr.write(inputText + '\n')
    for line in genText:
    	filePtr.write( line + '\n')
    filePtr.write('\n')