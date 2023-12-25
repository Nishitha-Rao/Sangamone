def perm3(word3):
    s1, s2, s3 = word3
    return [s1 + s2 + s3, s1 + s3 + s2, s2 + s1 + s3, s2 + s3 + s1, s3 + s1 + s2, s3 + s2 + s1]

def perm4(word4):
    s1, s2, s3, s4 = word4
    result = []
    result.extend([s1 + x for x in perm3(s2 + s3 + s4)])
    result.extend([s2 + x for x in perm3(s1 + s3 + s4)])
    result.extend([s3 + x for x in perm3(s1 + s2 + s4)])
    result.extend([s4 + x for x in perm3(s1 + s2 + s3)])
    return result

def perm5(word5):
    s1, s2, s3, s4, s5 = word5
    result = []
    result.extend([s1 + x for x in perm4(s2 + s3 + s4 + s5)])
    result.extend([s2 + x for x in perm4(s1 + s3 + s4 + s5)])
    result.extend([s3 + x for x in perm4(s1 + s2 + s4 + s5)])
    result.extend([s4 + x for x in perm4(s1 + s2 + s3 + s5)])
    result.extend([s5 + x for x in perm4(s1 + s2 + s3 + s4)])
    return result

input1 = input("Enter a word: ")
len1 = len(input1)

if len1 == 3:
    result = perm3(input1)
elif len1 == 4:
    result = perm4(input1)
elif len1 == 5:
    result = perm5(input1)

print(result)

