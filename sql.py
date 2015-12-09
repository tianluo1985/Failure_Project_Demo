import xlrd
import psycopg2
from prepare_data import prepare_a9k_data
import web

_,y,_=prepare_a9k_data('all_freq_aftmanu_1.3.txt',two_class=False,shuffle=False)

conn=psycopg2.connect('dbname=postgres user=postgres')
cur=conn.cursor()


filename='ASR9000_puredata.xlsx'
wb=xlrd.open_workbook(filename)
sh=wb.sheet_by_index(0)


col2=sh.col_values(2)[1:]
col3=sh.col_values(3)[1:]
col4=sh.col_values(4)[1:]
col5=sh.col_values(5)[1:]
col6=sh.col_values(6)[1:]

db=web.database(dbn='postgres',db='postgres',user='postgres')
for i in xrange(len(y)):
	c2=col2[i][1:-1].strip()
	c3=col3[i][1:-1].strip()
	c4=col4[i][1:-1].strip()
	c5=col5[i][1:-1].strip()
	c6=col6[i][1:-1].strip()
	ftext=c2+' '+c3+' '+c4+' '+c5+' '+c6
	print i
	db.insert('asr9000',statement=c2,service_request_title_description=c3,sr_customer_symptom=c4,sr_problem_description=c5,problem_description=c6,full_text=ftext,category=y[i])
	
