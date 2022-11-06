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

# cursor.execute('''create table mystaff.employees
#       (id int primary key not null,
#        first_name varchar(25) not null,
#        last_name varchar(25) not null,
#        department varchar(25) not null,
#        phone varchar(25),
#        address varchar(50),
#        salary int);''')

# cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) \
#  values (1, 'John', 'Smith', 'Sales', '0123456789', '1st Street, Miami', 50000), \
#         (2, 'Jack', 'Doe', 'IT', '0213456742', '2nd Street, NY', 55000), \
#         (3, 'Emily', 'Davids', 'Sales', '0123456999', '3rd Street, LA', 59000), \
#         (4, 'Karen', 'Willson', 'Logistics', '0823556785', '4th Street, Las Vegas', 41000), \
#         (5, 'Emma', 'Richard', 'Marketing', '0423453580', '5th Street, Denver', 40000);")


# cursor.execute("update mystaff.employees set department = 'Logistics' where last_name = 'Doe';")

# cursor.execute("delete from mystaff.employees where salary > 50000;")

# cursor.execute("select * from mystaff.employees where salary > 5000")

# records = cursor.fetchall()

# for record in records:
#     print(record)

# cursor.execute("select * from mystaff.employees where salary between 40000 and 45000")

# records = cursor.fetchall()

# for record in records:
#     print(record)

cursor.execute("select * from mystaff.employees where salary between 40000 and 45000")

records = cursor.fetchone()

for record in records:
    print(record)

cursor.execute("select * from mystaff.employees where salary between 40000 and 45000")

records = cursor.fetchmany(size=2)

for record in records:
    print(record)

connection.commit()

connection.close()
