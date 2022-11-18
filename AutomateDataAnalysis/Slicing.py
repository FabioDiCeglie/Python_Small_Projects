import pandas

# Indexing and Slicing Tables with Pandas
#Loading a JSON file from the current directory
djson = pandas.read_json("./sample_data/Employees.json")
# print(djson)

# print(djson.loc[[2,4,7]])

# print(djson.loc[3:5])

# print(djson.loc[0:2,"Phone": "Skills"])

# -------------------------------------

# Change index
# djson.set_index("Address", inplace = True)
# print(djson)

# print(djson.loc["1st Address, Miami": "5th Address, Miami"])
# print(djson.loc["1st Address, Miami": "5th Address, Miami", "Phone"])
# print(djson.loc["1st Address, Miami": "5th Address, Miami", ["LastName", "Skills"]])
# print(djson.loc["1st Address, Miami": "5th Address, Miami", "LastName": "Skills"])
# print(djson.loc["1st Address, Miami", "Phone"])

# All phone numbers for all the addresses
# print(djson.loc[:, "Phone"])

# All tables
# print(djson.loc[:,:])

# print(set(djson.loc[:,"Department"])) {'Logistics', 'Sales', 'Marketing', 'IT'}


# ----------------------------------------

# iloc method we can slice tables differently

# print(djson.iloc[[4,6,8]])

# print(djson.iloc[2, 2:5])

# print(djson.iloc[:, 2:5])


# ----------------------------------------

# sample method

# print(djson.sample())
# print(djson.sample(n = 4))

# Random return
# print(djson.sample(frac = 0.2))


# ----------------------------------------

# Condition

djson.set_index("ID", inplace = True)

# Employees less then 50000
# print(djson[djson.loc[:, "Salary"] < 50000])

# print(djson[(djson.loc[:, "Salary"] < 50000) | (djson.loc[:, "Salary"] > 56000)])

# print(djson[(djson.loc[:, "Salary"] > 50000) & (djson.loc[:, "Department"] == "Sales")])

# print(djson[(djson.loc[:, "Salary"] > 50000) & (djson.loc[:, "Department"] != "IT")])

# Not working on IT department
print(djson[~(djson.loc[:, "Department"] == "IT")])
