class MenuItem:
  """
  This class represents a single item on the restaurant menu.
  """
  def __init__(self, name, description, price):
    """
    Initializes a menu item with name, description, and price.
 
    Args:
      name: The name of the menu item (string).
      description: A description of the item (string).
      price: The price of the item (float).
    """
    self.name = name
    self.description = description
    self.price = price
 
  def display_info(self):
    """
    Prints the menu item's name, description, and price in a formatted way.
    """
    print(f"{self.name:<20}: {self.description} (${self.price:.2f})")
 
 
class RestaurantMenu:
  """
  This class represents a restaurant menu with a list of menu items.
  """
  def __init__(self, name):
    """
    Initializes the restaurant menu with a name and an empty list of items.
 
    Args:
      name: The name of the restaurant (string).
    """
    self.name = name
    self.menu_items = []
 
  def add_item(self, item):
    """
    Adds a new menu item to the list.
 
    Args:
      item: A MenuItem object to add to the menu.
    """
    self.menu_items.append(item)
 
  def remove_item(self, name):
    """
    Removes a menu item from the list by name.
 
    Args:
      name: The name of the item to remove (string).
    """
    for item in self.menu_items:
      if item.name == name:
        self.menu_items.remove(item)
        print(f"Item '{name}' removed from the menu.")
        return
    print(f"Item '{name}' not found on the menu.")
 
  def display_menu(self):
    """
    Prints the entire restaurant menu with item details.
    """
    print(f"\n** {self.name} Menu **")
    for item in self.menu_items:
      item.display_info()
    print("")
 
 
def main():
  """
  Main function to create and manage the restaurant menu.
  """
  restaurant_name = input("Enter restaurant name: ")
  menu = RestaurantMenu(restaurant_name)
 
  while True:
    print("\nMenu:")
    print("1. Add Menu Item")
    print("2. Remove Menu Item")
    print("3. Display Menu")
    print("4. Exit")
 
    choice = input("Enter your choice (1-4): ")
 
    if choice == "1":
      name = input("Enter item name: ")
      description = input("Enter item description: ")
      try:
        price = float(input("Enter item price: "))
        menu.add_item(MenuItem(name, description, price))
        print(f"Item '{name}' added to the menu.")
      except ValueError:
        print("Invalid input: Please enter a valid price (number).")
 
    elif choice == "2":
      name = input("Enter item name to remove: ")
      menu.remove_item(name)
 
    elif choice == "3":
      menu.display_menu()
 
    elif choice == "4":
      print("Exiting...")
      break
 
    else:
      print("Invalid choice. Please try again.")
 
 
if __name__ == "__main__":
  main()
 