# Restaurant Order Management System

## Overview
This Restaurant Order Management System is designed to help restaurants efficiently manage both dine-in and delivery orders. It supports real-time tracking of orders and their billing processes. The system categorizes orders by order ID, total bill, payment method, and, for dine-in orders, table number.

## System Requirements
- Python 3.x

## Installation
No external libraries are required for this project. You can run it with any standard Python interpreter. Simply download the script and run it in your Python environment.

## Components
The system consists of three main classes:
- `Order`: The base class for handling general order details such as order ID, total bill, and payment method.
- `DineInOrder`: Inherits from `Order` and adds functionality to handle table numbers for dine-in customers.
- `DeliveryOrder`: Inherits from `Order` and is used for delivery orders without additional attributes.

## Usage
To create orders, initialize objects from either the `DineInOrder` or `DeliveryOrder` class, and then print them to view order details.

### Example Code
```python
# For DineInOrder
dine_in_order = DineInOrder('A12', 30.00, 'cash', 6)

# For DeliveryOrder
delivery_order = DeliveryOrder('A23', 25.00, 'card')

# Print order details
print("Dine-in order details:")
print(dine_in_order)
print("\nDelivery order details:")
print(delivery_order)
```

## Features
- Real-time data tracking of order details.
- Supports multiple payment methods.
- Categorizes orders efficiently for dine-in and delivery services.

## Future Enhancements
- Integration with a database for persistent storage.
- Implementation of a user interface for easier management.
- Real-time updates to kitchen and delivery staff.

For further assistance or feedback on the system, feel free to reach out or open an issue in the project repository.
