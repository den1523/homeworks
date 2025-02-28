def count_letter(some, letter):
    count = 0
    for word in some:
        if letter in word:
            count += 1
    return count

result = count_letter(['python', 'c++', 'c', 'scala', 'java'], 'c')
print(result)