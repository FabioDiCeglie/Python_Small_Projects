import psycopg2

try:
    connection = psycopg2.connect(database="staff", user="mihai", password='python', host= '127.0.0.1', port='5432')

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("Connection to database was successful!")

# Creating databases tables with Python

# Cursor is a dedicated structure that allow us to traverse the records of a database
cursor = connection.cursor()

cursor.execute('''create table mystaff.employees
      (id int primary key not null,
       first_name varchar(25) not null,
       last_name varchar(25) not null,
       department varchar(25) not null,
       phone varchar(25),
       address varchar(50),
       salary int);''')


connection.commit()

connection.close()
