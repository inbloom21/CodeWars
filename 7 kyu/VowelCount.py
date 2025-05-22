def get_count(sentence):
    vowels = ["a", "i", "u", "e", "o"]
    count = 0
    for i in sentence:
        for j in vowels:
            if i == j:
                count += 1
    return count

print(get_count("halo nama saya ibra"))