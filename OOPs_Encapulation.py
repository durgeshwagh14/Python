class Car:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.__price = price 

    def car_info(self):
        print(f"{self.name} is the best car and its model {self.model}")

    def get_price(self):
        return self.__price

class Customer(Car):
    def __init__(self, name, model, price):
        super().__init__(name, model, price)

    def buy(self):
        print(f"I am buying the {self.name} car")
        print(f"The price is: {self.get_price()}")


c1 = Car("TUV", "2015", 100000)
cust1 = Customer("BMW", "2008", 150000)

print(c1.model)
# print(cust1.__price)

print(cust1.get_price())
cust1.buy()
