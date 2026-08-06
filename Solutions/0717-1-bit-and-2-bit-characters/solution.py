class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        c=0
        while c<len(bits)-1:
            if bits[c]==1:
                c+=1
            c+=1
        if c==len(bits):
            return False
        return True
        
