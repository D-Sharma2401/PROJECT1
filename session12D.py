#   WHATSAPP CONTACT LIST :)
contacts = [
    {
        "name": "john",
        "phone": "9872428192",
        "conversations": [
                        "hi",
                        "hello",
                        "i am good"
                         ]
    },

    {
        "name": "fionna",
        "phone": "9872428192",
        "conversations": [
                        "hola",
                        "ho",
                        "what are you doing ??"
                            ]
    },
    {
        "name": "george",
        "phone": "9836328192",
        "conversations": [
                        "xyz",
                        "hows your day going?",
                        "i am good."

                            ]
    }
]

search_keyword = input("Enter Keyword to Search..")
# print("search keyword", search_keyword)
for contact in contacts:
    if contact["name"].lower().find(search_keyword.lower()) >= 0 \
                or contact["phone"].find(search_keyword) >=0:

 print(contact)
 print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")


        # if contact["name"].lower().find(search_keyword.lower())>=0\
        #     or contact["phone"].find(search_keyword) >= 0:
        #
        #  print(contacts)
        # print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

    # if contact["name"].lower().startswith(search_keyword.lower()):
    # if contact["name"].lower().__contain__(search_keyword.lower()):
    # if contact["name"].lower().find(search_keyword.lower())>=0\
    #     or contact["phone"].find(search_keyword) >=0:
    #
    #  print(contact)
    #  print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

#ASSIGNMENT = Implementation search on conversation as well

    # if contact["name"].lower().find(search_keyword.lower()) >= 0 \
    #         or contact["phone"].find(search_keyword) >= 0 \
            # or contact["conversations"].startswith(search_keyword) >= 0:


