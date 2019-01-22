from app.helpers.database import Database

db = Database()

class User:

    def __init__(self, **kwargs):
        self.firstname = kwargs.get("firstname")
        self.lastname = kwargs.get("lastname")
        self.othernames = kwargs.get("othernames")
        self.email = kwargs.get("email")
        self.phoneNumber = kwargs.get("phoneNumber")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.registered = kwargs.get("registered")
        self.isAdmin = kwargs.get("isAdmin")

    @staticmethod
    def register_user(**user_details):
        return db.add_user(**user_details)

    @staticmethod
    def get_users():
        return db.get_all_users()

    @staticmethod
    def user_exists(username, email=None):
        if not email:
            return db.username_exists(username)
        return db.username_or_email_exists(username, email)

    def convert_to_dict(self):
        return dict(firstname=self.firstname,
                    lastname=self.lastname, othernames=self.othernames,
                    email=self.email, phoneNumber=self.phoneNumber,
                    username=self.username, registered=self.registered,
                    password=self.password, isAdmin=self.isAdmin)