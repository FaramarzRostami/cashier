class Account:
    def __init__(self,id,account_number,owner,balance,active, accountlist=None):
        self.id=id
        self.account_number=account_number
        self.owner=owner
        self.balance=balance
        self.active=active

        if not accountlist:
            self.account_list = []
        else:
            self.account_list = accountlist

    def get_account_with_id(self, account_id):
        for account in self.account_list:
            if account.id == account_id:
                return account

