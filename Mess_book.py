class Mess:
  def __init__(self, name, mess_price=0):
    self.name = name
    self.entries = {}
    self.mess_price = mess_price

  def add_detail(self, date, count):
    if date not in self.entries:
      self.entries[date] = 0
    self.entries[date] += count
    print(f"Added {count} plate for {date}")

  def display_total(self):
    total_rottis = sum(self.entries.values())
    total_cost = total_rottis * self.mess_price
    print(f"\nTotal plates for {self.name}: {total_rottis}")
    print(f"Total cost: ₹{total_cost}")

mess_book = Mess("Sagar", mess_price=70)
mess_book.add_detail("2023-10-26", 1)
mess_book.add_detail("2023-10-27", 1)
mess_book.add_detail("2023-10-26", 1)
mess_book.display_total()

