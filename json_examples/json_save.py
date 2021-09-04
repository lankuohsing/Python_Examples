# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 00:01:37 2021

@author: lankuohsing
"""

import json
# In[]
dict_example={"1":"a","2":"b"}
# In[]
"""json.dumps"""
json_str = json.dumps(dict_example, indent=4,ensure_ascii=False)
with open("dict_1.json", 'w',encoding='UTF-8') as json_file:
    json_file.write(json_str)
# In[]
"""json dump"""
with open("dict_2.json", 'w',encoding='UTF-8') as wf:
    json.dump(dict_example, wf)