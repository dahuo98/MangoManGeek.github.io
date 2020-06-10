class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = 0  # amount of gas needed to traval from 0th gas station to current starting point
        curr = 0  # how much gas is left if we start from current starting point
        start = 0 # current starting point
        
        for i in range(len(gas)):
            curr = curr + gas[i] - cost[i]
            if curr < 0:
                diff += curr
                start = i+1
                curr = 0
        
        return start if curr + diff >= 0 else -1