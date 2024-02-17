from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        # Create a hashmap to keep track of the freq
        self.tracker = defaultdict(int)
        self.freq_tracker = defaultdict(int)  # Keep track of the freq

    def add(self, number: int) -> None:
        freq = self.tracker.get(number, 0) + 1
        self.tracker[number] = freq  # Update the freq of the number
        self.freq_tracker[freq] = self.freq_tracker.get(freq, 0) + 1

    # If the number is in the Tracker and has a freq sub 1 if not del
    def deleteOne(self, number: int) -> None:
        freq = self.tracker[number]

        if self.tracker[number]:
            self.tracker[number] = freq - 1
            self.freq_tracker[freq] -= 1
        else:
            del self.tracker[number]
            del self.freq_tracker[freq]

    # If the freq is one of the values from the hash return True
    def hasFrequency(self, frequency: int) -> bool:
        print(self.tracker)
        print(self.freq_tracker)
        return True if self.freq_tracker[frequency] else False


# Your FrequencyTracker object will be instantiated and called as such:
obj = FrequencyTracker()
obj.add(1)
obj.add(1)
obj.add(1)
obj.add(1)
obj.add(2)
obj.add(2)
obj.add(2)
obj.add(3)
obj.deleteOne(1)
obj.deleteOne(1)
param_3 = obj.hasFrequency(5)
print(param_3)
