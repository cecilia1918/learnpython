#!/usr/bin/env python3

# declare constants as we need them
OK = "OK"
ERR = "ERR"

# import modules here
import sys

# function definitions

def getData(myParam):
    """
    function to retrieve data needed
    :param myParam: function parameter
    :return: data structure, or OK/ERR
    """
    print("function getData")
    return OK

def processData(myData):
    """
    process data retrieved by getData
    :param myData: input data set from getData
    :return: processedData, or ERR
    """
    print("function processData")
    # no real functionality, just return input data for now
    processedData = myData
    if len(processedData) == 0:
        return ERR
    else:
        return processedData
    
def writeData(outData):
    """
    write processed data to somewhere
    :param outData: data to write out
    :return: OK or ERR
    """
    print("function writeData")
    print(outData)
    return OK
    
# main function - note pattern below, use this where possible so your code can be re-used asd a module


def main():
    """
    main function
    :return: OK or ERR
    """
    myParam = "aDummyValue"
    myData = getData(myParam)
    if myData == ERR:
        return ERR
    procData = processData(myData)
    if procData == ERR:
        return ERR
    writeResult = writeData(procData)
    if writeResult == ERR:
        return ERR
    else:
        return OK
    
# remember the construct below
if __name__ == "__main__":
    scriptResult = main()
    print(scriptResult)
    if scriptResult == OK:
        sys.exit(0)
    else:
        sys.exit(1)
    

            
