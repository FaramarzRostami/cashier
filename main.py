from tkinter import Tk, Label, Entry, Button, messagebox, Checkbutton, IntVar
from tkinter.ttk import Combobox
from typing import dataclass_transform
from xmlrpc.client import boolean

from Data.user_data import is_user, get_user, get_active_status, get_user_list, get_user_with_id, \
    get_user_with_username, create_user, update_user

from Data.account_data import get_account_list, delete_account_with_id, update_account, get_money, give_money, \
    get_account_with_id, create_account

log_form = Tk()
log_form.title("Login")

label_user = Label(log_form, text="User Name ")
label_user.grid(row=0, column=0)
entry_user = Entry(log_form, width=30)
entry_user.grid(row=0, column=1)

label_pass = Label(log_form, text="Password ")
label_pass.grid(row=1, column=0)
entry_pass = Entry(log_form, width=10)
entry_pass.grid(row=1, column=1, sticky="w")


def show_account_form(account_data=None):
    account_form = Tk()
    account_form.title("New Account Form" if not account_data else "Update Account Form")

    account_number_label = Label(account_form, text="Account Number")
    account_number_label.grid(row=0, column=0, sticky="e")
    account_number_entry = Entry(account_form, width=15)
    account_number_entry.grid(row=0, column=1, padx=(0, 10), sticky="w")

    balance_label = Label(account_form, text="Balance")
    balance_label.grid(row=1, column=0, sticky="e")
    balance_entry = Entry(account_form, width=20)
    balance_entry.grid(row=1, column=1, rowspan=1, columnspan=2, sticky="w")

    owner_label = Label(account_form, text="Owner")
    owner_label.grid(row=2, column=0, sticky="e")
    owner_entry = Entry(account_form, width=30)
    owner_entry.grid(row=2, column=1, padx=(0, 10), rowspan=1, columnspan=2, sticky="e")

    var = IntVar(account_form)
    checkbutton = Checkbutton(account_form, text="Active Account", variable=var)
    checkbutton.grid(row=3, column=1, sticky="w")

    if account_data:
        account_number_entry.insert(0, account_data.account_number)
        balance_entry.insert(0, account_data.balance)
        owner_entry.insert(0, account_data.owner)
        var.set(account_data.active)
        account_number_entry.config(state="readonly")

    else:
        account_number_entry.config(state="normal")

    def submit():
        choice = var.get()
        account_number = account_number_entry.get()
        owner = owner_entry.get()
        active_check = choice
        balance = balance_entry.get()

        if not account_data:
            create_account(account_number, owner, balance, active_check)
        else:
            old_id = account_data.id
            old_account_number = account_number_entry.get()
            update_account(old_id, old_account_number, owner, balance, active_check)

        create_table_body()
        account_form.destroy()

    submit_button = Button(account_form, text="SUBMIT", command=submit)
    submit_button.grid(row=3, column=2, pady=(0, 10), sticky="w")

    account_form.mainloop()


def user_form():
    user_win = Tk()
    user_win.title("Users")

    note_label = Label(user_win, text="After Search : If exist Username Then Update else Create")
    note_label.grid(row=0, column=0,columnspan=3, sticky="w")
    user_label = Label(user_win, text="User Name")
    user_label.grid(row=1, column=0, sticky="w")

    user_entry = Entry(user_win, width=50)
    user_entry.grid(row=1, column=1, pady=(10, 10), sticky="w")

    pass_label = Label(user_win, text="Password")
    pass_label.grid(row=2, column=0, sticky="w")
    pass_entry = Entry(user_win, width=30)
    pass_entry.grid(row=2, column=1, columnspan=2, sticky="w")
    var_active = IntVar(user_win)
    checkbutton = Checkbutton(user_win, text="Active User", variable=var_active)
    checkbutton.grid(row=3, column=1, sticky="w")
    var_role = IntVar(user_win)
    checkbutton = Checkbutton(user_win, text="Manager", variable=var_role)
    checkbutton.grid(row=4, column=1, sticky="w")

    def search_user():
        data = get_user_with_username(user_entry.get())
        pass_entry.delete(0, 20)
        if data:
            button_user.config(text="Update")
            pass_entry.insert(0, data[0].password)
            var_active.set(data[0].active)
            var_role.set(data[0].role)
        else:
            button_user.config(text="Create")
            var_active.set(0)
            var_role.set(0)

    button_submit_user = Button(user_win, text="Search User", command=search_user)
    button_submit_user.grid(row=1, column=2, pady=(10, 10), sticky="e")

    def submit():
        data = get_user_with_username(user_entry.get())
        username = user_entry.get()
        password = pass_entry.get()
        active_check = var_active.get()
        role_check = var_role.get()
        choice_active = active_check
        choice_role = role_check
        if not data:
            create_user(username, password, choice_active, choice_role)
        else:
            old_id = data[0].id
            update_user(old_id, password, active_check, role_check)
        user_win.destroy()

    button_user = Button(user_win, text="SUBMIT", command=submit)
    button_user.grid(row=4, column=2, pady=(0, 10), padx=(0, 10), sticky="e")

    user_win.mainloop()

def get_give_form(idid, name, status):
    get_give_win = Tk()
    get_give_win.title("Get Money" if status == 1 else "Give Money")
    owner_label = Label(get_give_win, text=name)
    owner_label.grid(row=0, column=1, sticky="w")
    get_label = Label(get_give_win, text="Get Money" if status == 1 else "Give Money")
    get_label.grid(row=1, column=0, sticky="e")
    get_entry = Entry(get_give_win, width=20)
    get_entry.grid(row=1, column=1, padx=(0, 10), sticky="w")

    def submit():
        money = get_entry.get()
        if status == 1:
            get_money(idid, money)
        else:
            give_money(idid, money)
        get_give_win.destroy()
        create_table_body()

    button_get = Button(get_give_win, text="SUBMIT", command=submit)
    button_get.grid(row=1, column=2, pady=(0, 10), padx=(0, 10), sticky="e")

    get_give_win.mainloop()


def delete_account(id, balance):
    if balance > 0:
        messagebox.showinfo("Error", "Balance Greater than ZERO")
    else:
        delete_account_with_id(id)
        create_table_body()


def create_table_header(data_list, username, window=None):
    user_pass_label = Label(window, text="Username : " + username + " ----- Role : " + (
        "Manager" if data_list[0].role == 1 else "User Normal"))
    user_pass_label.grid(row=0, column=0, columnspan=7, sticky="w")

    user_button = Button(window,
                         text="Users", command=user_form)
    user_button.grid(row=1, column=0, columnspan=7, sticky="e")

    add_button = Button(window,
                        text="Create Account", command=show_account_form)
    add_button.grid(row=1, column=1, columnspan=9, sticky="e")

    row_label = Label(window, text="NO")
    row_label.grid(row=2, column=0, sticky="w")

    account_number_label = Label(window, text="Account Number")
    account_number_label.grid(row=2, column=1, sticky="w")

    owner_label = Label(window, text="Owner")
    owner_label.grid(row=2, column=2, sticky="w")

    balance_label = Label(window, text="Balance")
    balance_label.grid(row=2, column=3, sticky="w")

    active_label = Label(window, text="Active")
    active_label.grid(row=2, column=4, sticky="w")

entry_list = []

def create_table_body(window=None):
    for entry in entry_list:
        entry.destroy()

    entry_list.clear()

    account_list = get_account_list()

    row_number = 2
    for account in account_list:
        row_entry = Entry(window, width=5)
        row_entry.insert(0, str(row_number))
        row_entry.config(state="readonly")
        row_entry.grid(row=row_number + 1, column=0)
        entry_list.append(row_entry)

        account_number_entry = Entry(window, width=15)
        account_number_entry.insert(0, account.account_number)
        account_number_entry.config(state="readonly")
        account_number_entry.grid(row=row_number + 1, column=1)
        entry_list.append(account_number_entry)

        owner_entry = Entry(window, width=40)
        owner_entry.insert(0, account.owner)
        owner_entry.config(state="readonly")
        owner_entry.grid(row=row_number + 1, column=2)
        entry_list.append(owner_entry)

        balance_entry = Entry(window, width=20)
        balance_entry.insert(0, account.balance)
        balance_entry.config(state="readonly")
        balance_entry.grid(row=row_number + 1, column=3)
        entry_list.append(balance_entry)

        active_entry = Entry(window, width=12)
        active_entry.insert(0, 'Active' if account.active == 1 else 'Not Active')
        active_entry.config(state="readonly")
        active_entry.grid(row=row_number + 1, column=4, padx=(0, 10))
        entry_list.append(active_entry)

        get_button = Button(window, text="GET",
                            command=lambda c_id=account.id, current_owner=account.owner: get_give_form(c_id,
                                                                                                       current_owner,
                                                                                                       1))
        get_button.grid(row=row_number + 1, column=5, padx=(0, 10))
        entry_list.append(get_button)

        give_button = Button(window, text="GIVE",
                             command=lambda c_id=account.id, current_owner=account.owner: get_give_form(c_id,
                                                                                                        current_owner,
                                                                                                        0))
        give_button.grid(row=row_number + 1, column=6, padx=(0, 10))
        entry_list.append(give_button)

        update_button = Button(window, text="UPDATE",
                               command=lambda current_account=account: show_account_form(current_account))
        update_button.grid(row=row_number + 1, column=7, padx=(0, 10))
        entry_list.append(update_button)

        delete_button = Button(window, text="DELETE", command=lambda account_id=account.id,
                                                                     account_balance=account.balance: delete_account(
            account_id, account_balance))
        delete_button.grid(row=row_number + 1, column=8, padx=(0, 10))
        entry_list.append(delete_button)

        row_number += 1


def main_form(username, password):
    window = Tk()
    window.title("Cashier")

    data = get_user(username, password)

    create_table_header(data, username, window)
    create_table_body(window)
    window.mainloop()


def submit_login():
    user_name = entry_user.get()
    password = entry_pass.get()
    if not is_user(user_name, password):
        messagebox.showinfo("", "Username or Password is wrong")
    else:
        if get_active_status(user_name, password) == 0:
            messagebox.showinfo("", "User Not Active")
        else:
            log_form.destroy()
            main_form(user_name, password)


button_submit = Button(log_form, text="SUBMIT", command=submit_login)
button_submit.grid(row=1, column=1, sticky="e")

log_form.mainloop()
# show_log_form()
