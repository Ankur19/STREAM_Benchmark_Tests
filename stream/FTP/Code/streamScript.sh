#!/bin/bash

#export PATH=/app/mpiccInstall/bin:$PATH

#cd /app/stream/FTP/Code/Versions

echo "Which version?"
echo "[ 1: Local, 2: Volumes, 3: BindMounts ]"
read version

if [ $version -eq 1 ]
then
	cd ~/Downloads/stream/FTP/Code/Versions
else
	cd /app/stream/FTP/Code/Versions
	export PATH=/app/mpiccInstall/bin:$PATH

mkdir results

arr=( 1 2 5 10 25 50 100 250 500 )

rank=( 1 2 3 4 )

for i in "${arr[@]}"
do
	x=$((1000000*i))
	
	mpicc -O -DSTREAM_ARRAY_SIZE="$x" stream_mpi.c -o stream."$i"M
	
	for j in "${rank[@]}"
	do
		mpirun -n "$j" ./stream."$i"M >> $PWD/results/result_"$i"_"$j".txt
	done
	
done