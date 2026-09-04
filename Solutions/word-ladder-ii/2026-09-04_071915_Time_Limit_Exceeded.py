# Problem: Word Ladder II
# Status: Time Limit Exceeded
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-09-04_071915 UTC
# URL: https://leetcode.com/submissions/detail/2130425685/

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
            word_set.remove(beginWord)
        p_level = 1
        temp_stack = []
        
        while queue:

            word_seq, curr_level = queue.popleft()
            if p_level != curr_level:
                while temp_stack:
                    w = temp_stack.pop()
                    if w in word_set:
                        word_set.remove(w)
                p_level = curr_level
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
                            
                            temp_word_seq = word_seq + [new_word]
                            temp_stack.append(new_word)
                            queue.append((temp_word_seq, curr_level+1) )
                
                            
        return result

            
        