# Problem: Word Ladder
# Status: Time Limit Exceeded
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-30_152447 UTC
# URL: https://leetcode.com/submissions/detail/2125180969/

from collections import deque

class Solution:
    
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def find_row(word, wordList):
            n = len(wordList)
            m = len(wordList[0]) 
            for i in range(n):
                flag = 0
                for j in range(m):
                    if wordList[i][j] == word[j]:
                        continue
                    else:
                        flag = 1
                        break
                if flag == 0:
                    return i
            return -1  # returning -1 if the word is not in wordList

        def shortest_seq_dfs(beginWord, endWord, wordList, visited, my_queue):
            my_queue.append((beginWord, 1))
            r = find_row(beginWord, wordList)
            if r != -1:
                visited[r] = 1
            while my_queue:
                curr_word, curr_moves = my_queue.popleft()
                if curr_word == endWord:
                    return curr_moves
                for i in  range(len(curr_word)):
                    temp_word = copy.copy(curr_word)
                    for j in range(97, 123):
                        j = chr(j)
                        temp_word = temp_word[:i] + str(j) + temp_word[i+1:]
                        r = find_row(temp_word, wordList)
                        if r!=-1 and visited[r] == 0:
                            visited[r] = 1
                            my_queue.append((temp_word, curr_moves+1))
            return 0
        
        my_queue = deque()
        visited = [0]*len(wordList)

        moves = shortest_seq_dfs(beginWord, endWord, wordList, visited, my_queue)
        return moves


