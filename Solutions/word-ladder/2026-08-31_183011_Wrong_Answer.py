# Problem: Word Ladder
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-31_183011 UTC
# URL: https://leetcode.com/submissions/detail/2126491232/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque()
        queue.appendleft((beginWord, 1))
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        while queue:
            word, level = queue.pop()
            if word == endWord:
                return level
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i]+ch+word[i+1:]
                    if new_word in wordSet:
                        queue.append((new_word, level+1))
                        wordSet.remove(new_word)
        return 0