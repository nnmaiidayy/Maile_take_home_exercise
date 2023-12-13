# Author   : Mai Le
# Email    : mai@umass.edu
# Spire ID : 4132105723

class VendingMachine:
    def __init__(self):
        self.snacks = dict()
        self.bal = 0.0
        self.total = 0.00
        self.lst = []

    def list_items(self):
        if not self.snacks:
            print("No items in the vending machine")
        else:
            print("Available items:")
            for snack in sorted(self.snacks):
                cost = self.snacks[snack]['cost']
                quantity = self.snacks[snack]['quantity']
                print(f"{snack} (${cost}): {quantity} available")
    
    def add_item(self, name, cost, quantity):
        if name in self.snacks:
            self.snacks[name]['cost'] = cost
            self.snacks[name]['quantity'] += quantity
        else:
            self.snacks[name] = {'cost':cost, 'quantity':quantity}
        print(f"{quantity} {name}(s) added to inventory")

    
    def insert_money(self, amount):
        if amount == 1 or amount == 2 or amount == 3:
            self.bal += amount
            print(f"Balance: ${self.bal:.2f}")
        else:
            print("Invalid amount")

    def purchase(self, snack):
        if snack not in self.snacks:
            print("Invalid item")
        elif self.snacks[snack]['quantity'] == 0:
            print(f"Sorry {snack} is out of stock")
        elif self.bal < self.snacks[snack]['cost']:
            print(f"Insufficient balance. Price of {snack} is {self.snacks[snack]['cost']}")
        else:
            self.snacks[snack]['quantity'] -= 1
            self.bal -= self.snacks[snack]['cost']
            self.total += self.snacks[snack]['cost']
            self.total = round(self.total, 2)
            self.lst.append({'item': snack, 'sale': self.snacks[snack]['cost']})
            print(f"Purchased {snack}")
            print(f"Balance: {self.bal:.2f}")

    def display_change(self):
        if self.bal == 0:
            print("No change")
        else:
            print(f"Change: ${self.bal:.2f}")
            self.bal = 0

    def get_item_price(self, snack):
        if snack in self.snacks:
            return self.snacks[snack]['cost']
        else:
            print("Invalid item")

    def empty_inventory(self):
        self.snacks.clear()
        print("Inventory cleared")

    def get_total_sales(self):
        return self.total

    def get_item_quantity(self, snack):
        if snack in self.snacks:
            return self.snacks[snack]['quantity']
        else:
            print("Invalid item")

    def remove_item(self, snack):
        if snack in self.snacks:
            del self.snacks[snack]
            print(f"{snack} removed from inventory")
        else:
            print("Invalid item")
    
    def stats(self, N):
        if not self.lst:
            print("No sale history in the vending machine")
        else:
            length = len(self.lst)
            N = min(N, length)
            data = dict()
            for sale in self.lst[-N:]:
                item = sale['item']
                data[item] = data.get(item, {'total': 0, 'quantity': 0})
                data[item]['total'] += sale['sale']
                data[item]['quantity'] += 1

            print(f"Sale history for the most recent {N} purchase(s):")
            for item in sorted(data):
                total_sale = data[item]['total']
                quantity = data[item]['quantity']
                print(f"{item}: ${total_sale:.2f} for {quantity} purchase(s)")

    
