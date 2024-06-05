from dataclasses import dataclass
@dataclass
class Airline:
    ID: int
    IATA_CODE: str
    AIRLINE: str

    @property
    def ID(self):
        return self.ID

    @ID.setter
    def ID(self, value):
        self.ID = value

    @property
    def IATA_CODE(self):
        return self.IATA_CODE

    @IATA_CODE.setter
    def IATA_CODE(self, value):
        self.IATA_CODE = value

    @property
    def AIRLINE(self):
        return self.AIRLINE

    @AIRLINE.setter
    def AIRLINE(self, value):
        self.AIRLINE = value