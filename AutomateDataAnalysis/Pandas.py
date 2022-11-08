import pandas

# d = pandas.DataFrame([['Andy',46,'Engineer'], ['Jane',33,'Nurse'], ['Rober',21,'Student'], ['Maria',30,'Student']])

# print(type(d))
# print(d)


# d = pandas.DataFrame([['Andy',46,'Engineer'], ['Jane',33,'Nurse'], ['Rober',21,'Student'], ['Maria',30,'Student']],columns = ["Name", "Age", "Occupation"])
# print(d)

# d = pandas.DataFrame([['Andy',46,'Engineer'], ['Jane',33,'Nurse'], ['Rober',21,'Student'], ['Maria',30,'Student']],columns = ["Name", "Age", "Occupation"], index = ['ID', 'ID2', "ID3", "ID4"])
# print(d)
# print(d.Name)
# print(d.Age.min())

# Read two different files
dtxt = pandas.read_csv("./sample_data/Employees.txt")
print(dtxt)

dtxt2 = pandas.read_csv("./sample_data/Employees2.txt", delimiter= '|')
print(dtxt2)
