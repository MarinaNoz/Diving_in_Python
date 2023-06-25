#Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

class Bank:
    _BALANCE = 0
    _MIN = 50
    _COMMISSION = 0.015
    _BONUS = 0.03
    _TAX = 0.10
    _OPERATION: int

    def __init__(self):
        self._OPERATION = 0

    def _in(self, cash: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0:
            self._BALANCE += cash
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None
    
    def _out(self, cash: int, commission: int)-> tuple[int, int] |None:
        if cash % self._MIN == 0 and self._BALANCE > 0 and self._BALANCE -(cash + commission) >= 0:
            self._BALANCE -= cash
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None
    
    def _chek_commission(self, cash: int) -> int:
        sum_commission = cash * self._COMMISSION

        _MAX = 600
        _MIN = 30
        if sum_commission > _MAX:
            return _MAX
        elif sum_commission < _MIN:
            return _MIN
        else:
            return int (sum_commission)
        
    def _check_operation(self):
        return (False, True)[self._OPERATION % 3 == 0]


 

    
    def _exit(self):
        return "Всего доброго, приходите к нам еще"
    
    def start(self, mode: str, cash: int = 0) -> str:
        check_operation = self._check_operation()
        if check_operation:
            self._BALANCE += self._BALANCE * self._BONUS


        match mode:
            case "in":
                data = self._in(cash=cash)

                com_data = self._chek_commission(cash=cash)
                return f"Средства были зачислены сумма: {cash}, баланс: {self._BALANCE}"


            case "out":
                com_data = self._chek_commission(cash=cash)

                data = self._out(cash=cash, commission=com_data)
                if data:
                    return f"Операция осуществлена успешно, сумма: {cash}, комиссия: {com_data}, баланс: {self._BALANCE}"
                else:
                    return "Не хватает средств"

              
            
            case "exit":
                return self._exit()
            

client = Bank()
print(client.start(mode="in", cash=100))

