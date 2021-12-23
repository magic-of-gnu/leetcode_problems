class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.n = len(balance)

    def check_account_exists1(self, account1):
        if 0 < account1 <= self.n:
            return True

        return False

    def check_account_exists0(self, a0):
        if 0 <= a0 < self.n:
            return True

        return False
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:

        if money < 0:
            return False

        a0 = account1-1
        a1 = account2-1

        if not(self.check_account_exists0(a0) and self.check_account_exists0(a1)):
            return False

        if self.balance[a0] < money:
            return False

        self.balance[a1] += money
        self.balance[a0] -= money


    def deposit(self, account: int, money: int) -> bool:
        if not self.check_account_exists1(account):
            return False

        if money < 0:
            return False
            
        a0 = account-1
        self.balance[a0] += money
        

    def withdraw(self, account: int, money: int) -> bool:

        if not self.check_account_exists1(account):
            return False

        if money < 0:
            return False
            
        a0 = account-1

        if self.balance[a0] < money:
            return False

        self.balance[a0] -= money

        return True
        


if __name__ == "__main__":

    balance = [10, 100, 20, 50, 30]
    balance = [10,100,20,50,30]
    ans = [3,10],[5,1,20],[5,20],[3,4,15],[10,50]

    commands = ["Bank","deposit","deposit","transfer","transfer","transfer","deposit","transfer","withdraw","deposit","withdraw","transfer","transfer"]
    q = [[[767,653,252,849,480,187,761,243,408,385,334,732,289,886,149,320,827,111,315,155,695,110,473,585,83,936,188,818,33,984,66,549,954,761,662,212,208,215,251,792,956,261,863,374,411,639,599,418,909,208,984,602,741,302,911,616,537,422,61,746,206,396,446,661,48,156,725,662,422,624,704,143,94,702,126,76,539,83,270,717,736,393,607,895,661]],[68,668],[25,978],[8,31,924],[2,6,857],[20,43,59],[71,307],[11,46,577],[37,377],[72,835],[82,574],[67,9,939],[24,49,251]]

    print(q[0][0])
    print(len(q[0][0]))


    sol = Bank(balance)
    print(sol.withdraw(*ans[0]))

