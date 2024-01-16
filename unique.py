with open('words.txt', 'r') as file:
    content = file.read()
    elements = content.split()
    unique_elements = set(elements)
    unique=sorted(unique_elements)
    print(unique)
