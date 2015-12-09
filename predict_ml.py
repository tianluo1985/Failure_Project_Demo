from sklearn.externals import joblib
#import pickle

def predict_num(word_freq):
	svm=joblib.load('Project/svm_demo.pkl')
	tfidf=joblib.load('Project/transformer.pkl')
	vector=tfidf.transform(word_freq)
	pred_res=svm.predict(vector)
	return pred_res

def predict_CPN(word_freq):
	svm=joblib.load('Project/svm_demo.pkl')
	tfidf=joblib.load('Project/transformer.pkl')
#	f_svm=open('/var/www/html/project/svm.txt')
#	f_tfidf=open('/var/www/html/project/tfidf.txt')
#	svms=f_svm.read()
#	tfidfs=f_tfidf.read()
#	f_svm.close()
#	f_tfidf.close()
#	svm=pickle.loads(svms)
#	tfidf=pickle.loads(tfidfs)
	vector=tfidf.transform(word_freq)
	pred_res=svm.predict(vector)

	maps={'08':0,
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

	desc_maps={'08':'ASIC (Application-Specific INtegrated circuit)',
	 '11':'Capacitors',
	 '12':'Resistors',
	 '13':'Diodes',
	 '14':'Resistor Networks',
	 '15':' MPU (Memory Protection Unit),DRAM (Dynamic Random Addressable Memory),DIMM (Dual In-line Memory Module),DDR ...',
	 '16':'PLD (Programmable Logic Device),FPGA (Field Programmable Gate Array),EPROM (Erasable Programmable Read Only Memory),Flash Memory,SSD ( Solid State Disk)',
	 '17':'Programmed PLD/ Programmed Flash',
	 '19':'Crystals/ Oscillators',
	 '20':'Transistor',
	 '21':'Circuit Protection and Filter',
	 '23':'Relays',
	 '24':'Magnetic/Inductors/toroids/transformers',
	 '25':'LED',
	 '26':'Sockets',
	 '27':'Receptacle/Headers',
	 '28':'PCB (Printed Wire Board)',
	 '29':'Connectors',
	 '33':'Fafns and Blowers',
	 '34':'Power Supplies',
	 '341':'Off-line Front End AC/DC',
	 '49':'Nuts Washers',
	 '51':'Heat Sink',
	 '58':'Hard Disk Drive',
	 '68':'',
	 '700':'',
	 '72':'',
	 '73':'',
	 '800':''}

	reverse_map={y:x for x,y in maps.iteritems()}
	"""reverse_map={0:'08',1:'11',2:'12',3:'13',4:'14',5:'15',6:'16',7:'17',8:'19',9:'20',
		     10:'21',11:'23',12:'24',13:'25',14:'26',15:'27',16:'28',17:'29',18:'33',
		     19:'34',20:'341',21:'49',22:'51',23:'58',24:'68',25:'700',26:'72',27:'73',28:'800'}"""
	cpn=reverse_map[pred_res[0]]
	return (reverse_map[pred_res[0]],desc_maps[cpn])
