import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import os
import re
from sklearn.utils import shuffle

#os.chdir('/Users/tluo2/playground/')

#datas=pd.read_csv('ServiceRequestProblemStatement.csv')
def prepare_a9k_data(file_name,two_class=True,shuffle=True):
	labels=pd.read_csv('ASR9000_lable.txt',header=None)
	labels=labels.values
	#datas=datas.values
	#datas=datas.transpose()

	data5=pd.read_csv(file_name,header=None)
	data5=data5.values
	data5=data5[1:]

	from sklearn.feature_extraction.text import TfidfTransformer

	transformer=TfidfTransformer()
	transformer=transformer.fit(data5)
	X=transformer.transform(data5)

	tags=[]
	for i in xrange(len(labels)):
		segs=labels[i][0].split('-')
		tags.append(segs[0][1:])

	maps_ac={'08':0,
	 '11':1,
	 '12':2,
	 '13':3,
	 '14':4,
	 '15':5,
	 '16':6,
	 '17':7,
	 '19':8,
	 '20':9,
	 '21':10,
	 '23':11,
	 '24':12,
	 '25':13,
	 '26':14,
	 '27':15,
	 '28':16,
	 '29':17,
	 '33':18,
	 '34':19,
	 '341':20,
	 '49':21,
	 '51':22,
	 '58':23,
	 '68':24,
	 '700':25,
	 '72':26,
	 '73':27,
	 '800':28}

	maps_2c={'08':0,
	 '11':0,
	 '12':0,
	 '13':0,
	 '14':0,
	 '15':1,
	 '16':0,
	 '17':0,
	 '19':0,
	 '20':0,
	 '21':0,
	 '23':0,
	 '24':0,
	 '25':0,
	 '26':0,
	 '27':0,
	 '28':0,
	 '29':0,
	 '33':0,
	 '34':0,
	 '341':0,
	 '49':0,
	 '51':0,
	 '58':0,
	 '68':0,
	 '700':0,
	 '72':0,
	 '73':0,
	 '800':0}
	if two_class:
		maps=maps_2c
	else:
		maps=maps_ac

	labels=[]

	for i in xrange(len(tags)):
		labels.append(maps[tags[i]])


	X=X.toarray()
	y=np.asarray(labels)

	if shuffle:
		X,y=shuffle(X,y,random_state=0)
	return (X,y,transformer)


def prepare_a9k_raw_data(file_name,two_class=True,remove_first_row=False):
	labels=pd.read_csv('ASR9000_lable.txt',header=None)
	labels=labels.values
	#datas=datas.values
	#datas=datas.transpose()

	#data5=pd.read_csv(file_name,header=None)
	#data5=data5.values
	data5=np.loadtxt(file_name,delimiter=',')
	if remove_first_row:
		data5=data5[1:]

	#from sklearn.feature_extraction.text import TfidfTransformer

	#transformer=TfidfTransformer()
	#X=transformer.fit_transform(data5)
	X=data5
	tags=[]
	for i in xrange(len(labels)):
		segs=labels[i][0].split('-')
		tags.append(segs[0][1:])

	maps_ac={'08':0,
	 '11':1,
	 '12':2,
	 '13':3,
	 '14':4,
	 '15':5,
	 '16':6,
	 '17':7,
	 '19':8,
	 '20':9,
	 '21':10,
	 '23':11,
	 '24':12,
	 '25':13,
	 '26':14,
	 '27':15,
	 '28':16,
	 '29':17,
	 '33':18,
	 '34':19,
	 '341':20,
	 '49':21,
	 '51':22,
	 '58':23,
	 '68':24,
	 '700':25,
	 '72':26,
	 '73':27,
	 '800':28}

	maps_2c={'08':0,
	 '11':0,
	 '12':0,
	 '13':0,
	 '14':0,
	 '15':1,
	 '16':0,
	 '17':0,
	 '19':0,
	 '20':0,
	 '21':0,
	 '23':0,
	 '24':0,
	 '25':0,
	 '26':0,
	 '27':0,
	 '28':0,
	 '29':0,
	 '33':0,
	 '34':0,
	 '341':0,
	 '49':0,
	 '51':0,
	 '58':0,
	 '68':0,
	 '700':0,
	 '72':0,
	 '73':0,
	 '800':0}
	if two_class:
		maps=maps_2c
	else:
		maps=maps_ac

	labels=[]

	for i in xrange(len(tags)):
		labels.append(maps[tags[i]])


	#X=X.toarray()
	y=np.asarray(labels)


	X,y=shuffle(X,y,random_state=0)
	return (X,y)
