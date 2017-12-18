class Wallet():
    def __init__(self, money=0):
        self.deposit = money

    def put(self, money):
        try:
            if money >= 0:
                self.deposit += money
            else:
                print('Не верно указана сумма')
        except:
            print("Операция не выполнена")

    def get(self, money):
        try:
            if money >= 0:
                if self.deposit < money:
                    print('Превышен лимит')
                else:
                    self.deposit -= money
                    print(money)
                    return money
        except:
            print('Операция не выполнена')

    def summ(self):
        print(self.deposit)


if __name__ == '__main__':
    print('Первый экземпляр')
    wallet_1 = Wallet(50)  # создаём экземпляр класса Wallet
    wallet_1.put(60)  # вносим сумму на счёт
    wallet_1.summ()  # выводим текущую сумму на счёте
    wallet_1.get(40)  # пытаемя получить указанную сумму со счёта
    wallet_1.summ()  # выводим текущую сумму после снятия со счёта
    print('Второй экземпляр')
    wallet_1 = Wallet()
    wallet_1.put(40)
    wallet_1.summ()
    wallet_1.get(100)  # пытаемя получить указанную сумму со счёта
    wallet_1.summ()
    print('Третий экземпляр')
    wallet_1 = Wallet(5)
    wallet_1.put(-20)  # пытаемся внести не корректную сумму
    wallet_1.summ()
    wallet_1.get('a')  # пытаемся получить не корректное значение
    wallet_1.summ()
