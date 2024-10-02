import sqlite3

class User:
    def __init__(self,id,username,password,active,role, userlist=None):
        self.id=id
        self.username=username
        self.password=password
        self.active=active
        self.role=role

        if not userlist:
            self.user_list = []
        else:
            self.user_list = userlist


    def get_information(self):
        return f"{self.id}-{self.username}"

    def delete(self,id):
        pass

    def get_user_with_id(self, user_id):
        for user in self.user_list:
            if user.id == user_id:
                return user
