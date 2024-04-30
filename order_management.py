
class Order:
    def __init__(self, order_id, total_bill, payment_method):
        #load order attributes.
        self.order_id = order_id
        self.total_bill = total_bill
        self.payment_method = payment_method

    def __str__(self):
        #Return a string 
        return f"order id: {self.order_id}, total bill: ${self.total_bill}, payment method: {self.payment_method}"


class DineInOrder(Order):
    def __init__(self, order_id, total_bill, payment_method, table_number):
        super().__init__(order_id, total_bill, payment_method)
        self.table_number = table_number 

    def __str__(self):
        order_info = super().__str__()
        return f"{order_info}, table number: {self.table_number}"

class DeliveryOrder(Order):
    pass  # No additional functionalities required for delivery order.

# Example usage:
# For DineInOrder
dine_in_order = DineInOrder('A12', 30.00, 'cash', 6)
# For DeliveryOrder
delivery_order = DeliveryOrder('A23', 25.00, 'card')

# Print order details.
print("Dine-in order details:")
print(dine_in_order)
print("\nDelivery order details:")
print(delivery_order)
