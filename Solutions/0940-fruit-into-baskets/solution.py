class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        p1 = 0
        p2 = 0
        p3 = 0
        f1 = 0
        n = len(fruits)
        while p3 < n:
            while p2 < n-1 and fruits[p1] == fruits[p2]:
                p2 += 1
            p3 = p2 + 1
            
            while p3 < n and (fruits[p3] == fruits[p1] or fruits[p3] == fruits[p2]):
                if fruits[p3] == fruits[p1]:
                    f1 = p3
                p3 += 1
            max_fruits = max(max_fruits, p3-p1)
            if p3 > n-1:
                return max_fruits
            p1 = p3-1
            while fruits[p1] == fruits[p3-1]:
                p1 -= 1
            p1 += 1
            p2 = p3

        return max_fruits



