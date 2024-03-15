class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0

        for i in range(len(batteryPercentages)):
            if (batteryPercentages[i] > 0):
                tested += 1
                self.decrease(i, batteryPercentages)

        return tested

    def decrease(self, index, batteryPercentages):
        for i in range(index, len(batteryPercentages)):
            if (batteryPercentages[i] > 0):
                batteryPercentages[i] -= 1

        return batteryPercentages


        
