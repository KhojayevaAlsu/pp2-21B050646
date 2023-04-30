'''
1. Based on PostgreSQL tutorial create PhoneBook:
&Design tables for PhoneBook.
&Implement two ways of inserting data into the PhoneBook.
&upload data from csv file
&entering user name, phone from console
Implement updating data in the table (change user first name or phone)
&Querying data from the tables (with different filters)
&Implement deleting data from tables by username of phone
'''

import psycopg2 

conn = psycopg2.connect(
host = "localhost",
database = "postgre",
user = "postgres",
password = "54916626")

print("1. Add data from console\n2. Upload data from csv file\n3. \
Change data\n4. Querying data from the tables\n5. Delete data")


sql1 = 'select* from phone'
cur = conn.cursor()
choise = input("Choose a number from 1 to 5...")


if choise == "1":
  id = input("Enter user id...")
  name = input("Enter user name...")
  number = input("Enter phone number...")
  add_sql = f"insert into phone (user_id, username, numbers) values ({id}, '{name}' , {number})"
  cur.execute(add_sql)
if choise == "2":
  file = open('phone_numbers.csv', 'r')
  cur.copy_from(file, 'phone', sep =';')
  file.close()
if choise == "3":
    change = input("What do you want to change?")
    if change == "name":
        name = input('Name to set...')
        condition = input('Where do you want to set changes ')
        update_sql = f"update phone set \"username\" = '{name}' where \"numbers\" = '{condition}';"
    if change == "number":
        num = input('Phone number to set...')
        condition = input('Where do you want to set changes ')
        update_sql = f"update phone set \"numbers\" = '{num}' where \"username\" = '{condition}';"
    cur.execute(update_sql)
if choise == "4":
    data_filter = input("Quering data by..")
    if data_filter == "name":
       name = input("Enter user name...")
       sql_q = f"select * from phone where \"username\" in ('{name}');"
       cur.execute(sql_q)
       str1 = cur.fetchall()
       print(str1)
    if data_filter == "number":
       number = input("Enter number...")
       sql_q = f"select * from phone where \"numbers\" in ('{number}');"
       cur.execute(sql_q)
       str2 = cur.fetchone()
       print(str2)
    if data_filter == "id":
       id = input("Enter user id...")
       sql_q = f"select * from phone where \"user_id\" in ('{id}');"
       cur.execute(sql_q)
       str3 = cur.fetchone()
       print(str3)
if choise == "5":
    name = input('Enter user name...')
    delete_sql = f"delete from phone where username = '{name}';"
    cur.execute(delete_sql)



conn.commit()  
print("Record inserted successfully")  
cur.execute(sql1)


numbers = cur.fetchall()
conn.commit()
print(numbers)
conn.close()