import sqlite3
from Entities.account import Account

def get_account_list():
    account_list = []
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        SELECT id,
           account_number,
           owner,
           balance,
           active
        FROM account""")

        data = cursor.fetchall()
        for account_item in data:
            account = Account(*account_item)
            account_list.append(account)
    return account_list

def get_account_with_id(id):
    account_list = []
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        SELECT id,
           account_number,
           owner,
           balance,
           active
        FROM account
        WHERE id={id}""")

        data = cursor.fetchall()
        for account_item in data:
            account = Account(*account_item)
            account_list.append(account)
    return account_list

def create_account(account_number, owner, balance, active):
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        INSERT INTO account (
            account_number,
            owner,
            balance,
            active
                )
         VALUES (
             '{account_number}',
             '{owner}',
             {balance},
             {active}
         )""")
        connection.commit()

def update_account(new_id, new_account_number, new_owner, new_balance, new_active):
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        UPDATE account
           SET account_number = '{new_account_number}',
               owner = '{new_owner}',
               balance = {new_balance},
               active = {new_active}
         WHERE id =  {new_id};""")
        connection.commit()

def update_active_account(id, new_active):
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        UPDATE account
           SET active = {new_active}
         WHERE id =  {id};""")
        connection.commit()

def delete_account_with_id(account_id):
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        DELETE FROM account
        WHERE id =  {account_id} and balance<=0""")
        connection.commit()

def get_money(id, money):
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        UPDATE account
            SET balance = balance+{money}
        WHERE id = {id}""")

        connection.commit()

def give_money(id, money):
    with sqlite3.connect("cash.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        UPDATE account
           SET balance = balance - {money}
         WHERE id =  {id} and balance >= {money};""")
        connection.commit()
