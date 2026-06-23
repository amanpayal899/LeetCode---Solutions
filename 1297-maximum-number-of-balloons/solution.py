class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        my_dict = {'b' : 0, 'a' : 0, 'l' : 0, 'o' : 0, 'n' : 0}
        for chr in text:
            if chr == 'b' or chr == 'a' or chr == 'l' or chr == 'o' or chr=='n':
                my_dict[chr] += 1
        return min(my_dict['a'], my_dict['b'], my_dict['l']//2, my_dict['o']//2, my_dict['n'])
