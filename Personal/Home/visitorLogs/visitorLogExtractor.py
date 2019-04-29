import os
import sqlite3
import json

VISITOR_DATA_DIR = os.path.dirname(os.path.abspath(__file__))
HOME_DIR = os.path.dirname(VISITOR_DATA_DIR)
BASE_DIR = os.path.dirname(HOME_DIR)

class visitorLogExtractor:

    def __init__(self):
        self.pathToDB = os.path.join(BASE_DIR, 'db.sqlite3')
        print(self.pathToDB)

    def connectToDatabase(self):
        try:
            dbConnection = sqlite3.connect(self.pathToDB)
            return dbConnection
        except Exception as e:
            print(e)
            return None

    def closeDatabase(self, dbConnection):
        try:
            dbConnection.close()
        except Exception as e:
            print(e)
            return 

    def executeTransaction(self, dbConnection, queryStatement):
        try:
            dbCursor = dbConnection.cursor()
            dbCursor.execute(queryStatement)
            returnedData = dbCursor.fetchall()
            return returnedData
        except Exception as e:
            print(e)
            return 

    def commitTransaction(self, dbConnection):
        try:
            dbConnection.commit()
        except Exception as e:
            print(e)
            return

    def selectAllStatement(self):
        selectAllStatement = "SELECT * FROM visitorLogs"
        return selectAllStatement

    def selectAllVisitorsFromDatabase(self, dbConnection):
        visitors = self.executeTransaction(dbConnection, self.selectAllStatement())
        print(visitors)
        return visitors

    def convertVisitorDataToJSON(self, visitorData):
        jsonData = json.dumps(visitorData)
        return jsonData

def returnVisitorDataFromDatabase():
    logextractor = visitorLogExtractor()
    dbConnection = logextractor.connectToDatabase()
    visitors = logextractor.selectAllVisitorsFromDatabase(dbConnection)
    logextractor.closeDatabase(dbConnection)
    jsonFormattedData = logextractor.convertVisitorDataToJSON(visitors)
    return jsonFormattedData



