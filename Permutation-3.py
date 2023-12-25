def perm3(word):
    if len(word) == 0:
        return ['']
    first_char = word[0]
    rest_permutations = perm3(word[1:])
    result = []
    for permutation in rest_permutations:
        for i in range(len(permutation) + 1):
            result.append(permutation[:i] + first_char + permutation[i:])    
    return result

# For three letter word
word = input("Ener a three letter word: ")
permutations_list = perm3(word)

for permutation in permutations_list:
    print(permutation)
