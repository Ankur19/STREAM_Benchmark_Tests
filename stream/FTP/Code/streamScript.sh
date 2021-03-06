#!/bin/bash

#export PATH=/app/mpiccInstall/bin:$PATH

#cd /app/stream/FTP/Code/Versions

echo "Which version?"
echo "[ 1: Local, 2: Volumes, 3: BindMounts ]"
read version

cd Versions

if [ $version -eq 1 ]
then
	export PATH=/app/mpiccInstall/bin:$PATH
	resultPath=$PWD/localResults
	mkdir localResults
else
	export PATH=/app/mpiccInstall/bin:$PATH
	
	if [ $version -eq 2 ]
	then
		resultPath=$PWD/volumeResults
		mkdir volumeResults
	else
		resultPath=$PWD/bindMountResults
		mkdir bindMountResults
	fi
fi

arr=( 1 2 5 10 25 50 100 250 500 )

rank=( 1 2 4 8 )

tries=( 1 2 3 4 5 )

for k in "${tries[@]}"
do
	for i in "${arr[@]}"
	do
		x=$((1000000*i))
		
		mpicc -O -DSTREAM_ARRAY_SIZE="$x" stream_mpi.c -o stream."$i"M
		
		mkdir "$resultPath"/"$k"
		
		for j in "${rank[@]}"
		do
			mpirun -n "$j" ./stream."$i"M >> "$resultPath"/"$k"/result_"$i"_"$j".txt
		done
		
		rm ./stream."$i"M
	done
done
