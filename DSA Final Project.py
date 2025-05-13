class Node:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.next = None


class InventoryLinkedList:
    def __init__(self):
        self.head = None

    def add(self, name, quantity):
        if self.find(name):
            return False
        new_node = Node(name, quantity)
        new_node.next = self.head
        self.head = new_node
        return True

    def update(self, name, quantity):
        node = self.find(name)
        if node:
            node.quantity = quantity
            return True
        return False

    def remove(self, name):
        prev = None
        curr = self.head
        while curr:
            if curr.name == name:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def find(self, name):
        current = self.head
        while current:
            if current.name == name:
                return current
            current = current.next
        return None

    def view(self):
        current = self.head
        if not current:
            print("Inventory is empty.")
            return
        print("\n--- Inventory ---")
        while current:
            print(f"{current.name}: {current.quantity}")
            current = current.next
        print()


class Warehouse:
    def __init__(self):
        self.inventory = InventoryLinkedList()
        self.undo_stack = []
        self.waitlist = {}

    def add_item(self, name, quantity):
        if self.inventory.add(name, quantity):
            self.undo_stack.append(('remove', name))
            print(f"Item '{name}' added with quantity {quantity}.")
        else:
            print(f"Item '{name}' already exists.")

    def update_item(self, name, quantity):
        node = self.inventory.find(name)
        if not node:
            print(f"Item '{name}' does not exist.")
            return
        self.undo_stack.append(('update', name, node.quantity))
        self.inventory.update(name, quantity)
        print(f"Item '{name}' updated to quantity {quantity}.")
        if quantity == 0 and name in self.waitlist and self.waitlist[name]:
            print(f"Note: '{name}' is out of stock. Waitlist: {', '.join(self.waitlist[name])}")

    def remove_item(self, name):
        node = self.inventory.find(name)
        if not node:
            print(f"Item '{name}' not found.")
            return
        self.undo_stack.append(('add', name, node.quantity))
        self.inventory.remove(name)
        print(f"Item '{name}' removed from inventory.")

    def view_inventory(self):
        self.inventory.view()

    def add_to_waitlist(self, name, customer):
        if name not in self.waitlist:
            self.waitlist[name] = []
        self.waitlist[name].append(customer)
        print(f"{customer} added to waitlist for '{name}'.")

    def view_waitlist(self, name):
        if name in self.waitlist and self.waitlist[name]:
            print(f"Waitlist for '{name}': {', '.join(self.waitlist[name])}")
        else:
            print(f"No waitlist for '{name}'.")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        action = self.undo_stack.pop()
        if action[0] == 'remove':
            self.inventory.remove(action[1])
            print(f"Undo: Removed '{action[1]}'")
        elif action[0] == 'add':
            self.inventory.add(action[1], action[2])
            print(f"Undo: Re-added '{action[1]}' with quantity {action[2]}")
        elif action[0] == 'update':
            self.inventory.update(action[1], action[2])
            print(f"Undo: Restored '{action[1]}' to quantity {action[2]}")


def main():
    warehouse = Warehouse()

    while True:
        print("\n--- Warehouse Inventory Manager ---")
        print("1. Add Item")
        print("2. Update Item Quantity")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. Add Customer to Waitlist")
        print("6. View Waitlist")
        print("7. Undo Last Operation")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            name = input("Enter Item Name: ").strip()
            try:
                quantity = int(input("Enter Quantity: "))
                warehouse.add_item(name, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")

        elif choice == "2":
            name = input("Enter Item Name to Update: ").strip()
            try:
                quantity = int(input("Enter New Quantity: "))
                warehouse.update_item(name, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")

        elif choice == "3":
            name = input("Enter Item Name to Remove: ").strip()
            warehouse.remove_item(name)

        elif choice == "4":
            warehouse.view_inventory()

        elif choice == "5":
            name = input("Enter Item Name: ").strip()
            customer = input("Enter Customer Name: ").strip()
            warehouse.add_to_waitlist(name, customer)

        elif choice == "6":
            name = input("Enter Item Name to View Waitlist: ").strip()
            warehouse.view_waitlist(name)

        elif choice == "7":
            warehouse.undo()

        elif choice == "8":
            print("Exiting Warehouse Inventory Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
