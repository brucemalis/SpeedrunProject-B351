import os

def makeGen(genNumber):
    """Creates a new generation"""
    pass

def readRun(genNumber,runNumber):
    """Reads a given run number from a given generation, and returns a list of strings (the input strings)"""
    pass
  
def writeRun(genNumber,runNumber,inputList):
    """Writes a given run number to a given generation, based on the passed list of strings (the inputs)"""
    pass

def readResult(genNumber,runNumber):
    """Reads a given result number from a given generation, and returns a list where index 0 is the maximum X, and index 1 is the frame"""
    # Find and open the results folder
    dir = os.path.dirname(__file__)
    resultsPath = os.path.join(dir, "../Output/gen" + str(genNumber) + "/Results/")
    
    #Build the path to the requested file
    fileName = resultsPath + "result" + str(runNumber) + ".txt"
    
    # Open the file, and read it to a string, then close the file
    resultFile = open(fileName, 'r')
    resultString = resultFile.readline()
    resultFile.close()
    
    # Split the string into a list, and turn the strings to ints
    resultList = resultString.split(',')
    resultList = map(int, resultList)
    
    # Return the list of ints
    return resultList

def getConfig():
    """Returns the settings of the configuration file as a list"""
    # Temporary hack...
    return [100,1,0]

def getRunsPerGen():
    return getConfig()[0]