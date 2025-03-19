import datetime

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date

class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.orders = []

    def add_product(self, product):
        self.inventory[product.product_id] = product
        print(f'Product {product.name} added to inventory.')

    def process_order(self, order):
        product = self.inventory.get(order.product.product_id)
        if product and product.quantity >= order.quantity:
            product.quantity -= order.quantity
            self.orders.append(order)
            print(f'Order {order.order_id} processed.')
        else:
            print(f'Order {order.order_id} cannot be processed due to insufficient inventory.')

    def generate_report(self):
        print('\nInventory Report:')
        for product in self.inventory.values():
            print(f'Product ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}')

        print('\nOrders Report:')
        for order in self.orders:
            print(f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Order Date: {order.order_date}')


# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Adding products to inventory
    p1 = Product(1, 'Apple', 25.50, 100)
    p2 = Product(2, 'Apple Sauce', 15.75, 200)
    scm.add_product(p1)
    scm.add_product(p2)

    # Processing an order
    o1 = Order(1, p1, 5, datetime.datetime.now())
    scm.process_order(o1)

    # Generating a report
    import datetime

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date

class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.orders = []
        self.suppliers = {}

    def add_product(self, product):
        self.inventory[product.product_id] = product
        print(f'Product {product.name} added to inventory.')

    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier
        print(f'Supplier {supplier.name} added.')

    def process_order(self, order):
        product = self.inventory.get(order.product.product_id)
        if product and product.quantity >= order.quantity:
            product.quantity -= order.quantity
            self.orders.append(order)
            print(f'Order {order.order_id} processed.')
        else:
            print(f'Order {order.order_id} cannot be processed due to insufficient inventory.')

    def generate_report(self):
        print('\nInventory Report:')
        for product in self.inventory.values():
            supplier_name = self.suppliers[product.supplier_id].name
            print(f'Product ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}, Supplier: {supplier_name}')

        print('\nOrders Report:')
        for order in self.orders:
            print(f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Order Date: {order.order_date}')

        print('\nSuppliers Report:')
        for supplier in self.suppliers.values():
            print(f'Supplier ID: {supplier.supplier_id}, Name: {supplier.name}, Contact Info: {supplier.contact_info}')

# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Adding suppliers
    s1 = Supplier(1, 'Acme Supplies', 'acme@supplies.com')
    s2 = Supplier(2, 'Widget Corp', 'contact@widgetcorp.com')
    scm.add_supplier(s1)
    scm.add_supplier(s2)

    # Adding products to inventory
    p1 = Product(1, 'Widget', 25.50, 100, s2.supplier_id)
    p2 = Product(2, 'Gadget', 15.75, 200, s1.supplier_id)
    scm.add_product(p1)
    scm.add_product(p2)

    # Processing an order
    o1 = Order(1, p1, 5, datetime.datetime.now())
    scm.process_order(o1)

    # Generating a report

    scm.generate_report()
    import datetime

    import datetime

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status

class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.orders = []
        self.suppliers = {}

    def add_product(self, product):
        self.inventory[product.product_id] = product
        print(f'Product {product.name} added to inventory.')

    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier
        print(f'Supplier {supplier.name} added.')

    def process_order(self, order):
        product = self.inventory.get(order.product.product_id)
        if product and product.quantity >= order.quantity:
            product.quantity -= order.quantity
            order.update_status("Processed")
            self.orders.append(order)
            print(f'Order {order.order_id} processed.')
        else:
            order.update_status("Failed")
            print(f'Order {order.order_id} cannot be processed due to insufficient inventory.')

    def track_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}'
        return "Order not found."

    def generate_report(self):
        print('\nInventory Report:')
        for product in self.inventory.values():
            supplier_name = self.suppliers[product.supplier_id].name
            print(f'Product ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}, Supplier: {supplier_name}')

        print('\nOrders Report:')
        for order in self.orders:
            print(f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}')

        print('\nSuppliers Report:')
        for supplier in self.suppliers.values():
            print(f'Supplier ID: {supplier.supplier_id}, Name: {supplier.name}, Contact Info: {supplier.contact_info}')

# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Adding suppliers
    s1 = Supplier(1, 'Acme Supplies', 'acme@supplies.com')
    s2 = Supplier(2, 'Widget Corp', 'contact@widgetcorp.com')
    scm.add_supplier(s1)
    scm.add_supplier(s2)

    # Adding products to inventory
    p1 = Product(1, 'Widget', 25.50, 100, s2.supplier_id)
    p2 = Product(2, 'Gadget', 15.75, 200, s1.supplier_id)
    scm.add_product(p1)
    scm.add_product(p2)

    # Processing an order
    o1 = Order(1, p1, 5, datetime.datetime.now())
    scm.process_order(o1)

    # Tracking an order
    order_info = scm.track_order(1)
    print(f'\nOrder Tracking Info: {order_info}')

    # Generating a report
    scm.generate_report()

    import datetime
from collections import deque

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id
        self.historical_demand = deque(maxlen=5)  # Store the last 5 demand values

    def update_historical_demand(self, demand):
        self.historical_demand.append(demand)

    def forecast_demand(self):
        if not self.historical_demand:
            return 0  # No historical data to base forecast on
        return sum(self.historical_demand) / len(self.historical_demand)

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status

class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.orders = []
        self.suppliers = {}

    def add_product(self, product):
        self.inventory[product.product_id] = product
        print(f'Product {product.name} added to inventory.')

    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier
        print(f'Supplier {supplier.name} added.')

    def process_order(self, order):
        product = self.inventory.get(order.product.product_id)
        if product and product.quantity >= order.quantity:
            product.quantity -= order.quantity
            product.update_historical_demand(order.quantity)
            order.update_status("Processed")
            self.orders.append(order)
            print(f'Order {order.order_id} processed.')
        else:
            order.update_status("Failed")
            print(f'Order {order.order_id} cannot be processed due to insufficient inventory.')

    def track_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}'
        return "Order not found."

    def generate_report(self):
        print('\nInventory Report:')
        for product in self.inventory.values():
            supplier_name = self.suppliers[product.supplier_id].name
            forecast_demand = product.forecast_demand()
            print(f'Product ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}, Supplier: {supplier_name}, Forecast Demand: {forecast_demand}')

        print('\nOrders Report:')
        for order in self.orders:
            print(f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}')

        print('\nSuppliers Report:')
        for supplier in self.suppliers.values():
            print(f'Supplier ID: {supplier.supplier_id}, Name: {supplier.name}, Contact Info: {supplier.contact_info}')

# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Adding suppliers
    s1 = Supplier(1, 'Acme Supplies', 'acme@supplies.com')
    s2 = Supplier(2, 'Widget Corp', 'contact@widgetcorp.com')
    scm.add_supplier(s1)
    scm.add_supplier(s2)

    # Adding products to inventory
    p1 = Product(1, 'Widget', 25.50, 100, s2.supplier_id)
    p2 = Product(2, 'Gadget', 15.75, 200, s1.supplier_id)
    scm.add_product(p1)
    scm.add_product(p2)

    # Processing orders
    o1 = Order(1, p1, 5, datetime.datetime.now())
    o2 = Order(2, p1, 8, datetime.datetime.now())
    scm.process_order(o1)
    scm.process_order(o2)

    # Tracking an order
    order_info = scm.track_order(1)
    print(f'\nOrder Tracking Info: {order_info}')

    # Generating a report
    scm.generate_report()
    import datetime
import hashlib

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id
        self.historical_demand = deque(maxlen=5)  # Store the last 5 demand values

    def update_historical_demand(self, demand):
        self.historical_demand.append(demand)

    def forecast_demand(self):
        if not self.historical_demand:
            return 0  # No historical data to base forecast on
        return sum(self.historical_demand) / len(self.historical_demand)

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.orders = []
        self.suppliers = {}
        self.blockchain = Blockchain()

    def add_product(self, product):
        self.inventory[product.product_id] = product
        print(f'Product {product.name} added to inventory.')
        self.add_blockchain_entry(f'Added product: {product.name}')

    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier
        print(f'Supplier {supplier.name} added.')
        self.add_blockchain_entry(f'Added supplier: {supplier.name}')

    def process_order(self, order):
        product = self.inventory.get(order.product.product_id)
        if product and product.quantity >= order.quantity:
            product.quantity -= order.quantity
            product.update_historical_demand(order.quantity)
            order.update_status("Processed")
            self.orders.append(order)
            print(f'Order {order.order_id} processed.')
            self.add_blockchain_entry(f'Processed order: {order.order_id}')
        else:
            order.update_status("Failed")
            print(f'Order {order.order_id} cannot be processed due to insufficient inventory.')

    def add_blockchain_entry(self, data):
        latest_block = self.blockchain.get_latest_block()
        new_block = Block(latest_block.index + 1, datetime.datetime.now(), data, latest_block.hash)
        self.blockchain.add_block(new_block)

    def track_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}'
        return "Order not found."

    def generate_report(self):
        print('\nInventory Report:')
        for product in self.inventory.values():
            supplier_name = self.suppliers[product.supplier_id].name
            forecast_demand = product.forecast_demand()
            print(f'Product ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}, Supplier: {supplier_name}, Forecast Demand: {forecast_demand}')

        print('\nOrders Report:')
        for order in self.orders:
            print(f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}')

        print('\nSuppliers Report:')
        for supplier in self.suppliers.values():
            print(f'Supplier ID: {supplier.supplier_id}, Name: {supplier.name}, Contact Info: {supplier.contact_info}')

        print('\nBlockchain Report:')
        for block in self.blockchain.chain:
            print(f'Index: {block.index}, Timestamp: {block.timestamp}, Data: {block.data}, Hash: {block.hash}, Previous Hash: {block.previous_hash}')

# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Adding suppliers
    s1 = Supplier(1, 'Acme Supplies', 'acme@supplies.com')
    s2 = Supplier(2, 'Widget Corp', 'contact@widgetcorp.com')
    scm.add_supplier(s1)
    scm.add_supplier(s2)

    # Adding products to inventory
    p1 = Product(1, 'Widget', 25.50, 100, s2.supplier_id)
    p2 = Product(2, 'Gadget', 15.75, 200, s1.supplier_id)
    scm.add_product(p1)
    scm.add_product(p2)

    # Processing orders
    o1 = Order(1, p1, 5, datetime.datetime.now())
    o2 = Order(2, p1, 8, datetime.datetime.now())
    scm.process_order(o1)
    scm.process_order(o2)

    # Tracking an order
    order_info = scm.track_order(1)
    print(f'\nOrder Tracking Info: {order_info}')

    # Generating a report
    scm.generate_report()

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id
        self.historical_demand = deque(maxlen=5)  # Store the last 5 demand values

    def update_historical_demand(self, demand):
        self.historical_demand.append(demand)

    def forecast_demand(self):
        if not self.historical_demand:
            return 0  # No historical data to base forecast on
        return sum(self.historical_demand) / len(self.historical_demand)

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status

class Block:
    def __init__(self, index, timestamp, data, previous_hash, encryption_key):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.encryption_key = encryption_key
        self.encrypted_data = self.encrypt_data(data)
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f'{self.index}{self.timestamp}{self.encrypted_data}{self.previous_hash}'.encode('utf-8'))
        return sha.hexdigest()

    def encrypt_data(self, data):
        fernet = Fernet(self.encryption_key)
        return fernet.encrypt(data.encode())

    def decrypt_data(self):
        fernet = Fernet(self.encryption_key)
        return fernet.decrypt(self.encrypted_data).decode()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.encryption_key = Fernet.generate_key()
import datetime

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date

class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.orders = []

    def add_product(self, product):
        self.inventory[product.product_id] = product
        print(f'Product {product.name} added to inventory.')

    def process_order(self, order):
        product = self.inventory.get(order.product.product_id)
        if product and product.quantity >= order.quantity:
            product.quantity -= order.quantity
            self.orders.append(order)
            print(f'Order {order.order_id} processed.')
        else:
            print(f'Order {order.order_id} cannot be processed due to insufficient inventory.')

    def generate_report(self):
        print('\nInventory Report:')
        for product in self.inventory.values():
            print(f'Product ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}')

        print('\nOrders Report:')
        for order in self.orders:
            print(f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Order Date: {order.order_date}')


# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Adding products to inventory
    p1 = Product(1, 'Apple', 25.50, 100)
    p2 = Product(2, 'Apple Sauce', 15.75, 200)
    scm.add_product(p1)
    scm.add_product(p2)

    # Processing an order
    o1 = Order(1, p1, 5, datetime.datetime.now())
    scm.process_order(o1)

    # Generating a report
    import datetime

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date

class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.orders = []
        self.suppliers = {}

    def add_product(self, product):
        self.inventory[product.product_id] = product
        print(f'Product {product.name} added to inventory.')

    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier
        print(f'Supplier {supplier.name} added.')

    def process_order(self, order):
        product = self.inventory.get(order.product.product_id)
        if product and product.quantity >= order.quantity:
            product.quantity -= order.quantity
            self.orders.append(order)
            print(f'Order {order.order_id} processed.')
        else:
            print(f'Order {order.order_id} cannot be processed due to insufficient inventory.')

    def generate_report(self):
        print('\nInventory Report:')
        for product in self.inventory.values():
            supplier_name = self.suppliers[product.supplier_id].name
            print(f'Product ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}, Supplier: {supplier_name}')

        print('\nOrders Report:')
        for order in self.orders:
            print(f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Order Date: {order.order_date}')

        print('\nSuppliers Report:')
        for supplier in self.suppliers.values():
            print(f'Supplier ID: {supplier.supplier_id}, Name: {supplier.name}, Contact Info: {supplier.contact_info}')

# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Adding suppliers
    s1 = Supplier(1, 'Acme Supplies', 'acme@supplies.com')
    s2 = Supplier(2, 'Widget Corp', 'contact@widgetcorp.com')
    scm.add_supplier(s1)
    scm.add_supplier(s2)

    # Adding products to inventory
    p1 = Product(1, 'Widget', 25.50, 100, s2.supplier_id)
    p2 = Product(2, 'Gadget', 15.75, 200, s1.supplier_id)
    scm.add_product(p1)
    scm.add_product(p2)

    # Processing an order
    o1 = Order(1, p1, 5, datetime.datetime.now())
    scm.process_order(o1)

    # Generating a report

    scm.generate_report()
    import datetime

    import datetime

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status

class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.orders = []
        self.suppliers = {}

    def add_product(self, product):
        self.inventory[product.product_id] = product
        print(f'Product {product.name} added to inventory.')

    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier
        print(f'Supplier {supplier.name} added.')

    def process_order(self, order):
        product = self.inventory.get(order.product.product_id)
        if product and product.quantity >= order.quantity:
            product.quantity -= order.quantity
            order.update_status("Processed")
            self.orders.append(order)
            print(f'Order {order.order_id} processed.')
        else:
            order.update_status("Failed")
            print(f'Order {order.order_id} cannot be processed due to insufficient inventory.')

    def track_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}'
        return "Order not found."

    def generate_report(self):
        print('\nInventory Report:')
        for product in self.inventory.values():
            supplier_name = self.suppliers[product.supplier_id].name
            print(f'Product ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}, Supplier: {supplier_name}')

        print('\nOrders Report:')
        for order in self.orders:
            print(f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}')

        print('\nSuppliers Report:')
        for supplier in self.suppliers.values():
            print(f'Supplier ID: {supplier.supplier_id}, Name: {supplier.name}, Contact Info: {supplier.contact_info}')

# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Adding suppliers
    s1 = Supplier(1, 'Acme Supplies', 'acme@supplies.com')
    s2 = Supplier(2, 'Widget Corp', 'contact@widgetcorp.com')
    scm.add_supplier(s1)
    scm.add_supplier(s2)

    # Adding products to inventory
    p1 = Product(1, 'Widget', 25.50, 100, s2.supplier_id)
    p2 = Product(2, 'Gadget', 15.75, 200, s1.supplier_id)
    scm.add_product(p1)
    scm.add_product(p2)

    # Processing an order
    o1 = Order(1, p1, 5, datetime.datetime.now())
    scm.process_order(o1)

    # Tracking an order
    order_info = scm.track_order(1)
    print(f'\nOrder Tracking Info: {order_info}')

    # Generating a report
    scm.generate_report()

    import datetime
from collections import deque

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id
        self.historical_demand = deque(maxlen=5)  # Store the last 5 demand values

    def update_historical_demand(self, demand):
        self.historical_demand.append(demand)

    def forecast_demand(self):
        if not self.historical_demand:
            return 0  # No historical data to base forecast on
        return sum(self.historical_demand) / len(self.historical_demand)

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status

class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.orders = []
        self.suppliers = {}

    def add_product(self, product):
        self.inventory[product.product_id] = product
        print(f'Product {product.name} added to inventory.')

    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier
        print(f'Supplier {supplier.name} added.')

    def process_order(self, order):
        product = self.inventory.get(order.product.product_id)
        if product and product.quantity >= order.quantity:
            product.quantity -= order.quantity
            product.update_historical_demand(order.quantity)
            order.update_status("Processed")
            self.orders.append(order)
            print(f'Order {order.order_id} processed.')
        else:
            order.update_status("Failed")
            print(f'Order {order.order_id} cannot be processed due to insufficient inventory.')

    def track_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}'
        return "Order not found."

    def generate_report(self):
        print('\nInventory Report:')
        for product in self.inventory.values():
            supplier_name = self.suppliers[product.supplier_id].name
            forecast_demand = product.forecast_demand()
            print(f'Product ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}, Supplier: {supplier_name}, Forecast Demand: {forecast_demand}')

        print('\nOrders Report:')
        for order in self.orders:
            print(f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}')

        print('\nSuppliers Report:')
        for supplier in self.suppliers.values():
            print(f'Supplier ID: {supplier.supplier_id}, Name: {supplier.name}, Contact Info: {supplier.contact_info}')

# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Adding suppliers
    s1 = Supplier(1, 'Acme Supplies', 'acme@supplies.com')
    s2 = Supplier(2, 'Widget Corp', 'contact@widgetcorp.com')
    scm.add_supplier(s1)
    scm.add_supplier(s2)

    # Adding products to inventory
    p1 = Product(1, 'Widget', 25.50, 100, s2.supplier_id)
    p2 = Product(2, 'Gadget', 15.75, 200, s1.supplier_id)
    scm.add_product(p1)
    scm.add_product(p2)

    # Processing orders
    o1 = Order(1, p1, 5, datetime.datetime.now())
    o2 = Order(2, p1, 8, datetime.datetime.now())
    scm.process_order(o1)
    scm.process_order(o2)

    # Tracking an order
    order_info = scm.track_order(1)
    print(f'\nOrder Tracking Info: {order_info}')

    # Generating a report
    scm.generate_report()
    import datetime
import hashlib

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id
        self.historical_demand = deque(maxlen=5)  # Store the last 5 demand values

    def update_historical_demand(self, demand):
        self.historical_demand.append(demand)

    def forecast_demand(self):
        if not self.historical_demand:
            return 0  # No historical data to base forecast on
        return sum(self.historical_demand) / len(self.historical_demand)

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.orders = []
        self.suppliers = {}
        self.blockchain = Blockchain()

    def add_product(self, product):
        self.inventory[product.product_id] = product
        print(f'Product {product.name} added to inventory.')
        self.add_blockchain_entry(f'Added product: {product.name}')

    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier
        print(f'Supplier {supplier.name} added.')
        self.add_blockchain_entry(f'Added supplier: {supplier.name}')

    def process_order(self, order):
        product = self.inventory.get(order.product.product_id)
        if product and product.quantity >= order.quantity:
            product.quantity -= order.quantity
            product.update_historical_demand(order.quantity)
            order.update_status("Processed")
            self.orders.append(order)
            print(f'Order {order.order_id} processed.')
            self.add_blockchain_entry(f'Processed order: {order.order_id}')
        else:
            order.update_status("Failed")
            print(f'Order {order.order_id} cannot be processed due to insufficient inventory.')

    def add_blockchain_entry(self, data):
        latest_block = self.blockchain.get_latest_block()
        new_block = Block(latest_block.index + 1, datetime.datetime.now(), data, latest_block.hash)
        self.blockchain.add_block(new_block)

    def track_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}'
        return "Order not found."

    def generate_report(self):
        print('\nInventory Report:')
        for product in self.inventory.values():
            supplier_name = self.suppliers[product.supplier_id].name
            forecast_demand = product.forecast_demand()
            print(f'Product ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}, Supplier: {supplier_name}, Forecast Demand: {forecast_demand}')

        print('\nOrders Report:')
        for order in self.orders:
            print(f'Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Status: {order.status}, Order Date: {order.order_date}')

        print('\nSuppliers Report:')
        for supplier in self.suppliers.values():
            print(f'Supplier ID: {supplier.supplier_id}, Name: {supplier.name}, Contact Info: {supplier.contact_info}')

        print('\nBlockchain Report:')
        for block in self.blockchain.chain:
            print(f'Index: {block.index}, Timestamp: {block.timestamp}, Data: {block.data}, Hash: {block.hash}, Previous Hash: {block.previous_hash}')

# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Adding suppliers
    s1 = Supplier(1, 'Acme Supplies', 'acme@supplies.com')
    s2 = Supplier(2, 'Widget Corp', 'contact@widgetcorp.com')
    scm.add_supplier(s1)
    scm.add_supplier(s2)

    # Adding products to inventory
    p1 = Product(1, 'Widget', 25.50, 100, s2.supplier_id)
    p2 = Product(2, 'Gadget', 15.75, 200, s1.supplier_id)
    scm.add_product(p1)
    scm.add_product(p2)

    # Processing orders
    o1 = Order(1, p1, 5, datetime.datetime.now())
    o2 = Order(2, p1, 8, datetime.datetime.now())
    scm.process_order(o1)
    scm.process_order(o2)

    # Tracking an order
    order_info = scm.track_order(1)
    print(f'\nOrder Tracking Info: {order_info}')

    # Generating a report
    scm.generate_report()

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id
        self.historical_demand = deque(maxlen=5)  # Store the last 5 demand values

    def update_historical_demand(self, demand):
        self.historical_demand.append(demand)

    def forecast_demand(self):
        if not self.historical_demand:
            return 0  # No historical data to base forecast on
        return sum(self.historical_demand) / len(self.historical_demand)

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status

class Block:
    def __init__(self, index, timestamp, data, previous_hash, encryption_key):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.encryption_key = encryption_key
        self.encrypted_data = self.encrypt_data(data)
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f'{self.index}{self.timestamp}{self.encrypted_data}{self.previous_hash}'.encode('utf-8'))
        return sha.hexdigest()

    def encrypt_data(self, data):
        fernet = Fernet(self.encryption_key)
        return fernet.encrypt(data.encode())

    def decrypt_data(self):
        fernet = Fernet(self.encryption_key)
        return fernet.decrypt(self.encrypted_data).decode()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.encryption_key = Fernet.generate_key()
