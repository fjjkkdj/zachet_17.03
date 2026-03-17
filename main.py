from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Предмет", "Шанс"]
table.add_row(["Золотой меч", "0.5%"])
table.add_row(["Алмазный шлем", "0.1%"])
print(table)