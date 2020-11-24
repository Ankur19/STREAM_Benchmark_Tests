import os
import pandas as pd

array=[1,2,5,10,25,50,100,250,500]
rank=[1,2,4,8]
folders=["1","2","3","4","5"]

def createColumns():
    result = []
    for i in array:
        for j in rank:
            result.append(str(i)+"_"+str(j))
    return result


def readResults():
	for fold in folders:
	    files = os.listdir(os.getcwd() + "/" + fold)
	    columns = createColumns()
	    df = pd.DataFrame(columns=columns)
	    for file in sorted(files):
	        if "result_" in file:
	            identifiers=file.split(".")[0].split("_")
	            data = []
	            with open(os.getcwd() + "/" + fold + "/" + file, 'r') as f:
	                for line in f:
	                    part = line[:10]
	                    if "Copy:" in part or "Scale:" in part or "Add:" in part or "Triad:" in part:
	                        parts = line.split(" ")
	                        for i in range(1, len(parts)):
	                            if len(parts[i])>0:
	                                data.append(float(parts[i]))
	                                break
	            df[identifiers[1]+"_"+identifiers[2]] = data
	    df.to_csv("results_" + fold +".csv")

def averageResults():
	frames = []
	for fold in folders:
		df = pd.read_csv("results_" + fold +".csv")
		frames.append(df)
	df = pd.concat(frames).groupby(level=0).mean()
	df.to_csv("results.csv")

if __name__=="__main__":
    readResults()
    averageResults()