class Solution:
    def shortest_seq_bfs(self, beginWord, endWord, word_dict, queue):
        queue.append((beginWord, 1))
        while queue:
            word, pos = queue.popleft()
            if word == endWord:
                return pos
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    temp = word[:i] + j + word[i+1:]
                    if temp in word_dict:
                        if word_dict[temp] == 0:
                            queue.append((temp, pos+1))
                            word_dict[temp] = 1
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # i'm going to create a dictionary where key is a word and  it's value represents whether it's visited or not 

        word_dict = {}
        for word in wordList:
            word_dict[word] = 0
        # TC = O(NxM)

        if endWord not in word_dict:
            return 0
        
        queue = deque()
        return self.shortest_seq_bfs(beginWord, endWord, word_dict, queue)
        
