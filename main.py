import mysql.connector

while True:
    def insert():
        name = input("Enter name : ")
        job = input("Enter job : ")
        salary = int(input("Enter salary : "))
        cursor.execute(f"insert into employees (name,job,salary) values ('{name}', '{job}', {salary})")
        connection.commit()

    def select():
        id = int(input('Enter ID you want to select: '))
        read = f'SELECT * FROM employees WHERE `id`={id}'
        cursor.execute(read)
        d = cursor.fetchone()
        print(d)
    def update():
        id = int(input('Enter ID you want to update: '))
        name = input("Enter name : ")
        job = input("Enter job : ")
        salary = int(input("Enter salary : "))
        read = f"UPDATE employees SET name='{name}', job='{job}', salary={salary}"+ f' WHERE `id`={id}'
        cursor.execute(read)
        connection.commit()

    def delete():
        id = int(input('Enter ID you want to delete: '))
        read = f'DELETE FROM employees WHERE `id`={id}'
        cursor.execute(read)
        connection.commit()

    connection = mysql.connector.connect(user="root", password="admin", host="localhost", database="database")
    cursor = connection.cursor()
    print("Hello, this is DBMS system. What do you want to do?\n")
    choice = int(input("1.Insert\n2.Select\n3.Update\n4.Delete\n5.Exit\n"))
    match choice:
        case 1:
            insert()
        case 2:
            select()
        case 3:
            update()
        case 4:
            delete()
        case 5:
            break
        case _:
            break
    cursor.close()
    connection.close()

    """def read():
    query = f"SELECT * FROM bank"
    cursor.execute(query)
    response = cursor.fetchall()

    for row in response:
        print(row)
def create():
    card = int(input("Enter card number: "))
    name = input("Enter your new name: ")
    balance = int(input("Enter your balance: "))
    query = f"insert into bank (card,name,balance) values('{card}','{name}', {balance})"
    cursor.execute(query)
    connection.commit()
def delete():
    id = int(input("Enter id from 1 to 9 to delete: "))
    query = f'delete from bank where "id"={id}'
    cursor.execute(query)
    connection.commit()
def  update():
    id = int(input("Enter id from 1 to 9 to update: "))
    card = int(input("Enter your new card number: "))
    name = input("Enter your new name: ")
    balance = int(input("Enter your new balance: "))
    query = f"update bank set card='{card}', name='{name}', balance={balance} where " + f'"id"={id}'
    cursor.execute(query)
    connection.commit()
    """