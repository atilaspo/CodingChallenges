class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        min_res = R
        
        while L <= R:
            K = (L + R) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(float(pile) / K)
            if total_hours <= h:
                min_res = K
                R = K - 1
            else:
                L = K + 1
        return min_res 