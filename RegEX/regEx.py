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
result.group(3)
# Traceback (most recent call last):
#   File "<pyshell#92>", line 1, in <module>
#     result.group(3)
# IndexError: no such group
