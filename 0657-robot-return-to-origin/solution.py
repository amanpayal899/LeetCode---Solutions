class Solution:
    def judgeCircle(self, moves: str) -> bool:
      right=0
      up=0
      for i in moves:
        if i == 'U':
            up += 1
        elif i == 'D':
            up -= 1
        elif i == 'L':
            right -= 1
        else:
            right += 1
      if right == 0 and up == 0:
        return True
      return False
