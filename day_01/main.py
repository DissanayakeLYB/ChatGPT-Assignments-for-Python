input_file_path = "./expensesa.txt"
output_file_path = "./report.txt"


def read_file(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file \'{input_file_path}\' was not found.")
        return ""

def gather_data():
    content = read_file(input_file_path)

    expenses = dict() 

    for line in content.splitlines():
        data = line.split(',')

        if data[0] in expenses:
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

    return total, list_expenses, most_expensive


def write_output():
    outputs = output_results()

    with open(output_file_path, 'w') as file:
        file.write(f"Total: {outputs[0]}\n")

        for category, amount in outputs[1]:
            file.write(f"{category}: {amount}\n")

        file.write(f"Highest: {outputs[2][0]}")


if __name__ == "__main__":
    write_output()