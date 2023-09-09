from abc import abstractmethod, ABC

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    # function to add items
    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    # function to compute total price of the added items
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    


class Authorizer(ABC):
    @abstractmethod
    def is_authorised(self)->bool:
        pass

class SMSAuth(Authorizer):
    authorised =  False
    def verify_code(self, code):
        print(f"verfying code {code}")
        self.authorised = True

    def is_authorised(self)-> bool:
        return self.authorised

class NotARobot(Authorizer):
    authorised =  False
    
    def not_a_robot(self):
        print("Are you a robot")
        self.authorised =  True

    def is_authorised(self)-> bool:
        return self.authorised


class PaymentProcess(ABC):
    @abstractmethod
    def pay(self, order):
        pass



class DebitPaymentProcessor(PaymentProcess):
    def __init__(self, security_code, autorizer:SMSAuth):
        self.security_code = security_code
        self.autorizer = autorizer
      
    def pay(self, order):
        if not self.autorizer.is_authorised():
            raise Exception("Not Authorised")
        print("Processing debit payment type")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcess):
    def __init__(self, security_code):
        self.security_code = security_code     
 
    def pay(self, order):
        print("Processing debit payment type")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"

class UPIPaymentProcessor(PaymentProcess):
    def __init__(self, email_address, autorizer:SMSAuth):
        self.email_address = email_address
        self.autorizer = autorizer

    def pay(self, order):
        if not self.autorizer.is_authorised():
            raise Exception("Not Authorised")
        print("Processing UPI payment type")
        print(f"verifying email address: {self.email_address}")
        order.status = "paid"

        
order = Order()
order.add_item("keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print("Your total price:", order.total_price())
authorizer = NotARobot()
processor = UPIPaymentProcessor("hemantkr24@gmail.com", authorizer)
authorizer.not_a_robot()
processor.pay(order)

