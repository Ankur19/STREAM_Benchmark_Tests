import os
import pandas as pd

folders = ["localResults", "volumeResults", "bindMountResults"]
columns = ["Bandwidth", "AvgTime", "Type", "NumElements", "Processes"]
times = ["1", "2", "3", "4", "5"]

def readPart(line):
	parts = line.split(" ")
	results = []
	for i in range(1, len(parts)):
		if len(parts[i])>0:
			results.append(float(parts[i]))
	return results

def readResults():
	for folder in folders:
		res = []
		for t in times:
			files = os.listdir("stream/FTP/Code/Versions/" + folder + "/" + t + "/")
			
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
					
					with open("stream/FTP/Code/Versions/" + folder + "/" + t + "/" + file, 'r') as f:
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
			res.append([bandwidth, avgTime, typeOfResult, numElements, numProcesses])
		print(res)
		for i in [0, 1]:
			for k in range(len(res[0][i])):
				for j in range(1, 5):
					res[0][i][k]+=res[j][i][k]
				res[0][i][k]/=5
		for i in range(len(columns)):
			df[columns[i]] = res[0][i]
		df.to_csv(folder+".csv")

if __name__=="__main__":
	readResults()
