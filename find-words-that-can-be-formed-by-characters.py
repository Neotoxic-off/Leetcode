class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = {}
        for char in chars:
            char_count[char] = char_count.get(char, 0) + 1

        def can_form_word(word):
            word_count = {}
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1
            for char, count in word_count.items():
                if char not in char_count or count > char_count[char]:
                    return False

            return True
        result = 0
        for word in words:
            if can_form_word(word):
                result += len(word)

        return result

    
