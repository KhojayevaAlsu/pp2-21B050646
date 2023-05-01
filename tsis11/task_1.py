'''Function that returns all records based on a pattern 
(example of pattern: part of name, surname, phone number)
Create procedure to insert new user by name and phone, update phone if user already exists
Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. 
Check correctness of phone in procedure and return all incorrect data.
Create function to querying data from the tables with pagination (by limit and offset)
Implement procedure to deleting data from tables by username or phone'''


import psycopg2 

conn = psycopg2.connect(
host = "localhost",
database = "postgre",
user = "postgres",
password = "54916626")

print("1. Add data from console\n2. Upload data from csv file\n3. \
Change data\n4. Querying data from the tables\n5. Delete data\n6. All records based on a pattern\n7. \
Insert many new users by name and phone\n8. insert many new users by list of name and phone\n9. \
Check correctness of phone\n10. \
Querying data from the tables with pagination\n11. Delete data by username or phone")


sql1 = 'select* from phone'
cur = conn.cursor()
choiсe = input("Choose a number from 1 to 11...")


if choiсe == "1":
  id = input("Enter user id...")
  name = input("Enter user name...")
  number = input("Enter phone number...")
  add_sql = f"insert into phone (user_id, username, numbers) values ({id}, '{name}' , {number})"
  cur.execute(add_sql)
if choiсe == "2":
  file = open('phone_numbers.csv', 'r')
  cur.copy_from(file, 'phone', sep =';')
  file.close()
if choiсe == "3":
    change = input("What do you want to change?")
    if change == "name":
        name = input("Name to set...")
        condition = input("Where do you want to set changes ")
        update_sql = f"update phone set \"username\" = '{name}' where \"numbers\" = '{condition}';"
    if change == "number":
        num = input('Phone number to set...')
        condition = input("Where do you want to set changes ")
        update_sql = f"update phone set \"numbers\" = '{num}' where \"username\" = '{condition}';"
    cur.execute(update_sql)
if choiсe == "4":
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
if choiсe == "5":
    name = input("Enter user name...")
    delete_sql = f"delete from phone where username = '{name}';"
    cur.execute(delete_sql)
if choiсe == "6":
    pattern = input("Enter pattern... ")
    search = input("Search in... ")
    '''if search == "name":
       search_sql = f"select (user_id, username, numbers) from phone where \"username\" like '%{pattern}%';"
       cur.execute(search_sql)
    if search == "number":
       number = input("Enter number...")
       search_sql = f"select (user_id, username, numbers) from phone where where \"numbers\" like '%{pattern}%';"
    if search == "id":
       search_sql = f"select (user_id, username, numbers) from phone where where \"user_id\" like '%{pattern}%';"'''
    search_sql = f"select * from phone where \"{search}\" like '%{pattern}%';"
    cur.execute(search_sql)
    str_search = cur.fetchall()
    print(str_search)
if choiсe == "7":
    id = input("Enter id... ")
    name = input("Enter name... ")
    phone_number = input("Enter phone number...")
    cur.execute(f"select * from from phone where \"username\" like '%{pattern}%';")
    print(len(cur.fetchall()))
    if len(cur.fetchall()) > 0 :
        cur.execute(f"update phone set \"username\" = '{name}' where \"user_id\" = '{id}';")
        cur.execute(f"update phone set \"numbers\" = '{name}' where \"user_id\" = '{id}';")
    else:
        cur.execute(f"insert into phone (user_id, username, numbers) values ({id}, '{name}', {number});")
if choiсe == "8":
    phone_list = [('123', 'Lera', '98707166374'), ('145','Katya',  '987476925109'), ('54','Kiril',  '987775554433'), ('79','Tolya', '977479541961')]
    for i in range(len(phone_list)):
        cur.execute(f"insert into phone values {phone_list[i]}")
if choiсe == "9":
    pattern = '8__________'
    incorrect_sql = "select (user_id, username, numbers) from phone where \"numbers\" not like '%{pattern}%';"
    cur.execute(incorrect_sql)
    print("Incorrect:", cur.fetchall())
    cur.execute("delete from phone where  \"numbers\" not like '%{pattern}%'")
if choiсe == "10":
    order = input("Order by... ")
    limit = input("Limit... ") 
    offset = input("Offset...") 
    query_sql = f"select * from phone order by {order} limit {limit} offset {offset};"  
    cur.execute(query_sql)
    str_query = cur.fetchall()
    print(str_query)     
if choiсe == "11":
    pattern = input("By what delete...")
    condition = input("Data to delete ")
    delete_sql = f"delete from phone where  \"{condition}\" like '%{pattern}%'"
    cur.execute(delete_sql)
    conn.commit()
    cur.execute(sql1)



conn.commit()  
print("Record inserted successfully")  
cur.execute(sql1)


numbers = cur.fetchall()
conn.commit()
print(numbers)
print(len(numbers))
conn.close()