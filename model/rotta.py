from dataclasses import dataclass

from model import airports


@dataclass
class Rotta:
    a1: airports.Airport
    a2: airports.Airport
    totDistance: float
    nVoli: int

    def __post_init__(self):
        self.avgDistance = float(self.totDistance / self.nVoli)

    @property
    def a1(self):
        return self._a1

    @a1.setter
    def a1(self, value):
        self._a1 = value

    @property
    def a2(self):
        return self._a2

    @a2.setter
    def a2(self, value):
        self._a2 = value

    @property
    def totDistance(self):
        return self._totDistance

    @totDistance.setter
    def totDistance(self, value):
        self._totDistance = value

    @property
    def nVoli(self):
        return self._nVoli

    @nVoli.setter
    def nVoli(self, value):
        self._nVoli = value

    @property
    def avgDistance(self):
        return self._avgDistance

    @avgDistance.setter
    def avgDistance(self, value):
        self._avgDistance = value