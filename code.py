import web
import json
import text_analysis_gui as tag
from predict_ml import predict_CPN
import mapping as mp
import database

urls = (
    '/index','index',
    '/test', 'test',
    '/prediction','prediction',
    '/prediction2','prediction2',
    '/classify','classify',
    '/static/(.*)','static',
    '/demo','demo',
    '/search','search',
    '/request','request'
)

name="Qing"
dic=mp.demo_dict
dic_keys=dic.keys()

render = web.template.render('templates/')

class index:
    def GET(self):
        return render.index(name,dic,dic_keys)

class test:
    def GET(self):
    	user_data=web.input()
    	text=' '.join(user_data.values())
    	text=tag.remove_address_info(text)
    	word_freq=tag.calculate_all_text_freq(text)
    	category=predict_CPN(word_freq)
        return category

class prediction:
    def GET(self):
        return render.prediction()

class prediction2:
    def GET(self):
        return render.prediction2(dic_keys,dic)

class classify:
	def GET(self):
		user_data=web.input()
		text=' '.join(user_data.values())
		text=tag.remove_address_info(text)
		word_freq=tag.calculate_all_text_freq(text)
		category,desc=predict_CPN(word_freq)
		img_file='static/img/'+category+'.jpg'
		cpn='Component Number: '+category
		pyDict={"CPN":cpn,"img_file":img_file,"DESC":desc}
		web.header('Content-Type','application/json')
		return json.dumps(pyDict)

class search:
    def GET(self):
#        usr_data=web.input()
        return render.search_index()
#        return json.dumps(usr_data)

class request:
    def GET(self):
        usr_data=web.input()
        return database.get_entry_by_category(usr_data.values()[0])

class static:
    def GET(self,filename):
    	f=open('static'+filename)
        print f.read()

class demo:
    def GET(self):
        return 'this is demo page'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
