# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    vowels = ["a", "i", "u", "e", "o"]
    count = 0
    for i in sentence:
        for j in vowels:
            if i == j:
                count += 1
    return count
