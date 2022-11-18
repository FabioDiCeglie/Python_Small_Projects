import pandas
from sqlalchemy import create_engine

#Loading the TXT file for writing to a new table in the database
# dtxt = pandas.read_csv("./data/my_employees.txt")

# #Loading the CSV file for writing to a new table in the database
# dcsv = pandas.read_csv("./data/my_employees.csv")

# #Loading the JSON file for writing to a new table in the database
# djson = pandas.read_json("./data/my_employees.json")

# #Loading the Excel file for writing to a new table in the database
# dxlsx = pandas.read_excel("./data/my_employees.xlsx", sheet_name = 0)

# #Loading an existing SQL table as a DataFrame for writing to a new table in the database
# #Creating an SQLAlchemy engine (Dialect object + Pool object)
# #More information: https://docs.sqlalchemy.org/en/latest/core/engines.html#engine-configuration
engine = create_engine('postgresql+psycopg2://mihai:python@127.0.0.1:5432/staff')
# dsql = pandas.read_sql_table('employees', engine, schema = 'mystaff')

# dsql.rename({"id": "ID", "first_name": "FirstName", "last_name": "LastName", "department": "Department", "phone": "Phone", "address": "Address", "salary": "Salary"}, axis = 'columns', inplace = True)

# #Writing the scattered data (DataFrames) to a new table in the PostgreSQL database
# dtxt.to_sql('allstaff', engine, schema = 'mystaff', index = False)

# dcsv.to_sql('allstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')

# djson.to_sql('allstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')

# dxlsx.to_sql('allstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')

# dsql.to_sql('allstaff', engine, schema = 'mystaff', index = False, if_exists = 'append')

#Reading SQL queries to DataFrames and building a HTML summary report
#Printing the entire table of employees
query_all = pandas.read_sql_query('SELECT * FROM mystaff.allstaff', engine)

#The total number of employees
query_count = pandas.read_sql_query('SELECT COUNT (*) FROM mystaff.allstaff', engine)
total_employees = query_count.iloc[0][0]
#print(total_employees)

#The total number of departments
query_dept = pandas.read_sql_query('SELECT COUNT(DISTINCT "Department") FROM mystaff.allstaff', engine)
total_depts = query_dept.iloc[0][0]
#print(total_depts)

#The number of employees per department
query_epd = pandas.read_sql_query('SELECT "Department", COUNT("LastName") FROM mystaff.allstaff GROUP BY "Department"', engine)
#print(query_epd)

#Setting the Department as index
query_epd.set_index("Department", inplace = True)

#Number of employees in Logistics
log_emp = query_epd.loc["Logistics", "count"]

#Number of employees in Marketing
mk_emp = query_epd.loc["Marketing", "count"]

#Number of employees in Sales
sls_emp = query_epd.loc["Sales", "count"]

#Number of employees in IT
it_emp = query_epd.loc["IT", "count"]

#Number of employees in HR
# hr_emp = query_epd.loc["HR", "count"]

#Highest salary
sal_high = query_all['Salary'].max()

#Lowest salary
sal_low = query_all['Salary'].min()

#Average salary
sal_avg = query_all['Salary'].mean()


#Joining the above information in a nice format - HTML

summary = [["Total number of employees", int(total_employees)],
           ["Employees in Logistics", int(log_emp)],
           ["Employees in Marketing", int(mk_emp)],
           ["Employees in Sales", int(sls_emp)],
           ["Employees in IT", int(it_emp)],
        #    ["Employees in HR", int(hr_emp)],
           ["Highest salary", int(sal_high)],
           ["Lowest salary", int(sal_low)],
           ["Salary average", int(sal_avg)]]

# print(summary)

summary_html = pandas.DataFrame(summary, columns = ["Stats", "Value"])

# print(summary_html)


#Writing the summary report to HTML format
#More information: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_html.html
with open("./summary.html", "w") as f:
    summary_html.to_html(f, index = False, justify = 'center')



#End of program
