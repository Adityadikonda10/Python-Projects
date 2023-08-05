IDENTITY = {
    "SID000001": {
        "name": "Aditya Ravindra Dikonda",
        "branch": "Electronics & Telecommunications Engineering",
        "year": "2022-2026",
        "birth_date": "10-February-2005",
        "gender": "male",
        "phone_number": "9167965566",
        "address": "709/1B, Koyna CHS, Mankhurd, Mumbai 400043.",
        "e-mail": "adityadikonda10@gmail.com",
        "GST-Email": "adityardextc122@gst.sies.edu.in",

    },
    "SID000002": {
        "name": "Riya Praveenkumar Alle",
        "branch": "Electronics & Telecommunications Engineering",
        "year": "2022-2026",
        "birth_date": "10-August-2004",
        "gender": "female",
        "phone_number": "",
        "address": "709/1B, Koyna CHS, Mankhurd, Mumbai 400043.",
        "e-mail": "@gmail.com",
        "GST-Email": "extc122@gst.sies.edu.in",

    },
    "SID000003": {
        "name": "",
        "branch": "Electronics & Telecommunications Engineering",
        "year": "2022-2026",
        "birth_date": "",
        "gender": "male",
        "phone_number": "",
        "address": "",
        "e-mail": "@gmail.com",
        "GST-Email": "extc122@gst.sies.edu.in",

    },
    "SID000004": {
        "name": "",
        "branch": "Electronics & Telecommunications Engineering",
        "year": "2022-2026",
        "birth_date": "",
        "gender": "male",
        "phone_number": "",
        "address": "",
        "e-mail": "@gmail.com",
        "GST-Email": "extc122@gst.sies.edu.in",

    },
    "SID000005": {
        "name": "",
        "branch": "Electronics & Telecommunications Engineering",
        "year": "2022-2026",
        "birth_date": "",
        "gender": "male",
        "phone_number": "",
        "address": "",
        "e-mail": "@gmail.com",
        "GST-Email": "extc122@gst.sies.edu.in",

    },
}

# print(IDENTITY["SID000001"]['name'])
id_number = str(input("Enter the SID number you want to verify: "))
for id_n in IDENTITY[id_number]:
    info = IDENTITY[id_number][id_n]
    print(info)

#     name = IDENTITY[id_number]['name']
#     branch = IDENTITY[id_number]['branch']
#     year = IDENTITY[id_number]['year']
#     birth_date = IDENTITY[id_number]['birth_date']
#     gender = IDENTITY[id_number]['gender']
#     phone_number = IDENTITY[id_number]['phone_number']
#     address = IDENTITY[id_number]['address']
#     e_mail = IDENTITY[id_number]['e-mail']
#     GST_Email = IDENTITY[id_number]['GST-Email']
# print(IDENTITY[id_number]['name'])