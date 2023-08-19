"""
    SQL
    create table customer(
    cid int primary key auto_increment,
    name text,
    phone text,
    email text
    );

 create database dsharma;
 show database
 use dsharma

 create table customer(
    cid int primary key auto_increment,
    name text,
    phone text,
    email text
    );

    describe customer;

    insert into customer values(null, 'John', '+91 98724012819', 'john@example.com');
    select * from customer;



"""
import mysql.connector as db
class Customer:

    def __init__(self):
        self.name =input("Enter customer name:")
        self.phone=input("Enter customer phone:")
        self.email =input("Enter customer email:")


def main():
    customer = Customer()
    print(vars(customer))

# database connectivity
    #step 1: create connnection with database
    connection = db.connect(user='root',
                            password='',
                            host='127.0.0.1',
                            database='dsharma')
    #step2: obtain cursor to perform SQL operations;
    cursor = connection.cursor()
    #step3: create sql command
    sql = "insert into customer values(null, '{name}', '{phone}', '{email}');".format_map(vars(customer))
    #step4: execute sql command
    cursor.execute(sql)
    connection.commit()

    print("customer inserted...")


if __name__ == "__main__":
    main()
