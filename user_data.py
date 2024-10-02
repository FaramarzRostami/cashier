import sqlite3
from Entities.user import User


def get_user_list():
    user_list = []
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
        Select  id
        ,       username
        ,       password
        ,       active
        ,       role
        From    Users""")

        data = cursor.fetchall()

        for user_item in data:
            user = User(*user_item)
            user_list.append(user)

    return user_list


def create_user(username, password, active, role):
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        INSERT INTO users (
              username,
              password,
              active,
              role
                  )
        VALUES (
             '{username}',
             '{password}',
             {active},
             {role}
         )""")
        connection.commit()


def update_user(new_id,new_password, new_active, new_role):
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        UPDATE users
           SET password='{new_password}',
               active = {new_active},
               role = {new_role}
         WHERE id =  {new_id}""")
        connection.commit()


def is_user(username, password):
    # user_list=[]
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            Select  id
            ,       username
            ,       password
            ,       active
            ,       role
            From    users
            where username='{username}' and password='{password}'""")

    data = cursor.fetchall()
    if data:
        # if data
        return True
    else:
        return False


def get_active_status(username, password):
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            Select  id
            ,       username
            ,       password
            ,       active
            ,       role
            From    users
            where username='{username}' and password='{password}' and active=1""")

    data = cursor.fetchall()
    if data:
        return 1
    else:
        return 0


def get_user(username, password):
    user_list = []
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            Select  id
            ,       username
            ,       password
            ,       active
            ,       role
            From    users
            where username='{username}' and password='{password}'""")

        data = cursor.fetchall()
        for user_item in data:
            user = User(*user_item)
            user_list.append(user)

    return user_list


def get_user_with_username(username):
    user_list = []
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            Select  id
            ,       username
            ,       password
            ,       active
            ,       role
            From    users
            where username='{username}'""")

        data = cursor.fetchall()
        for user_item in data:
            user = User(*user_item)
            user_list.append(user)

    return user_list


def get_user_with_id(id):
    user_list = []
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            Select  id
            ,       username
            ,       password
            ,       active
            ,       role
            From    users
            where id={id}'""")

        data = cursor.fetchall()
        for user_item in data:
            user = User(*user_item)
            user_list.append(user)

    return user_list

# def update_active_user(id, new_active):
#     with sqlite3.connect("cash.db") as connection:
#         cursor = connection.cursor()
#         cursor.execute(f"""
#         UPDATE users
#            SET active = {new_active}'
#          WHERE id =  {id}""")
#         connection.commit()
