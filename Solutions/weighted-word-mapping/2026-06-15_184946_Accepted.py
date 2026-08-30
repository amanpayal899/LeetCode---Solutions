# Problem: Weighted Word Mapping
# Status: Accepted
# Language: python3
# Runtime: 8 ms
# Memory: 19.2 MB
# Submitted: 2026-06-15_184946 UTC
# URL: https://leetcode.com/submissions/detail/2034331902/

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