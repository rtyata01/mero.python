class Inventory:
    """
    A class to manage the product inventory for a shop.
    """
    
    def __init__(self):
        """
        Initializes an empty inventory.
        """
        self.products = {}
    
    def add_product(self, product_name, quantity, price):
        """
        Adds a new product to the inventory or updates the quantity if it already exists.
        
        Parameters:
        product_name (str): The name of the product.
        quantity (int): The quantity of the product.
        price (float): The price of the product.
        """
        if product_name in self.products:
            self.products[product_name]['quantity'] += quantity
        else:
            self.products[product_name] = {'quantity': quantity, 'price': price}
        print(f"Added/Updated product '{product_name}' with quantity {quantity} and price {price}.")

    def view_inventory(self):
        """
        Displays the current inventory.
        """
        if not self.products:
            print("The inventory is empty.")
            return
        
        print(f"{'Product Name':<20} {'Quantity':<10} {'Price':<10}")
        print("-" * 40)
        for product_name, details in self.products.items():
            print(f"{product_name:<20} {details['quantity']:<10} ${details['price']:<10.2f}")

    def update_quantity(self, product_name, quantity):
        """
        Updates the quantity of an existing product.
        
        Parameters:
        product_name (str): The name of the product.
        quantity (int): The new quantity of the product.
        """
        if product_name in self.products:
            self.products[product_name]['quantity'] = quantity
            print(f"Updated quantity of '{product_name}' to {quantity}.")
        else:
            print(f"Product '{product_name}' not found in the inventory.")

    def remove_product(self, product_name):
        """
        Removes a product from the inventory.
        
        Parameters:
        product_name (str): The name of the product to remove.
        """
        if product_name in self.products:
            del self.products[product_name]
            print(f"Removed product '{product_name}' from the inventory.")
        else:
            print(f"Product '{product_name}' not found in the inventory.")


def main():
    """
    Main function to interact with the Inventory class.
    """
    inventory = Inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Add/Update Product")
        print("2. View Inventory")
        print("3. Update Quantity")
        print("4. Remove Product")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: $"))
            inventory.add_product(product_name, quantity, price)
        
        elif choice == '2':
            inventory.view_inventory()
        
        elif choice == '3':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter new quantity: "))
            inventory.update_quantity(product_name, quantity)
        
        elif choice == '4':
            product_name = input("Enter product name to remove: ")
            inventory.remove_product(product_name)
        
        elif choice == '5':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
