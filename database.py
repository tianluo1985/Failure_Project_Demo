import web
import json
import numpy as np
from mapping import reverse_map,desc_maps

db=web.database(dbn='postgres',db='postgres',user='postgres')

def fetch_entry(id):
    variable=dict(ID=id)
    res=db.select('asr9000',variable,where="id = $ID")
    entry=res[0]
    dic={'statement': entry.statement,
         'service_request_title_description': entry.service_request_title_description,
         'sr_customer_symptom': entry.sr_customer_symptom,
         'sr_problem_description': entry.sr_problem_description,
         'problem_description': entry.problem_description,
         'full_text': entry.full_text,
         'category': entry.category}
    return json.dumps(dic)

def get_entry_by_category(cate):
    variable=dict(category=cate)
    res=db.select('asr9000new_correct',variable,where="category = $category")
    selection=np.random.randint(len(res))
    case=res[selection]
    cid=case.category
    real_cpn=reverse_map[int(cid)]
    real_desc=desc_maps[real_cpn]
    dic={'statement':case.statement,
         'service_request_title_description':case.service_request_title_description,
         'sr_customer_symptom':case.sr_customer_symptom,
         'sr_problem_description':case.sr_problem_description,
         'problem_description':case.problem_description,
         'full_text':case.full_text,
         'category':case.category,
         'real_CPN':"Component: "+real_cpn,
         'real_DESC':real_desc,
         'fa_number':case.fa_number}
    return json.dumps(dic)
    
