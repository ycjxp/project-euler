#!python
class CoinCounter:

    def __init__(self, coins):
        self.coins = coins

    def count(self, target):
        return self._count(target, len(self.coins))

    def _count(self, target, maxIndex):
        if target == 0:
            return 1
        if maxIndex == 0 or target < 0:
            return 0
        return self._count(target, maxIndex-1) + \
            self._count(target - self.coins[maxIndex-1], maxIndex)

COINS = [1, 2, 5, 10, 20, 50, 100, 200]

c = CoinCounter(COINS)
print(c.count(200))
