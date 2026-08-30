# Problem: Weighted Word Mapping
# Status: Accepted
# Language: python3
# Runtime: 11 ms
# Memory: 19.3 MB
# Submitted: 2026-06-13_193555 UTC
# URL: https://leetcode.com/submissions/detail/2032129905/

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