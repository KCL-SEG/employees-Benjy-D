"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def get_contract_str(self):
        return self.name + ""

    def get_commission_str(self):
        return ""

    def get_total_pay_str(self):
        return ". Their total pay is " + str(self.get_pay()) + "."

    def __str__(self):
        return self.get_contract_str() + self.get_commission_str() + self.get_total_pay_str()

class SalaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def get_contract_str(self):
        return super().get_contract_str() + " works on a monthly salary of " + str(self.salary)
    
    def __str__(self):
        return super().__str__()
    
class HourlyEmployee(Employee):
    def __init__(self, name, hourlyPay, hours):
        super().__init__(name)
        self.hourlyPay = hourlyPay
        self.hours = hours

    def get_pay(self):
        return self.hourlyPay * self.hours
    
    def get_contract_str(self):
        return super().get_contract_str() + " works on a contract of " + str(self.hours) + " hours at " + str(self.hourlyPay) + "/hour"
    
    def __str__(self):
        return super().__str__()
    
class SalaryBonusCommissionEmployee(SalaryEmployee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus
    
    def get_commission_str(self):
        return super().get_commission_str() + " and receives a bonus commission of " + str(self.bonus)
    
    def __str__(self):
        return super().__str__()
    
class HourlyBonusCommissionEmployee(HourlyEmployee):
    def __init__(self, name, hourlyPay, hours, bonus):
        super().__init__(name, hourlyPay, hours)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus
    
    def get_commission_str(self):
        return super().get_commission_str() + " and receives a bonus commission of " + str(self.bonus)
    
    def __str__(self):
        return super().__str__()

class SalaryContractCommissionEmployee(SalaryEmployee):
    def __init__(self, name, salary, contractPay, numContracts):
        super().__init__(name, salary)
        self.contractPay = contractPay
        self.numContracts = numContracts

    def get_pay(self):
        return super().get_pay() + self.contractPay * self.numContracts
    
    def get_commission_str(self):
        return super().get_commission_str() + " and receives a commission for " + str(self.numContracts) + " contract(s) at " + str(self.contractPay) + "/contract"
    
    def __str__(self):
        return super().__str__()
    

class HourlyContractCommissionEmployee(HourlyEmployee):
    def __init__(self, name, hourlyPay, hours, contractPay, numContracts):
        super().__init__(name, hourlyPay, hours)
        self.contractPay = contractPay
        self.numContracts = numContracts

    def get_pay(self):
        return super().get_pay() + self.contractPay * self.numContracts
    
    def get_commission_str(self):
        return super().get_commission_str() + " and receives a commission for " + str(self.numContracts) + " contract(s) at " + str(self.contractPay) + "/contract"
    
    def __str__(self):
        return super().__str__()


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 25, 100)

print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryContractCommissionEmployee('Renee', 3000, 200, 4)

print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContractCommissionEmployee('Jan', 25, 150, 220, 3)

print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryBonusCommissionEmployee('Robbie', 2000, 1500)

print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyBonusCommissionEmployee('Ariel', 30, 120, 600)

print(str(ariel))