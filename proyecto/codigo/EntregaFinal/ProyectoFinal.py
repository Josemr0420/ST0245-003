import numpy as np
from numpy import genfromtxt
from matplotlib import pyplot as plt
import time

def getFile(fileName):
    
  with open(fileName) as file:
    text = file.read()
    return text

def getRowsNColumns(text):
    
   nRows = text.split("\n")
   nColumns = nRows[0].split(",")
   
   return len(nRows), len(nColumns)

def getMatrix(text,numberOfRows,numberOfColumns):
  matrix = np.zeros( (numberOfRows-1,numberOfColumns) )
  rows = text.split("\n")
  
  index = 0
  
  for row in rows:
    jIndex = 0
    columns = row.split(",")
    
    for column in columns:
      if column != '':
        matrix[index][jIndex] = int(column)
        jIndex = jIndex + 1
        
    index = index + 1
    
  return matrix

def lossyAlgorithm(matrix,numberOfRows,numberOfColumns):
    print("The image is going to compressed but you are going to loss some pixels...")
    lista = []

    if numberOfRows%2 == 1 and numberOfColumns%2 == 0:
        
        newRows = numberOfRows//2
        newColumns = numberOfColumns//2
        
        matrix2 = np.zeros((newRows,newColumns))
        
        for i in range(numberOfRows-1):
            for j in range(numberOfColumns):
                if j%2 == 0 and i%2 == 0:
                    lista.append(matrix[i][j])
                    
        matrix2 = np.array(lista).reshape(newRows, newColumns)
    
    elif numberOfRows%2 == 0 and numberOfColumns%2 == 1:
        
        newRows = numberOfRows//2
        newColumns = numberOfColumns//2
        
        matrix2 = np.zeros(((newRows),newColumns+1))
        
        for i in range(numberOfRows-1):
            for j in range(numberOfColumns):
                if j%2 == 0 and i%2 == 0:
                    lista.append(matrix[i][j])
                    
        matrix2 = np.array(lista).reshape(newRows, newColumns+1)
    
    elif numberOfRows%2 == 0 and numberOfColumns%2 == 0:
        
        newRows = numberOfRows//2
        newColumns = numberOfColumns//2
        
        matrix2 = np.zeros(((newRows),newColumns))
        
        for i in range(numberOfRows-1):
            for j in range(numberOfColumns):
                if j%2 == 0 and i%2 == 0:
                    lista.append(matrix[i][j])
                    
        matrix2 = np.array(lista).reshape(newRows, newColumns)
    
    else:
        newRows = numberOfRows//2
        newColumns = numberOfColumns//2
        
        matrix2 = np.zeros(((newRows),newColumns+1))
        
        for i in range(numberOfRows-1):
            for j in range(numberOfColumns):
                if j%2 == 0 and i%2 == 0:
                    lista.append(matrix[i][j])
                    
        matrix2 = np.array(lista).reshape(newRows, newColumns+1)
        
    print("The image was compressed and decompressed succesfully.")
    
    return matrix2

def matrixToList(matrix,numberOfRows, numberOfColumns):
    
    newRowsForList = numberOfRows
    newColumnsForList = numberOfColumns
    
    list = []
    
    for i in range(newRowsForList-1):
        for j in range(newColumnsForList):
            list.append(matrix[i][j])
            
    return list

def losslessCompressionAlgorithm(list):
    
    print("Compressing the image...")
    
    cont = 0
    i = 0
    listLossless = []
    
    while i < len(list):
        
        cont += 1
        target = findTarget(list, i)
        
        if target:
            targetDistance, targetLength = target
            difference = min(i+targetLength, len(list)-1)
            listLossless.append('<' + str(targetDistance) + ',' + str(targetLength) + ',' + str(list[difference]) + '>')
            i = i + (targetLength+1)
            
        else:
            listLossless.append('<0,0,'+str(list[i]) + '>')
            i = i + 1
            
    print("Image compressed succesfully.")
    
    return listLossless

def findTarget(list,i):
    
    looked = 15
    looking = 15
    
    buffer = min(i+looking, len(list) + 1)
    
    targetDistance = -1 
    targetLength = -1
    
    for j in range(i,buffer):
        
        start = max(0, i - looked)
        list1 = list[i: j+1]
        
        for k in range(start, i):
            times =  len(list1)//(i-k)
            last = len(list1)%(i-k)
            
            targetList = list[k:i] * times + list[k:k+last]
            
            if targetList == list1 and len(list1) == targetLength:
                targetDistance = i - k
                targetLength = len(list1)

    if targetDistance > 0 and targetLength > 0:
        return targetList, targetLength
    else:
        return None
          
def losslessDecompressionAlgorithm(compList):
    print("Decompressing the image...")
    
    decoList = []
    index1 = 0
    
    while index1 < len(compList):
        unzip = compList[index1]
        frst = unzip.index(',')
        scd = unzip.index(',', frst + 1)
        
        if compList[index1][1:frst] == '0':
            decoList.append(compList[index1][scd+1:unzip.index('>')])
            index1 = index1 + 1
            
        else:
            if compList[index1][frst+1:scd] == '1':
                number = decoList[-(int(compList[index1][1:frst]))]
                decoList.append(number)
                decoList.append(compList[index1][scd+1:unzip.index('>')])
                index1 = index1 + 1
                
            else:
                listA2 = []
                other = -(int(compList[index1][1:frst]))
                otherOne = int(compList[index1][frst+1:scd])
                
                if abs(other) > otherOne:
                    while otherOne > 0:
                        listA2.append(decoList[other])
                        other = other + 1
                        otherOne = otherOne - 1
                        
                    for item in listA2:
                        decoList.append(item)
                        
                    decoList.append(compList[index1][scd+1:unzip.index('>')])
                    index1 = index1 + 1
                    
                else:
                    save = otherOne - int(compList[index1][1:frst])
                    otherOne = int(compList[index1][1:frst])
                    
                    while otherOne > 0:
                        listA2.append(decoList[other])
                        other = other + 1
                        otherOne = otherOne - 1
                        
                    for item in listA2:
                        decoList.append(item)
                        
                    while save > 0:
                        decoList.append(decoList[-1])
                        save = save - 1
                        
                    decoList.append(compList[index1][scd+1:unzip.index('>')])
                    index1 = index1 + 1
                    
    print("Image Decompressed.")
    
    return decoList

def printImage(nameFile):
    print("Showing the image...")
    
    nameFile1 = nameFile
    nameFile1 = genfromtxt(nameFile1, delimiter = ",")
    
    plt.imshow(nameFile1, cmap = "gray")
    plt.show()
    
    print("The show is done.")

def stringToFloatList(list):
    floatList = []
    
    for item in list:
        floatList.append(float(item))

    return floatList

def floatToIntList(list):
    integerList = []
    
    for i in list:
        integer = int(i)
        integerList.append(integer)
        
    return integerList

def main():
    print("-"*28,"THE PROGRAM IS STARTING","-"*28, "\n")
    startTheTimer = time.time()
    
    # nameFile = "_56caf73c-2d5d-11e7-a28f-c563b2540923.csv"
    nameFile = "0.csv"
    text = getFile(nameFile)
    
    numberOfRows, numberOfColumns = getRowsNColumns(text)
    matrix = getMatrix(text, numberOfRows, numberOfColumns)
    
    matrix2 = lossyAlgorithm(matrix, numberOfRows, numberOfColumns)
    
    np.savetxt("lossyAlgorithm.csv",matrix2.astype(int), fmt='%i', delimiter = ",")
    nameFile2 = "lossyAlgorithm.csv"
    losslyTime = time.time()
    timeOfExecutionLooslyAlgoritm = losslyTime - startTheTimer
    print("\nTime of the Lossly Algorithm (Nearest neighbor): ", timeOfExecutionLooslyAlgoritm, "secs\n")
   
    print("-"*83,"\n")
    
    printImage(nameFile)
    printImage(nameFile2)
    timeOfFinishingCreationImage = time.time()
    timeOfExecutionCreationImage = timeOfFinishingCreationImage - losslyTime
    print("\nTime during the ploting of the images: ", timeOfExecutionCreationImage, "secs\n")
   
    print("-"*83,"\n")
    
    list = matrixToList(matrix,numberOfRows, numberOfColumns)
    compressedList = losslessCompressionAlgorithm(list)
    timeOfCompressionAlgorithm = time.time()
    timeOfFinishedCompressionAlgorithm = timeOfCompressionAlgorithm - timeOfFinishingCreationImage
    print("\nTime of the lossless compression algorithm (LZ77): ",timeOfFinishedCompressionAlgorithm, "secs\n")
    
    print("-"*83,"\n")
    
    timeOfInitializationDecompressionAlgorithm = time.time()
    decompressingList = losslessDecompressionAlgorithm(compressedList)
    floatList = stringToFloatList(decompressingList)
    integerList = floatToIntList(floatList)
    timeOfFinalizationDecompressionAlgorithm = time.time()
    timeOfFinishedDecompressionAlgorithm = timeOfFinalizationDecompressionAlgorithm - timeOfInitializationDecompressionAlgorithm
    print("\nTime of the lossless decompression algorithm (LZ77): ", timeOfFinishedDecompressionAlgorithm, "secs\n")
    
    
    nameFile3 = open("lossLessDecompresingFile.csv", 'w')
    for j in range(len(integerList)):
        nameFile3.write(str(integerList[j])+',')
    nameFile3.close()
    
    finishedTimer = time.time()
    
    totalTimeOfExecution = finishedTimer - startTheTimer
    print("-"*83,"\n")
    print("TOTAL TIME OF EXECUTION (NEAREST NEIGHBOR AND LZ77): ", totalTimeOfExecution - timeOfExecutionCreationImage, "secs\n")
    printImage(nameFile)
    print("-"*31,"THE PROGRAM FINISHED","-"*31, "\n")
    
main()