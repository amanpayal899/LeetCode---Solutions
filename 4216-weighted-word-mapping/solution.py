class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        map = ""
        for word in words:
            n = len(word)
            sum = 0
            for char in word:
                sum += weights[ord(char) - ord('a')]
            result = sum % 26
            result = chr(ord('z') - result)
            map = map + result
        return map
