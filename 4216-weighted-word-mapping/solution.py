class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alphabet_string = "abcdefghijklmnopqrstuvwxyz"
        #weight           [__________________________]
        result = ""
        for word in words:
            sum = 0
            for character in word:
                sum += weights[alphabet_string.index(character)]
            result += alphabet_string[25 - (sum % 26)]
        return result
