import os
import pandas as pd

folders = ["localResults", "volumeResults", "bindMountResults"]
columns = ["Bandwidth", "AvgTime", "Type", "NumElements", "Processes"]

def readPart(line):
    parts = line.split(" ")
    results = []
    for i in range(1, len(parts)):
        if len(parts[i])>0:
            results.append(float(parts[i]))
    return results

def readResults():
    for folder in folders:
        files = os.listdir("stream/FTP/Code/Versions/" + folder + "/")
        
        df = pd.DataFrame(columns=columns)
        
        bandwidth = []
        avgTime = []
        typeOfResult = []
        numElements = []
        numProcesses = []
        
        for file in sorted(files):
            if "result_" in file:
                identifiers=file.split(".")[0].split("_")
                data = []
                
                with open("stream/FTP/Code/Versions/" + folder + "/" + file, 'r') as f:
                    for line in f:
                        part = line[:10]
                        if "Copy:" in part:
                            results = readPart(line)
                            bandwidth.append(results[0])
                            avgTime.append(results[1])
                            typeOfResult.append("Copy")
                            numElements.append(str(1000000*int(identifiers[1])))
                            numProcesses.append(str(identifiers[2]))
                        elif "Scale" in part:
                            results = readPart(line)
                            bandwidth.append(results[0])
                            avgTime.append(results[1])
                            typeOfResult.append("Scale")
                            numElements.append(str(1000000*int(identifiers[1])))
                            numProcesses.append(str(identifiers[2]))
                        elif "Add" in part:
                            results = readPart(line)
                            bandwidth.append(results[0])
                            avgTime.append(results[1])
                            typeOfResult.append("Add")
                            numElements.append(str(1000000*int(identifiers[1])))
                            numProcesses.append(str(identifiers[2]))
                        elif "Triad" in part:
                            results = readPart(line)
                            bandwidth.append(results[0])
                            avgTime.append(results[1])
                            typeOfResult.append("Triad")
                            numElements.append(str(1000000*int(identifiers[1])))
                            numProcesses.append(str(identifiers[2]))
        results = [bandwidth, avgTime, typeOfResult, numElements, numProcesses]
        for i in range(len(columns)):
            df[columns[i]] = results[i]
        df.to_csv(folder+".csv")

if __name__=="__main__":
    readResults()