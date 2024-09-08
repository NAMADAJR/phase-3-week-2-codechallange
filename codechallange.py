class Customer:
    def __init__(self, name):
        self.name = name
        self._validate_name()
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._validate_name()

    def _validate_name(self):
        if not isinstance(self._name, str) or not (1 <= len(self._name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order



class Coffee:
    def __init__(self, name):
        self._name = name
        self._validate_name()
        self._orders = []

    @property
    def name(self):
        return self._name

    def _validate_name(self):
        if not isinstance(self._name, str) or len(self._name) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)



class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price  # Set the price before validation
        self._validate_price()

        # Add this order to customer and coffee's list of orders
        customer.orders().append(self)
        coffee.orders().append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def _validate_price(self):
        if not isinstance(self.price, (int, float)) or not (1.0 <= self.price <= 10.0):
            raise ValueError("Price must be a number between 1.0 and 10.0.")

# Create some customers
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Create some coffee
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Create orders
order1 = customer1.create_order(coffee1, 5.0)
order2 = customer2.create_order(coffee1, 6.5)
order3 = customer1.create_order(coffee2, 4.0)

# Access order data
print(customer1.coffees())  # List of unique coffees Alice ordered
print(coffee1.customers())  # List of customers who ordered the Latte
print(coffee1.num_orders())  # Number of orders for Latte
print(coffee1.average_price())  # Average price of orders for Latte
