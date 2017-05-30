import simplejson as json
import nltk
import limpieza as lm
from textblob.classifiers import NaiveBayesClassifier


class Clasificador(object):

	#Constructores
	def __init__(self):
		self.__cl = None
		print("Cargando datos de entrenamiento")
		train = []
		i=0
		for twit in open('Data/train.txt', 'r'):
			train.append((json.loads(twit)['texto'],json.loads(twit)['opinion']))
			print(i,twit)
			i=i+1

		print("Entrenando clasificador (calculando probabilidad condicional)")
		self.__cl = NaiveBayesClassifier(train)
		print(self.__cl.labels())

	#Metodos
	def clasif(self, texto):

		texto = lm.eliminaURL(texto)
		texto = lm.elimina_acentos(texto)
		texto = lm.elimina_puntuacion(texto)
		texto = lm.pasa_minusculas(texto)
		return self.__cl.classify(texto)


#Creacion Objeto e inicio programa


#texto = "Bienvendido al estadio BBVA"

#crudoT = Clasificador()
#print(crudoT.clasif(texto))

