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
    
    # function to do payment for the order    
    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unkown payment type {payment_type}")
        
order = Order()
order.add_item("keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
order.pay("debit", "2343232")