import csv
name = input("Enter the state: ").upper()
l = [
    "AP", "AR", "AS", "BR", "CG", "GA", "GJ", "HR", "HP", "JH",
    "KA", "KL", "MP", "MH", "MN", "ML", "MZ", "NL", "OD", "PB", "RJ",
    "SK", "TN", "TG", "TR", "UP", "UK", "WB",
    "AN", "CH", "DN", "DD", "DL", "LD", "PY", "JK", "LA"
]
if name not in l:
    print("Invalid input")
else:
    with open('Holidays_2024.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        state_index = header.index('States')
        column_indices = [state_index, header.index('Holidays'), header.index('Date'),header.index('Day')]
        for row in csv_reader:
            state = row[state_index].replace("\n","")
            if name in state and not "National except" in state:
                print(row[column_indices[1]],"->",row[column_indices[2]],":",row[column_indices[3]])
            if "National" in state and not name in state:
                print(row[column_indices[1]],"->",row[column_indices[2]],":",row[column_indices[3]])
