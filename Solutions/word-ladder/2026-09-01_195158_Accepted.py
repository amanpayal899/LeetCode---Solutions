# Problem: Word Ladder
# Status: Accepted
# Language: python3
# Runtime: 282 ms
# Memory: 20.5 MB
# Submitted: 2026-09-01_195158 UTC
# URL: https://leetcode.com/submissions/detail/2127710658/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque()
        queue.append((beginWord, 1))
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i]+ch+word[i+1:]
                    if new_word in wordSet:
                        queue.append((new_word, level+1))
                        wordSet.remove(new_word)
        return 0