class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        validateAccountNumber - between 1 to n
        """
        self.balance = balance

    def getAccountIndex(self, accountNo):
        index = accountNo - 1 
        return index
    
    def isValidateAccountNo(self, accountNo):
        n = len(self.balance)
        index = self.getAccountIndex(accountNo)
        return True if index >= 0 and index < n else False          

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if self.isValidateAccountNo(account1) and self.isValidateAccountNo(account2):
            account1Index = self.getAccountIndex(account1)
            account2Index = self.getAccountIndex(account2)
            if self.balance[account1Index] >= money:
                self.balance[account1Index] -= money
                self.balance[account2Index] += money
                return True

        return False

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if self.isValidateAccountNo(account):
            accountIndex = self.getAccountIndex(account)
            self.balance[accountIndex] += money
            return True
        
        return False
        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if self.isValidateAccountNo(account):
            accountIndex = self.getAccountIndex(account)
            if self.balance[accountIndex] >= money:
                self.balance[accountIndex] -= money
                return True
        
        return False        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)