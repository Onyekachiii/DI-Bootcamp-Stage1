class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, new_name):
        self.name = new_name

    def set_price(self, new_price):
        self.price = new_price


class MenuEditor:
    def __init__(self):
        self.menu = []

    def add_item_to_menu(self, name, price):
        item = MenuItem(name, price)
        self.menu.append(item)

    def remove_item_from_menu(self, name):
        for item in self.menu:
            if item.get_name() == name:
                self.menu.remove(item)
                return True
        return False

    def update_item_in_menu(self, name, price, new_name, new_price):
        for item in self.menu:
            if item.get_name() == name and item.get_price() == price:
                item.set_name(new_name)
                item.set_price(new_price)
                return True
        return False

    def show_restaurant_menu(self):
        print("Restaurant Menu:")
        for item in self.menu:
            print(f"{item.get_name()} - ${item.get_price()}")

    def show_user_menu(self):
        print("Menu Editor")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        choice = input("Enter your choice: ")
        self.handle_user_choice(choice)

    def handle_user_choice(self, choice):
        if choice == "V":
            self.view_item()
        elif choice == "A":
            self.add_item()
        elif choice == "D":
            self.delete_item()
        elif choice == "U":
            self.update_item()
        elif choice == "S":
            self.show_restaurant_menu()
        else:
            print("Invalid choice. Please try again.")

    def view_item(self):
        name = input("Enter the name of the item: ")
        price = input("Enter the price of the item: ")
        found = False
        for item in self.menu:
            if item.get_name() == name and item.get_price() == price:
                print(f"{item.get_name()} - ${item.get_price()}")
                found = True
                break
        if not found:
            print("Item not found.")

    def add_item(self):
        name = input("Enter the name of the item: ")
        price = input("Enter the price of the item: ")
        self.add_item_to_menu(name, price)
        print("Item added successfully.")

    def delete_item(self):
        name = input("Enter the name of the item: ")
        if self.remove_item_from_menu(name):
            print("Item deleted successfully.")
        else:
            print("Error deleting item.")

    def update_item(self):
        name = input("Enter the name of the item: ")
        price = input("Enter the price of the item: ")
        new_name = input("Enter the new name of the item: ")
        new_price = input("Enter the new price of the item: ")
        if self.update_item_in_menu(name, price, new_name, new_price):
            print("Item updated successfully.")
        else:
            print("Error updating item.")


menu_editor = MenuEditor()
while True:
    menu_editor.show_user_menu()
    choice = input("Do you want to continue editing the menu? (Y/N) ")
    if choice == "N":
        menu_editor.show_restaurant_menu()
        break