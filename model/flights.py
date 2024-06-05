from dataclasses import dataclass
from datetime import datetime


@dataclass
class Flight:
    ID: int
    AIRLINE_ID: int
    FLIGHT_NUMBER: int
    TAIL_NUMBER: str
    ORIGIN_AIRPORT_ID: int
    DESTINATION_AIRPORT_ID: int
    SCHEDULED_DEPARTURE_DATE: datetime
    DEPARTURE_DELAY: float
    ELAPSED_TIME: float
    DISTANCE: int
    ARRIVAL_DATE: datetime
    ARRIVAL_DELAY: float

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, value):
        self._ID = value

    @property
    def AIRLINE_ID(self):
        return self._AIRLINE_ID

    @AIRLINE_ID.setter
    def AIRLINE_ID(self, value):
        self._AIRLINE_ID = value

    @property
    def FLIGHT_NUMBER(self):
        return self._FLIGHT_NUMBER

    @FLIGHT_NUMBER.setter
    def FLIGHT_NUMBER(self, value):
        self._FLIGHT_NUMBER = value

    @property
    def TAIL_NUMBER(self):
        return self._TAIL_NUMBER

    @TAIL_NUMBER.setter
    def TAIL_NUMBER(self, value):
        self._TAIL_NUMBER = value

    @property
    def ORIGIN_AIRPORT_ID(self):
        return self._ORIGIN_AIRPORT_ID

    @ORIGIN_AIRPORT_ID.setter
    def ORIGIN_AIRPORT_ID(self, value):
        self._ORIGIN_AIRPORT_ID = value

    @property
    def DESTINATION_AIRPORT_ID(self):
        return self._DESTINATION_AIRPORT_ID

    @DESTINATION_AIRPORT_ID.setter
    def DESTINATION_AIRPORT_ID(self, value):
        self._DESTINATION_AIRPORT_ID = value

    @property
    def SCHEDULED_DEPARTURE_DATE(self):
        return self._SCHEDULED_DEPARTURE_DATE

    @SCHEDULED_DEPARTURE_DATE.setter
    def SCHEDULED_DEPARTURE_DATE(self, value):
        self._SCHEDULED_DEPARTURE_DATE = value

    @property
    def DEPARTURE_DELAY(self):
        return self._DEPARTURE_DELAY

    @DEPARTURE_DELAY.setter
    def DEPARTURE_DELAY(self, value):
        self._DEPARTURE_DELAY = value

    @property
    def ELAPSED_TIME(self):
        return self._ELAPSED_TIME

    @ELAPSED_TIME.setter
    def ELAPSED_TIME(self, value):
        self._ELAPSED_TIME = value

    @property
    def DISTANCE(self):
        return self._DISTANCE

    @DISTANCE.setter
    def DISTANCE(self, value):
        self._DISTANCE = value

    @property
    def ARRIVAL_DATE(self):
        return self._ARRIVAL_DATE

    @ARRIVAL_DATE.setter
    def ARRIVAL_DATE(self, value):
        self._ARRIVAL_DATE = value

    @property
    def ARRIVAL_DELAY(self):
        return self._ARRIVAL_DELAY

    @ARRIVAL_DELAY.setter
    def ARRIVAL_DELAY(self, value):
        self._ARRIVAL_DELAY = value