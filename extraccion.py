import tweepy as twt
import simplejson as json
import time
from datetime import date, timedelta

CONSUMER_KEY = 'p16pNm4jlUk2gxIVmRjlpBMgC'
CONSUMER_SECRET = 'aJj2lNUU6Z7CpPgqY58CBZfjhNskGSYfFkHeYrDfxynbDpMKaf'
ACCESS_KEY = '2191437690-c4tiRfmBV3NjuofnBK7ZnBkmLRSvNP90RrcQnWl'
ACCESS_SECRET = 'Wt613Xxw3Wozk30QttRVDr72VyXFVWGKbk6fLPTtkQgpd'

auth = twt.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.secure = True

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = twt.API(auth)

i=1
hoy = date.today()
mañana = hoy + timedelta(days=1)
pkey = ['bbva','bancomer','banorte','HSBC']

for tw in twt.Cursor(api.search,
					q = pkey[0]+" OR "+pkey[1]+" OR "+pkey[2]+" OR "+pkey[3],
					count = 100,
					since = hoy, #'2017-03-14'
                           		until = mañana,
					#geocode = '19.4284700,-99.1276600,800mi',
					lang='es').items():

	with open('Data/data'+hoy+'.txt', 'a', encoding='utf8') as f:
  		#json.dump(tw._json, f, ensure_ascii=False, indent=1)
		json.dump(tw._json, f, ensure_ascii=False)	
		f.write('\n')

	print(i, tw.author.name, tw.created_at
)		

	i=i+1



