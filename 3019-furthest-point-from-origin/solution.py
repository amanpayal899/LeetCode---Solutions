class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        _count = 0
        right_count = 0
        left_count = 0
        for i in moves:
            if i == 'R':
                right_count += 1
            elif i == 'L':
                left_count += 1
            else:
                _count += 1
        if right_count > left_count:
            return right_count + _count - left_count
        return left_count + _count -right_count
