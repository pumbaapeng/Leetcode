class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        min_idx = -1
        min_level = float('inf')
        cur_level = 0
        for i in range(n):
            cur_level += (gas[i] - cost[i])
            if cur_level < min_level:
                min_level = cur_level
                min_idx = i
        if cur_level < 0:
            return -1
        return (min_idx + 1) % n
