import os 
import sys 
import json
import sqlite3

# Here we will grab the visitor data JSON from several directories up
# The class takes the logs from 

VISITOR_LOG_ANALYSIS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
HOME_DIR = os.path.dirname(VISITOR_LOG_ANALYSIS_DIR)
BASE_DIR = os.path.dirname(HOME_DIR)
INNER_PERSONAL_DIR = os.path.dirname(BASE_DIR)
OUTER_PERSONAL_DIR = os.path.dirname(INNER_PERSONAL_DIR)
OPT_DIR = os.path.dirname(OUTER_PERSONAL_DIR)
LOG_ANALYSIS_DIR = os.path.join(OPT_DIR, 'LogAnalysis')

sys.path.append(LOG_ANALYSIS_DIR)
sys.path.append(INNER_PERSONAL_DIR)

VISITOR_DATA_DIR = os.path.join(LOG_ANALYSIS_DIR, 'visitorData')
PATH_TO_SQLITE_DB = os.path.join(BASE_DIR, 'db.sqlite3')

class visitorLogInjector:

    def __init__(self):
        self.visitorDataFile = ""

    def updateInitializedVariables(self):
        self.visitorDataFile = os.path.join(VISITOR_DATA_DIR, 'visitorData.json')

    def readInVisitorDataToMemory(self):
        print("Reading entries into memory as a list...")
        
        listOfAllEntries = []

        with open(self.visitorDataFile, encoding='utf-8') as visitorDataFile:
            jsonFile = json.loads(visitorDataFile.read())

            for entry in jsonFile:
                if entry is not None:
                    listOfAllEntries.append(entry)

        return listOfAllEntries

    def insertEntriesIntoDatabase(self, jsonFormattedVisitorEntries):

        dbConnection = self.openConnectionToDatabase()
        self.createTableInDatabase(dbConnection)

        thisEntry = []

        for entry in jsonFormattedVisitorEntries:
            visitorsIP = entry[0]["visitorsIP"]
            visitorsContinent = entry[1]["visitorsContinent"]
            visitorsCountry = entry[2]["visitorsCountry"]
            visitorsRegionCode = entry[3]["visitorsRegionCode"]
            visitorsRegionName = entry[4]["visitorsRegionName"]
            visitorsCity = entry[5]["visitorsCity"]
            visitorsZipCode = entry[6]["visitorsZipCode"]
            visitorsLongitude = entry[7]["visitorsLongitude"]
            visitorsLatitude = entry[8]["visitorsLatitude"]

            thisEntry = [
                visitorsIP, 
                visitorsContinent, 
                visitorsCountry,
                visitorsRegionCode, 
                visitorsRegionName, 
                visitorsCity, 
                visitorsZipCode, 
                visitorsLongitude, 
                visitorsLatitude
            ]

            self.insertEntryIntoDatabase(thisEntry, dbConnection)
        
        self.commitTransaction(dbConnection)
        self.closeConnectionToDatabase(dbConnection)

    def openConnectionToDatabase(self):
        try:
            dbConnection = sqlite3.connect(PATH_TO_SQLITE_DB)
            if dbConnection is not None:
                return dbConnection
        except Exception as e:
            print(e)
            return None

    def closeConnectionToDatabase(self, dbConnection):
        try: 
            dbConnection.close()
        except Exception as e:
            print(e)
            return

    def executeTransaction(self, dbConnection, transaction):
        dbCursor = dbConnection.cursor()
        try:
            dbCursor.execute(transaction)
        except Exception as e:
            print(e)
            return 

    def commitTransaction(self, dbConnection):
        try: 
            dbConnection.commit()
        except Exception as e:
            print(e)
            return 

    def createTableInDatabase(self, dbConnection):
        
        createTableString = '''
        CREATE TABLE IF NOT EXISTS visitorLogs (
            visitorsIPAdress VARCHAR (255) PRIMARY KEY,
            visitorsContinent VARCHAR (255) NOT NULL,
            visitorsCountry VARCHAR (255), 
            visitorsRegionCode VARCHAR (255), 
            visitorsRegionName VARCHAR (255), 
            visitorsCity VARCHAR (255), 
            visitorsZipCode VARCHAR (255), 
            visitorsLongitude REAL, 
            visitorsLatitude REAL
        ) 
        '''
        print("Creating visitorLogs table in SQLite Database...")
        self.executeTransaction(dbConnection, createTableString)
        self.commitTransaction(dbConnection)

    def insertEntryIntoDatabase(self, visitorEntry, dbConnection):
        
        thisInsertionStatement = self.createEntryInsertionString(visitorEntry)

        print(f"Inserting data for IP address {visitorEntry[0]} into visitorLogs table...")
        self.executeTransaction(dbConnection, thisInsertionStatement)

    def createEntryInsertionString(self, visitorEntryAsList):

        lastIndexInList = len(visitorEntryAsList) -1 

        sqlInsertStatement = ""
        sqlInsertStatement += "INSERT INTO visitorLogs"
        sqlInsertStatement += "( visitorsIPAdress, visitorsContinent, visitorsCountry, visitorsRegionCode, visitorsRegionName, visitorsCity, visitorsZipCode, visitorsLongitude, visitorsLatitude )"
        sqlInsertStatement += " VALUES ("

        for index, field in enumerate(visitorEntryAsList):

            if index != lastIndexInList:
                if isinstance(field, int):
                    sqlInsertStatement += str(field) + ","
                elif isinstance(field, float):
                    sqlInsertStatement += str(field) + ","
                elif isinstance(field, str):
                    sqlInsertStatement += repr(field) + ","
                elif field is None:
                    sqlInsertStatement += "'" + str(field) + "',"
            else:
                if isinstance(field, int):
                    sqlInsertStatement += str(field) 
                elif isinstance(field, float):
                    sqlInsertStatement += str(field)
                elif isinstance(field, str):
                    sqlInsertStatement += repr(field) 
                elif field is None:
                    sqlInsertStatement += "'" + str(field) + "'"

        sqlInsertStatement += " )"

        return sqlInsertStatement

def main():
    loganalyzer = visitorLogInjector()
    loganalyzer.updateInitializedVariables()
    visitorEntries = loganalyzer.readInVisitorDataToMemory()
    loganalyzer.insertEntriesIntoDatabase(visitorEntries)

def insertFormattedJSONIntoSQLITEDatabase():
    loganalyzer = visitorLogInjector()
    loganalyzer.updateInitializedVariables()
    visitorEntries = loganalyzer.readInVisitorDataToMemory()
    loganalyzer.insertEntriesIntoDatabase(visitorEntries)

main()

