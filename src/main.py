from utils import format_last_operations

count_operations = 5
data = format_last_operations(count_operations)
for item in data:
    if 'from' in item:
        print(f"{item['date']} {item['description']}\n"
              f"{item['from']} -> {item['to']}\n"
              f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}")
    else:
        print(f"{item['date']} {item['description']}\n"
              f"{item['to']}\n"
              f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}")
    print()
