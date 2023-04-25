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

sql1 = 'select* from phone'
cur = conn.cursor()
choise = input()
if choise == "1":
  id = input()
  name = input()
  number = input()
  cur.execute(f"INSERT INTO PHONE (USER_ID, USERNAME, NUMBERS) VALUES ({id}, '{name}' , {number})")
if choise == "2":
  f = open('phone_numbers.csv', 'r')
  cur.copy_from(f, 'phone', sep =';')
  f.close()
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
    data_filter = input('Enter filter...')
    sql1 = f"select * from phone where {data_filter};"
    cur.execute(sql1)
if choise == "5":
    name = input('Enter user name...')
    delete_sql= f"delete from phone where name = '{name}';"
    cur.execute(delete_sql)




conn.commit()  
print("Record inserted successfully")  
cur.execute(sql1)



numbers = cur.fetchall()
conn.commit()
print(numbers)
conn.close()