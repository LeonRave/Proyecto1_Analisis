import simplejson as json
import re
import nltk
import unicodedata
from textblob.classifiers import NaiveBayesClassifier

#Diccionarios para eliminar stopwords y regresar palabras a su raiz
stopword = nltk.corpus.stopwords.words('spanish')
stemmer = nltk.stem.SnowballStemmer("spanish")

def eliminaURL(s):

	while(True):
		if s.find('http')<0:
			break
		
		else:
			n = s.find('http')
			i = 0
			try:
		    		while s[n+i]!=' ':
		        		i=i+1
			except:
		    		i=i   

			if s[n-1] == ' ':
		    		url = s[n:n+i]
		    		s = s.replace(s[n-1:n+i],'')
			else:
		    		url = s[n:n+i]
		    		s = s.replace(s[n:n+i],'')
	return s

def elimina_acentos(s):
	return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def elimina_puntuacion(s):
	return re.sub('\W+', ' ',s)

def pasa_minusculas(s):
	return s.lower()

def quita_raiz_stopwords(s):
	texto = ""
	for j in [i for i in s.split() if i not in stopword]:
		texto = texto +" "+ stemmer.stem(j)
	return texto

tweets = []
i=0
for twiit in open('Data/entrenar1.txt', 'r'):
	tweets.append(json.loads(twiit))
	text = tweets[i]['text'].encode('utf8').decode('utf8', 'ignore')
	text = eliminaURL(text)
	text = elimina_acentos(text)
	text = elimina_puntuacion(text)
	text = pasa_minusculas(text)
	#text = quita_raiz_stopwords(text)
	id = tweets[i]['id']
	print(i, id, text)

	with open('Data/train.txt', 'a', encoding='utf8') as f:
		dic={"texto": text, "opinion": "positiva"}
		json.dump(dic, f, ensure_ascii=False)
		f.write('\n')
	
	i=i+1

tweets = []
i=0
for twiit in open('Data/entrenar2.txt', 'r'):
	tweets.append(json.loads(twiit))
	text = tweets[i]['text'].encode('utf8').decode('utf8', 'ignore')
	text = eliminaURL(text)
	text = elimina_acentos(text)
	text = elimina_puntuacion(text)
	text = pasa_minusculas(text)
	#text = quita_raiz_stopwords(text)
	id = tweets[i]['id']
	print(i, id, text)

	with open('Data/test.txt', 'a', encoding='utf8') as f:
		dic={"texto": text, "opinion": "positiva"}
		json.dump(dic, f, ensure_ascii=False)
		f.write('\n')
	
	i=i+1



