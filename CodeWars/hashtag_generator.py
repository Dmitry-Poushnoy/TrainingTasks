def generate_hashtag(s):
    return f"#{s.title().replace(' ', '')}" if 0 < len(s) < 141 else False


if __name__ == '__main__':
    print(generate_hashtag('Codewars Is Nice'))
