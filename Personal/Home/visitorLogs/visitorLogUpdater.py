import os
import sys
import time

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

from logAcquirer import copyAccessLogsFromVarDirectoryToCopiedLogsDirectory as logUpdateStepOne
from logPreparer import unzipNecessaryFilesAndMigrateAllFilesToPreparedLogsDirectory as logUpdateStepTwo
from logCompiler import combineAllAccessLogsIntoSingleLogInCompiledLogsDirectory as logUpdateStepThree
from logExaminer import requestAdditionalDataAboutVisitorIPAdressesAndWriteToVisitorDataDirectory as logUpdateStepFour
from visitorLogInjector import insertFormattedJSONIntoSQLITEDatabase as logUpdateStepFive

class visitorLogUpdater:

    def __init__(self):
        pass

    def updateAccessLogs(self):
        # if sys.platform == 'linux':
        logUpdateStepOne()
        time.sleep(5)
        logUpdateStepTwo()
        time.sleep(5)
        logUpdateStepThree()
        time.sleep(5)
        logUpdateStepFour()
        time.sleep(5)
        logUpdateStepFive()
        # else:
        #     failedToUpdateMessage = f'Unable to process certain commands on {sys.platform}. Needs to be ran on a Linux machine...'
        #     print(failedToUpdateMessage)
        #     return failedToUpdateMessage

def main():
    logupdater = visitorLogUpdater()
    logupdater.updateAccessLogs()

def updateAccessLogs():
    logupdater = visitorLogUpdater()
    return logupdater.updateAccessLogs()

if __name__ == '__main__':
    main()
