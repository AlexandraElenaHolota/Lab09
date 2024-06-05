from database.DB_connect import DBConnect
from model.airlines import Airline
from model.airports import Airport
from model.flights import Flight
from model.rotta import Rotta


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM airports a  """

        cursor.execute(query, )

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllFlights():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM flights f  """

        cursor.execute(query, )

        for row in cursor:
            result.append(Flight(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAirlines():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM airlines a  """

        cursor.execute(query, )

        for row in cursor:
            result.append(Airline(**row))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getAllRotteV1():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT f.ORIGIN_AIRPORT_ID as a1, f.DESTINATION_AIRPORT_ID as a2, SUM(f.DISTANCE) as totDistance, COUNT(*) as nVoli 
                    FROM flights f 
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID"""

        cursor.execute(query)

        for row in cursor:
            result.append(Rotta(**row))

        cursor.close()
        conn.close()
        return result

    def getAllRotteV2():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT T1.ORIGIN_AIRPORT_ID as a1, T1.DESTINATION_AIRPORT_ID as a2, COALESCE(T1.D, 0) + COALESCE(T2.D, 0) as totDistance, COALESCE(T1.N, 0) + COALESCE(T2.N, 0) as nVoli
                    FROM
                    (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                    FROM flights f
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T1
                    LEFT JOIN
                    (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                    FROM flights f
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T2
                    ON T1.ORIGIN_AIRPORT_ID = T2.DESTINATION_AIRPORT_ID AND T2.ORIGIN_AIRPORT_ID = T1.DESTINATION_AIRPORT_ID
                    WHERE T1.ORIGIN_AIRPORT_ID < T2.ORIGIN_AIRPORT_ID OR T2.ORIGIN_AIRPORT_ID IS NULL OR T2.DESTINATION_AIRPORT_ID IS NULL"""

        cursor.execute(query)

        for row in cursor:
            result.append(Rotta(**row))

        cursor.close()
        conn.close()
        return result
