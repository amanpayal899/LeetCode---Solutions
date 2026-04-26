class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        j=0
        for i in range (1,n+1):
            if i == target[j]:
                j+=1
                s.append("Push")
            else:
                s.append("Push")
                s.append("Pop")
            if j == len(target):
                break

        return s
