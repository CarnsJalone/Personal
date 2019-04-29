import os
import sys
import time
import logging 

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
STATUS_LOG_TEXT = os.path.join(VISITOR_LOG_ANALYSIS_DIR, 'statusLog.txt')

from logAcquirer import copyAccessLogsFromVarDirectoryToCopiedLogsDirectory as logUpdateStepOne
from logPreparer import unzipNecessaryFilesAndMigrateAllFilesToPreparedLogsDirectory as logUpdateStepTwo
from logCompiler import combineAllAccessLogsIntoSingleLogInCompiledLogsDirectory as logUpdateStepThree
from logExaminer import requestAdditionalDataAboutVisitorIPAdressesAndWriteToVisitorDataDirectory as logUpdateStepFour
from visitorLogInjector import insertFormattedJSONIntoSQLITEDatabase as logUpdateStepFive

logging.basicConfig(level=logging.DEBUG, filename=STATUS_LOG_TEXT)

class visitorLogUpdater:

    def __init__(self):
        self.accessLogTXT = ""

    def updateInitializedVariables(self):
        self.accessLogTXT = STATUS_LOG_TEXT

    def deleteAccessLogToBeginProcessing(self):
        if os.path.isfile(self.accessLogTXT):
            os.remove(self.accessLogTXT)

    def updateAccessLogs(self):
        if sys.platform == 'linux':
            
            # Step One
            now = time.time()
            print("Step One Beginning...")
            logging.info("Step One Beginning...")
            logUpdateStepOne()
            print(f"Step One Successfully Completed. Took {time.time() - now} to Complete...")
            logging.info(f"Step One Successfully Completed. Took {time.time() - now} to Complete...")

            # Step Two
            now = time.time()
            print("Step Two Beginning...")
            logging.info("Step Two Beginning...")
            logUpdateStepTwo()
            print(f"Step Two Successfully Completed. Took {time.time() - now} to Complete...")
            logging.info(f"Step Two Successfully Completed. Took {time.time() - now} to Complete...")

            # Step Three
            now = time.time()
            print("Step Three Beginning...")
            logging.info("Step Three Beginning...")
            logUpdateStepThree()
            print(f"Step Three Successfully Completed. Took {time.time() - now} to Complete...")
            logging.info(f"Step Three Successfully Completed. Took {time.time() - now} to Complete...")


            now = time.time()
            print("Step Four Beginning...")
            logging.info("Step Four Beginning...")
            logUpdateStepFour()
            print(f"Step Four Successfully Completed. Took {time.time() - now} to Complete...")
            logging.info(f"Step Four Successfully Completed. Took {time.time() - now} to Complete...")


            now = time.time()
            print("Step Five Beginning Beginning...")
            logging.info("Step Five Beginning...")
            logUpdateStepFive()
            print(f"Step Five Successfully Completed. Took {time.time() - now} to Complete...")
            logging.info(f"Step Five Successfully Completed. Took {time.time() - now} to Complete...")

        else:
            failedToUpdateMessage = f'Unable To Process Certain On Elements On {sys.platform}. This Functionality Is Based On A Linux Machine...'
            logging.debug(failedToUpdateMessage)
            return failedToUpdateMessage

def main():
    logupdater = visitorLogUpdater()
    logupdater.updateInitializedVariables()
    logupdater.deleteAccessLogToBeginProcessing()
    logupdater.updateAccessLogs()

def updateAccessLogs():
    logupdater = visitorLogUpdater()
    logupdater.updateInitializedVariables()
    logupdater.deleteAccessLogToBeginProcessing()
    logupdater.updateAccessLogs()

if __name__ == '__main__':
    main()
