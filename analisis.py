import analizador as an
import limpieza as l
import simplejson as json
import os
import re

#Instanciar y crear el objeto clasificador
crudoT = an.Clasificador()

#Guardando el nombre de lso archivos a leer en una liesta
archivo = (os.popen('ls Data | grep dataW').read()).split("\n")
archivo.pop()

#Buffer de los datos
tweets = []

for ar in archivo:

	i=0
	print("Archivo: ", ar)
	for twiit in open('Data/'+ar, 'r'):
		tweets.append(json.loads(twiit))
		source = tweets[i]['source']
		author = tweets[i]['user']['screen_name']
		location = tweets[i]['user']['location']
		followers = tweets[i]['user']['followers_count']
		timestamp = tweets[i]['created_at']
		message = tweets[i]['text'].encode('utf8').decode('utf8', 'ignore')
		message = l.eliminaURL(message)
		message = l.elimina_acentos(message)
		message = l.elimina_puntuacion(message)
		message = l.pasa_minusculas(message)
	
		with open('Data/DatosAnalizados.txt', 'a', encoding='utf8') as f:
			dic={"source": source,
			     "author": author,
			     "location": location,
			     "followers": followers,
			     "timestamp": timestamp,
			     "message": message,
			     "sentiment": crudoT.clasif(message)}
			json.dump(dic, f, ensure_ascii=False)
			f.write('\n')
	
		i=i+1


