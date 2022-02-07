#!/usr/bin/env bash
echo "ct2mt start!"
echo "Do you want to creat artificial Ellipsoid? (Y/N): "
read flag1
if [ $flag1 = 'Y' ]
then
	python ./artificial_CT.py
	python ./marchingcubes.py
	echo "Do you want to use Karambola for MT-Calculation? (Y/N)"
	read flag2
	if [ $flag2 = 'Y' ]
	then
		echo "Karambola running......"
       		cd ./karambola-NJP/
       		echo "input the polyfilename(mit Nachsilbe):"
       		read polyfilename
       		./karambola -i ../$polyfilename --labels
       		echo "Karambola End......"
		echo "Do you want to calculate the Sim-Precision? (Y/N)"
		read flag3
		if [ $flag3 = 'Y' ]
		then
			cd ..
			python ./auflosung.py
		fi
	fi
else
	python ./marchingcubes.py
	echo "Do you want to use Karambola for MT-Calculation? (Y/N)"
	read flag4
	if [ $flag4 = 'Y' ]
	then
                echo "Karambola running......"
                cd ./karambola-NJP/
                echo "input the polyfilename(mit Nachsilbe):"
                read polyfilename
                ./karambola -i ../$polyfilename --labels
                echo "Karambola End......"
	fi
fi
echo "Programm End......"
