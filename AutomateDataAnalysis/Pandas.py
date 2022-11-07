import pandas

# d = pandas.DataFrame([['Andy',46,'Engineer'], ['Jane',33,'Nurse'], ['Rober',21,'Student'], ['Maria',30,'Student']])

# print(type(d))
# print(d)


# d = pandas.DataFrame([['Andy',46,'Engineer'], ['Jane',33,'Nurse'], ['Rober',21,'Student'], ['Maria',30,'Student']],columns = ["Name", "Age", "Occupation"])
# print(d)

d = pandas.DataFrame([['Andy',46,'Engineer'], ['Jane',33,'Nurse'], ['Rober',21,'Student'], ['Maria',30,'Student']],columns = ["Name", "Age", "Occupation"], index = ['ID', 'ID2', "ID3", "ID4"])
print(d)
