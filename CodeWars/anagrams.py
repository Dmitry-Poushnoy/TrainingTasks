def anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]

if __name__ == '__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))