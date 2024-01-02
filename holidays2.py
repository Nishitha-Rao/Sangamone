import csv
name=input("Enter the state")
with open('Holidays_2024.csv', 'r') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)
    # Read the header to get the column names
    header = next(csv_reader)
    # Determine the indice of the column of states
    state_index = header.index('States')
    column_indices = [state_index, header.index('Holidays'), header.index('Date')]
    for row in csv_reader:
        # Extract the state from the 'States' column
        state = row[state_index].replace("\n","")
        # Check if 'KA' is in the state string
        if name in state and not "National except" in state:
            print(row[column_indices[1]],"->",row[column_indices[2]]," : ",state)
        if "National" in state and not name in state:
            print(row[column_indices[1]],"->",row[column_indices[2]]," : ",state)
