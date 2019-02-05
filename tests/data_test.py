red_flag_valid = {
    "title": "Title 1",
    "comment": "We are facing this challenge",
    "location": "Lat 1231 Long 1424",
    "images": ["picurl1","picurl1"],
    "videos": ["vidurl1","vidurl2"]
}
red_flag_wrong_media = {
    "title": "Title 2",
    "comment": "We are facing this challenge",
    "location": "Lat 1231 Long 1424",
    "videos": ["vidurl"],
    "images": 12353
}
user_invalid_phone = {
    "firstname": "Mugerwa",
    "lastname": "Fred",
    "othernames": "",
    "email": "reifred33@gmail.com",
    "phoneNumber": "dfdfdfd",
    "username": "username33",
    "password": "Password33",
    "isAdmin": False
}
user_short_pass = {
    "firstname": "Mugerwa",
    "lastname": "Fred",
    "othernames": "",
    "email": "fred@gmail.com",
    "phoneNumber": "0757605424",
    "username": "username",
    "password": "pass",
    "isAdmin": False
}
valid_admin = {
    "firstname": "Kiggundu",
    "lastname": "Gerald",
    "othernames": "",
    "email": "admin@gmail.com",
    "phoneNumber": "0753736433",
    "username": "admin",
    "password": "Admin123",
    "isAdmin": True
}
sign_in_admin = {
    "username": "admin",
    "password": "Admin123",
}
valid_user = {
    "firstname": "Mugerwa",
    "lastname": "Fred",
    "othernames": "",
    "email": "rei33@gmail.com",
    "phoneNumber": "0757605424",
    "username": "username",
    "password": "Password123",
    "isAdmin": False
}
valid_user2 = {
    "firstname": "Mugerwa",
    "lastname": "Fred",
    "othernames": "",
    "email": "reifred33@gmail.com",
    "phoneNumber": "0757605424",
    "username": "username33",
    "password": "Password33",
    "isAdmin": False
}
user_invalid_email = {
    "firstname": "Mugerwa",
    "lastname": "Fred",
    "othernames": "",
    "email": "email",
    "phoneNumber": "0757605424",
    "username": "username2",
    "password": "password",
    "isAdmin": False
}
user_name_not_string = {
    "firstname": "Mugerwa",
    "lastname": 11111,
    "othernames": "",
    "email": "mugerwafred@gmail.com",
    "phoneNumber": "0757605424",
    "username": "username2",
    "password": "password",
    "isAdmin": False
}
sign_wrong_password = {
    "username": "username",
    "password": "Passwor12d",
    "isAdmin": False
}
sign_wrong_username = {
    "username": "usern",
    "password": "Password12",
    "isAdmin": False
}
valid_sign_in = {
    "username": "username",
    "password": "Password123",
    "isAdmin": False
}
valid_sign_in2 = {
    "username": "username33",
    "password": "Password33"
}
valid_comment = {
    "comment": "New comment"
}
short_comment = {
    "comment": "Today"
}
valid_location = {
    "location": "Kampala"
}
valid_status = {
    "status": "resolved"
}
invalid_status = {
    "status": "draf"
}
status_wrong_data = {
    "status": 34343
}
