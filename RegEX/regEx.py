string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% the worst day since it launched in 1998.The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

import re
result = re.search(r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
result.groups()
('index', 'FTSE', '19 February')
result.group(1)
'index'
result.group(2)
'FTSE'
result.group(3)
'19 February'
result = re.search(r".+(?:\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
result.groups()
('FTSE', '19 February')
result.group(1)
'FTSE'
result.group(2)
'19 February'

result = re.search(r".+(?P<wordex>\b.+ex\b).+(?P<uppercase>\b[A-Z]{4}\b).+(?P<date>\d\d\s.+)\.", string)
result.groups()
('index', 'FTSE', '19 February')
result.group("wordex")
'index'
result.group("uppercase")
'FTSE'
result.group("date")
'19 February'
result.group(1)
'index'
result.group(2)
'FTSE'
result.group(3)
'19 February'
result.groupdict()
{'wordex': 'index', 'uppercase': 'FTSE', 'date': '19 February'}
result = re.findall(r"[A-Z]{5}\s(?=[0-9]{3})", string)
result
['STOXX ', 'STOXX ']
result = re.findall(r"([A-Z]{5})\s(?=[0-9]{3})", string)
result
['STOXX', 'STOXX']
result = re.findall(r"Euro(?=[a-z]+)", string)
result
['Euro']
