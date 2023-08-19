from session18A import Customer
from MongoDBHelper import MongoDBHelper
from bson.objectid import ObjectId

def main():
    db = MongoDBHelper()

    # customer = Customer()
    # customer.read_customer_data()
    #
    # document = vars(customer)
    #
    # db.insert(document)
    # query = {'phone': '817498'}
    query = {'_id': ObjectId('64c36fac07a859642834c0e9')}
    # db.delete(query)
    db.fetch(query=query)

    document_data_to_update = {'name': 'George W', 'phone': '+91 8723642764', 'age': '33'}
    db.update(document_data_to_update, query)



if __name__ == "__main__":
    main()