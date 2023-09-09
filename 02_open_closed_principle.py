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

class PaymentProcess(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcess):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"verifying security code: {security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcess):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"verifying security code: {security_code}")
        order.status = "paid"

class UPIPaymentProcessor(PaymentProcess):
    def pay(self, order, security_code):
        print("Processing UPI payment type")
        print(f"verifying security code: {security_code}")
        order.status = "paid"


        
order = Order()
order.add_item("keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print("Your total price:", order.total_price())
processor = UPIPaymentProcessor()
processor.pay(order, "948375")

