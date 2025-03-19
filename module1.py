#!/usr/bin/python3  # Shebang line (if needed)
"""Module/docstring at very top"""
import os  # Built-in libraries first
import sys
from typing import Dict  # Standard library imports

# Third-party imports (with spacing)
import requests
import numpy as np

# Local imports
from .utils import helper_function

# Constants (ALL_CAPS)
API_ENDPOINT = "https://api.example.com"
TRUST_THRESHOLD = 70
def main():
    # Primary execution logic
         if __name__ == "__main__":
            main()  # Entry point for script execution
# Beginning: Imports & setup
import requests
import ipaddress
import sys
import os

# Middle: Function definitions
def sanitizeInput(inputs):
    # ...

    def getVersions(IPaddr):
    # ...

# End: Execution guard
        if __name__ == "__main__":
            print(getVersions(...))
import heapq

def secure_dijkstra(graph, start_node, trust_scores, min_trust=70):
    """
    Enhanced Dijkstra's algorithm for blockchain node routing with:
    - Trust-based path selection
    - Malicious node avoidance
    - Secure priority queue
    
    Parameters:
    graph (dict): Adjacency list {node: {neighbor: weight}}
    start_node (str): Starting node ID
    trust_scores (dict): {node: trust_score (0-100)}
    min_trust (int): Minimum acceptable trust score
    
    Returns:
    dict: Shortest distances from start node to all trusted nodes
    """
    
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    
    # Priority queue using heap structure
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip nodes below trust threshold
        if trust_scores.get(current_node, 0) < min_trust:
            continue
            
        for neighbor, weight in graph[current_node].items():
            # Only consider trusted neighbors
            if trust_scores.get(neighbor, 0) >= min_trust:
                distance = current_distance + weight
                
                # Update distance if shorter path found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances
# Define network topology with latency weights
blockchain_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

# Node trust scores from reputation system
node_trust = {
    'A': 95,
    'B': 85, 
    'C': 30,  # Marked as potentially malicious
    'D': 90
}

# Find secure paths from node A with minimum 70 trust
secure_paths = secure_dijkstra(
    graph=blockchain_graph,
    start_node='A',
    trust_scores=node_trust,
    min_trust=70
)

print("Secure Path Distances:")
print(secure_paths)

import datetime

import hashlib
import datetime
from collections import deque

# Example: AutoVPN Configuration for CUI Environments
mx75.configure(
    vpn_type="IPsec",
    encryption="aes256-gcm",
    dh_group=24,  # NSA Suite B
    ike_version=2,
    perfect_forward_secrecy=True,
    security_services={
        'ids_mode': 'prevention',
        'amp': 'block_all',
        'content_filter': 'strict'
    }
)

# RFID Scanner Simulation Class
class RFIDScanner:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.last_scan = None
        
    def scan_tag(self, product):
        """Simulates RFID tag scanning process"""
        self.last_scan = {
            'tag_id': product.product_id,
            'timestamp': datetime.datetime.now(),
            'product_data': {
                'name': product.name,
                'supplier_id': product.supplier_id
            }
        }
        return self.last_scan

# Enhanced Block Class with RFID Data
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(
            f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'.encode()
        ).hexdigest()

# Updated Supply Chain Management
class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.suppliers = {}
        self.blockchain = Blockchain()
        self.scanners = {}
        
    def register_scanner(self, scanner):
        self.scanners[scanner.serial] = scanner
        self.blockchain.add_block(Block(
            len(self.blockchain.chain),
            datetime.datetime.now(),
            f"Registered RFID Scanner: {scanner.serial}",
            self.blockchain.get_latest_block().hash
        ))

    def process_rfid_scan(self, scanner_serial, product_id):
        scanner = self.scanners.get(scanner_serial)
        if not scanner:
            raise ValueError("Unauthorized scanning device")
            
        product = self.inventory.get(product_id)
        if not product:
            self.blockchain.add_block(Block(
                len(self.blockchain.chain),
                datetime.datetime.now(),
                f"RFID Scan Error: Unknown product {product_id}",
                self.blockchain.get_latest_block().hash
            ))
            return False

        scan_data = scanner.scan_tag(product)
        supplier = self.suppliers.get(product.supplier_id)
        
        # Counterfeit verification
        alert = ""
        if self._check_counterfeit_supplier(supplier.name, supplier.contact_info):
            alert = "COUNTERFEIT SUPPLIER ALERT! "
            product.is_counterfeit = True
            
        if self._check_counterfeit_product(product.name, supplier.name):
            alert += "COUNTERFEIT PRODUCT DETECTED! "
            product.is_counterfeit = True

        block_data = (
            f"RFID Scan: Product {product.name} ({product_id}) | "
            f"Supplier: {supplier.name} | "
            f"Scanner: {scanner_serial} | "
            f"Status: {'CLEAN' if not product.is_counterfeit else 'FLAGGED'} | "
            f"{alert}"
        )
        
        self.blockchain.add_block(Block(
            len(self.blockchain.chain),
            datetime.datetime.now(),
            block_data,
            self.blockchain.get_latest_block().hash
        ))
        
        return True

    # Existing counterfeit check methods
    def _check_counterfeit_supplier(self, name, location):
        return any(s['name'].lower() == name.lower() and 
                  s['location'].lower() == location.lower()
                  for s in COUNTERFEIT_SUPPLIERS)

    def _check_counterfeit_product(self, product_name, supplier_name):
        for supplier in COUNTERFEIT_SUPPLIERS:
            if supplier['name'].lower() == supplier_name.lower():
                return any(p.lower() == product_name.lower() 
                          for p in supplier['products'])
        return False

# Example Usage
if __name__ == "__main__":
    scm = SupplyChainManagement()
    
    # Initialize RFID Scanner
    scanner = RFIDScanner("RFID-007")
    scm.register_scanner(scanner)
    
    # Add test supplier and product
    supplier = Supplier(1, "Huajie Electronics", "Shenzhen, China")
    product = Product(1, "Electromagnetic Interference Filters", 150.00, 100, 1)
    
    scm.add_supplier(supplier)
    scm.add_product(product)
    
    # Simulate RFID scan
    scm.process_rfid_scan("RFID-007", 1)
    
    # Generate report
    scm.generate_report()

class product:
    def __init__(self, product):
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
    p1 = Product(1, 'Integrated Circuits', 25.50, 100)
    p2 = Product(2, 'TCAS System Parts', 15.75, 200)
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
        from cryptography.fernet import Fernet
import datetime
import hashlib
from collections import deque

# Counterfeit supplier database
COUNTERFEIT_SUPPLIERS = [
    {
        "name": "Hong Dark Electronic Trade",
        "location": "Shenzhen, China",
        "products": ["Integrated Circuits", "TCAS System Parts"],
        "case": "Supplied 84,000 counterfeit parts to DoD (2012-2018)"
    },
    {
        "name": "Huajie Electronics", 
        "location": "Shenzhen, China",
        "products": ["Electromagnetic Interference Filters"],
        "case": "Parts used in SH-60B helicopters via Raytheon subcontractors"
    },
    {
        "name": "Unmarked/Counterfeit Firearms Manufacturers",
        "location": "Hungary, Romania",
        "products": ["Small Arms (Western-caliber)"],
        "case": "Linked to gray-market arms sales for Middle Eastern clients"
    }
]

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id
        self.historical_demand = deque(maxlen=5)
        self.is_counterfeit = False  
        
 # New counterfeit flag

    def update_historical_demand(self, demand):
        self.historical_demand.append(demand)

    def forecast_demand(self):
        return sum(self.historical_demand)/len(self.historical_demand) if self.historical_demand else 0

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info
        self.is_counterfeit = False  
        
# New counterfeit flag

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        self.chain.append(new_block)

class SupplyChainManagement:
    def __init__(self):
        self.inventory = {}
        self.orders = []
        self.suppliers = {}
        self.blockchain = Blockchain()
    
    def _check_counterfeit_supplier(self, supplier_name, supplier_location):
        return any(s['name'].lower() == supplier_name.lower() and 
                   s['location'].lower() == supplier_location.lower()
                   for s in COUNTERFEIT_SUPPLIERS)
    
    def _check_counterfeit_product(self, product_name, supplier_name):
        for supplier in COUNTERFEIT_SUPPLIERS:
            if supplier['name'].lower() == supplier_name.lower():
                return any(p.lower() == product_name.lower() 
                          for p in supplier['products'])
        return False

    def add_supplier(self, supplier):
        # Counterfeit check
        if self._check_counterfeit_supplier(supplier.name, supplier.contact_info):
            supplier.is_counterfeit = True
            self.blockchain.add_block(Block(
                len(self.blockchain.chain),
                datetime.datetime.now(),
                f"COUNTERFEIT WARNING: Supplier {supplier.name} added",
                self.blockchain.get_latest_block().hash
            ))
            print(f"WARNING: Flagged counterfeit supplier - {supplier.name}")
        
        self.suppliers[supplier.supplier_id] = supplier
        self.blockchain.add_block(Block(
            len(self.blockchain.chain),
            datetime.datetime.now(),
            f"Supplier {supplier.name} added",
            self.blockchain.get_latest_block().hash
        ))

    def add_product(self, product):
        supplier = self.suppliers.get(product.supplier_id)
        if supplier:
            # Check both supplier and product
            if supplier.is_counterfeit or self._check_counterfeit_product(product.name, supplier.name):
                product.is_counterfeit = True
                self.blockchain.add_block(Block(
                    len(self.blockchain.chain),
                    datetime.datetime.now(),
                    f"COUNTERFEIT ALERT: Product {product.name} from {supplier.name}",
                    self.blockchain.get_latest_block().hash
                ))
                print(f"SECURITY ALERT: Counterfeit product detected - {product.name}")
        
        self.inventory[product.product_id] = product
        self.blockchain.add_block(Block(
            len(self.blockchain.chain),
            datetime.datetime.now(),
            f"Product {product.name} added",
            self.blockchain.get_latest_block().hash
        ))

    def generate_report(self):
        print("\nSecurity Audit Report:")
        for product in self.inventory.values():
            supplier = self.suppliers.get(product.supplier_id)
            status = "COUNTERFEIT" if product.is_counterfeit else "CLEAN"
            print(f"Product: {product.name} | Supplier: {supplier.name} | Status: {status}")
        
        print("\nBlockchain Integrity Report:")
        for block in self.blockchain.chain:
            print(f"Block {block.index}: {block.data} | Hash: {block.hash[:10]}...")

# Example Usage
if __name__ == "__main__":
    scm = SupplyChainManagement()
    
    if __name__ == "__main__":
        scm = SupplyChainManagement()
    
    # Add known counterfeit supplier
    bad_supplier = Supplier(1, "Huajie Electronics", "Shenzhen, China")
    scm.add_supplier(bad_supplier)
    
    # Add product from counterfeit supplier
    bad_product = Product(1, "Electromagnetic Interference Filters", 150.00, 100, 1)
    scm.add_product(bad_product)
    
    # Generate security report
    scm.generate_report()



