from session15 import Pet
from session14A import Customer
from session14B import DBHelper
from tabulate import tabulate
from session17 import Consultation
def consultation_menu():

    db = DBHelper()

    message = """
       >>Consultation Menu<<
       1: Add Consultation
       2: Update Consultation
       3: View All Consultations
       4: View Consultations by Date
       5: View Customers Pets Consultation
       0: Quit
       """
    print(message)
    choice = int(input("Enter Your Choice: "))

    pet = Pet()
    customer = Customer()
    consultation = Consultation()


    while True:
        if choice == 1:

            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pets_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'PROBLEM', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            if len(rows) == 0:
                print("Please add pet First....")
                break
            if len(rows) == 1:
                pet.pid = rows[0][0]
            else:
                pet.pid = int(input("Enter Pet Id: "))

            consultation.cid = customer.cid
            consultation.pid = pet.pid
            consultation.read_consulation_data()

            print(vars(pet))

            sql = consultation.get_insert_sql_query()
            db.execute_sql(sql)
            print("Consultation Added Successfully...")
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 0:
            break
        else:
            print("Invalid Choice")

        print(message)
        choice = int(input("Enter Your Choice: "))