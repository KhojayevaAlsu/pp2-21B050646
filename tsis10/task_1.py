

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

conn.commit()  
print("Record inserted successfully")  

cur.execute('select * from phone where user_id > 5')
stud = cur.fetchall()
print(stud)

cur.execute('select * from phone where numbers/1000 > 1')
st = cur.fetchall()
print(st)

cur.execute("DELETE FROM phone WHERE user_id = 2")
conn.commit()

conn.close()