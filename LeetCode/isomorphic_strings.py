class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        _vocabulary1 = {}
        for i in range(len(s)):
            _vocabulary1[s[i]] = t[i]
        _vocabulary2 = {}
        for _key, _val in _vocabulary1.items():
            _vocabulary2[_val] = _key
        word_for_check = ""
        for letter in t:
            try:
                word_for_check += _vocabulary2[letter]
            except:
                return False
        if word_for_check == s:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.is_isomorphic("foo", "bar"))

# Если разная длина, то False
# создаём словарь соответствий букв: ключ - 1, значение - 2
# разворачиваем словарь
# генерируем проверочное слово 1
# если проверочоное слово равно первому, то True
