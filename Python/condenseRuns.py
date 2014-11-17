import os

def condenseRuns(genNumber):
    """Turns a directory full of runs into one .csv file"""
    allResults = ["Run Number, Maximum X, Frame Reached\n"]
    
    # Find and open the results
    dir = os.path.dirname(__file__)
    resultsPath = os.path.join(dir, "../Output/gen" + str(genNumber) + "/Results/")
    
    for fileNum, filename in enumerate(os.listdir(resultsPath)):            # Iterate
        resultFile = open(resultsPath + filename, 'r')                      # Open the file
        allResults.append(str(fileNum) + ',' + resultFile.readline()+'\n')  # Add the result to our list
        resultFile.close()                                                  # Close the file
    
    outputFile = open(resultsPath + "../allResults.csv", 'w')  # Create a .csv
    outputFile.writelines(allResults)                          # Write the results
    outputFile.close()                                         # Close the file
    
    allResults.pop(0)   # Remove the headers before we return
    return allResults

def getBestRuns(genNumber,numberOfRuns):
    """Returns a list of integers representing the top numberOfRuns runs from the given generation"""
    pass


if __name__ == '__main__':
    condenseRuns(0)
