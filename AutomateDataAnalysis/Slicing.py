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

# djson.set_index("ID", inplace = True)

# Employees less then 50000
# print(djson[djson.loc[:, "Salary"] < 50000])

# print(djson[(djson.loc[:, "Salary"] < 50000) | (djson.loc[:, "Salary"] > 56000)])

# print(djson[(djson.loc[:, "Salary"] > 50000) & (djson.loc[:, "Department"] == "Sales")])

# print(djson[(djson.loc[:, "Salary"] > 50000) & (djson.loc[:, "Department"] != "IT")])

# Not working on IT department
# print(djson[~(djson.loc[:, "Department"] == "IT")])

# ----------------------------------------

# Add a row
# djson["Badge ID"] = ["0010","0011","0012","0013","0014","0015","0016","0017","0018","0019" ]
# print(djson)

# djson = djson.append([{"Address": "11th Address, Miami",
                    "Department": "IT",
                    "FirstName": "John",
                    "ID": 11,
                    "LastName": "Doe",
                    "Phone": "09090977",
                    "Salary": "60000",
                    "Skills": "Java",
                    "Badge ID": "0020"},
                    {"Address": "12th Address, Miami",
                    "Department": "IT",
                    "FirstName": "Jake",
                    "ID": 12,
                    "LastName": "Winston",
                    "Phone": "09090988",
                    "Salary": "59000",
                    "Skills": "Python",
                    "Badge ID": "0021"},
                    {"Address": "13th Address, Miami",
                    "Department": "IT",
                    "FirstName": "Jacob",
                    "ID": 13,
                    "LastName": "Mueller",
                    "Phone": "09090999",
                    "Salary": "59600",
                    "Skills": "Routing",
                    "Badge ID": "0022"}], ignore_index = True)
# print(djson)

# djson["Badge ID"] = djson["FirstName"] + "2019"
# print(djson)

# shape return the number of rows and colon
# djson["FirstName"] = djson.shape[0] * ["Jack"]
# print(djson)

# djson.loc[djson["Department"] == "IT", "Salary"] = "9000"
# print(djson)

# djson.loc[(djson["Department"] == "IT") & (djson["Skills"] == "Networking"), "Salary"] = "10000"
# print(djson)

# djson.loc[(djson["ID"] == 9, ["Salary", "Phone"])] = ["800", "77"]
# print(djson)

# ----------------------------------------


#Deleting Rows and Columns

djson.set_index("Badge ID", inplace = True)

#Deleting a row by its name; by default, this command removes a row, if it is found
djson.drop("label")

#Deleting a row explicitly, by passing 0 or 'index' as an argument; drop labels from the index (0 or 'index')
djson.drop("label", 0)
djson.drop("label", "index")
