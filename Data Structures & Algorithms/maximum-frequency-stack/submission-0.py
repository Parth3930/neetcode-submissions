class FreqStack:

    def __init__(self):
        self.count = {} 
        self.groups = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:

        self.count[val] = self.count.get(val, 0) + 1
        freq = self.count[val]

        self.maxFreq = max(self.maxFreq, freq)

        if freq not in self.groups:
            self.groups[freq] = []

        self.groups[freq].append(val)

    def pop(self) -> int:

        val = self.groups[self.maxFreq].pop()

        self.count[val] -= 1

        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1

        return val