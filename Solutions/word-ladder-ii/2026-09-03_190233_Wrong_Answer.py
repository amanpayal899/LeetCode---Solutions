# Problem: Word Ladder II
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-09-03_190233 UTC
# URL: https://leetcode.com/submissions/detail/2130020451/

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        level = float('inf')
        queue = deque()
        result = []
        queue.append(([beginWord], 1))
        if beginWord in word_set:
            word_set.remove(beginWorld)
        t = 0
        while queue:
            word_seq, curr_level = queue.popleft()
            curr_word = word_seq[-1]
            if curr_word == endWord:
                if level < curr_level:
                    return result
                result.append(word_seq)
                level = curr_level
            else:
                for i in range(len(curr_word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = curr_word[:i] + ch + curr_word[i+1:]
                        if new_word in word_set:
                            word_set.remove(new_word)
                            word_seq.append(new_word)
                            queue.append((word_seq, curr_level+1) )
                            
        return result

            
        