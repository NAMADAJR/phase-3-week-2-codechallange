# Phase 3 weeek 1 Code Challenge

### By Namada Junior

## Project description-Coffee Shop Domain Model

This project models a simple coffee shop with three main classes: `Customer`, `Coffee`, and `Order`. The relationships between these classes are defined to simulate real-world operations in a coffee shop. 

## Properties of the project

## Class Structure and Methods

### **Customer Class**

```py
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
```

#### Properties:
- **`name`**: 
  - Stores the name of the customer.
  - Validates that the name is a string between 1 and 15 characters.
  - Can be updated after the customer is created.

#### Methods:
- **`orders()`**: 
  - Returns a list of all the orders associated with the customer.
- **`coffees()`**: 
  - Returns a unique list of all the different coffees the customer has ordered.
- **`create_order(coffee, price)`**: 
  - Creates and returns a new order associated with the customer and the given coffee object.



### **Coffee Class**

```py
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

```

#### Properties:
- **`name`**: 
  - Stores the name of the coffee.
  - Validates that the name is at least 3 characters long.
  - Cannot be changed after initialization.

#### Methods:
- **`orders()`**: 
  - Returns a list of all the orders for that specific coffee.
- **`customers()`**: 
  - Returns a unique list of all customers who have ordered that coffee.
- **`num_orders()`**: 
  - Returns the total number of times the coffee has been ordered.
- **`average_price()`**: 
  - Returns the average price of the coffee based on its associated orders.
  - If the coffee has no orders, returns 0.

### **Order Class**

```py
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
```

#### Properties:
- **`customer`**: 
  - Associates the order with a `Customer` instance.
- **`coffee`**: 
  - Associates the order with a `Coffee` instance.
- **`price`**: 
  - Stores the price of the order.
  - Validates that the price is a float between 1.0 and 10.0.

## Relationships
- A **`Customer`** has many **`Orders`**.
- A **`Coffee`** has many **`Orders`**.
- An **`Order`** belongs to one **`Customer`** and one **`Coffee`**.
- The relationship between **`Customer`** and **`Coffee`** is many-to-many through **`Orders`**.

## Usage
The system allows customers to place orders for coffee, and tracks the relationships between them. You can create customers, coffees, and orders, and retrieve data about customer orders, the coffees they've ordered, and coffee statistics like the number of orders and average price.


## Development

Want to contribute? Excellent!

To enhance or contribute on the existing project, follow these steps:

- Fork the repo
- Create a new branch (git checkout -b enhance-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -m 'enhanced feature')
- Push to the branch (git push origin enhance-feature)
- Create a Pull Request

## License

MIT License

Copyright (c) [2024] [Namada Junior]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.




