file_path = "./expenses.txt"

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def gather_data():
    content = read_file(file_path)

    expenses = dict() 

    for line in content.splitlines():
        data = line.split(',')

        if data[0] in expenses.keys():
            expenses[data[0]] += float(data[1])
        else:
            expenses[data[0]] = float(data[1])
    
    return expenses

def output_results():
    expenses = gather_data()

    total = 0
    list_expenses = []
    most_expensive = ("", -1)

    for category,amount in expenses.items():
        total += amount
        list_expenses.append((category, amount))

        if amount > most_expensive[1]:
            most_expensive = (category, amount)

    print(f"Total: ${total:.2f}")

    for category, amount in list_expenses:
        print(f"{category}: ${amount:.2f}")

    print(f"Highest: {most_expensive[0]}")


if __name__ == "__main__":
    output_results()