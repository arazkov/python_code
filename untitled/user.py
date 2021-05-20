class User():
    """docstring forUser."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def discrip_user(self):
        return (self.first_name + ' ' + self.last_name)

    def greet_user(self):
        print('Hello', self.discrip_user())

    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self):
        self.privileges = [
        'разрешено добавлять сообщения',
        'разрешено удалять пользователей',
        'разрешено банить пользователей'
        ]

    def show_privileges(self):
        print(self.privileges)

class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


user_1 = User('Adam', 'Moran')
user_2 = User('Nick', 'Friman')
user_3 = User('Igor', 'Semkin')
user_admin = Admin('Bob', 'Forman')

user_admin.privileges.show_privileges()
print(user_admin.last_name)


# user_1.login_attempts = 3
#
# while user_1.login_attempts < 5:
#     user_1.increment_login_attempts()
#     print(user_1.login_attempts)
#
# user_1.reset_login_attempts()
# print(user_1.login_attempts)
