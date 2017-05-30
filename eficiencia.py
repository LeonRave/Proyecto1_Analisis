import simplejson as json
import nltk
import limpieza as lm
from textblob.classifiers import NaiveBayesClassifier


print("Cargando datos de entrenamiento")
train = []
i=0
for twit in open('Data/train.txt', 'r'):
	train.append((json.loads(twit)['texto'],json.loads(twit)['opinion']))
	#print(i,twit)
	i=i+1

test = []
i=0
for twit in open('Data/test.txt', 'r'):
	test.append((json.loads(twit)['texto'],json.loads(twit)['opinion']))
	#print(i,twit)
	i=i+1

print("Entrenando clasificador (calculando probabilidad condicional)")
cl = NaiveBayesClassifier(train)
cl.labels()

print("CLasificando los datos de test")
print("La eficiencia es de: "+ str(cl.accuracy(test)))


