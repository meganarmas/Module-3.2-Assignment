# Objective: The goal of this assignment is to deepen your 
# understanding of tuple packing and unpacking in Python.

# Task 1: Customer Order Processing Refine your skills in 
# tuple unpacking by managing customer orders.

#Problem Statement: You are given a list of tuples, 
# each representing a customer's order. Each tuple 
# contains the customer's name, the product ordered, and 
# the quantity. Your task is to unpack each tuple and 
# print the order details in a user-friendly format.

# Sample Order Data:
# orders = [
#    ("Alice", "Laptop", 1),
#   ("Bob", "Camera", 2),
#    # More orders...
# ]
# - Write a function to iterate over the list of orders. - 
# Unpack each tuple in the list and format the details for display.

orders = [
    ("Charlie", "Guitar", 1),
    ("Claire", "Camera", 1),
    ("Aaron", "Laptop", 1),
    ("James", "Book", 3),
    ("Juliet", "Book", 7)
]

def print_orders(orders):
    for index, order in enumerate(orders, +1):
        name, item_ordered, quantity_order = order
        print(f"\nOrder number: {index}: ")
        print(f"Customer name: {name}")
        print(f"Item ordered: {item_ordered}")
        print(f"Quantity: {quantity_order}")



print_orders(orders)