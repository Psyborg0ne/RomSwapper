import rom
import fun
import csv

def loadRom(funcade, rom, status):
	#Creating the script file and writing the code + selected rom
	print("Creating autostart.sh file...")
	fileOperation = open('autostart.sh', 'w+')
	print("Writing to file...")
	fileOperation.write('/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ mame-libretro ~/RetroPie/roms/mame-libretro/' + rom.romName + '.zip\nemulationstation #auto')
	fileOperation.close()
	print("File ok! Trying to push...")
	funcade.swapRom(status, rom)

def initRoms(romList):
	#Reading the csv file to get the rom list (Rom name,Displayed name) with "," delimiter
	with open('romlist.csv') as romsFile:
		readRoms = csv.reader(romsFile, delimiter=',')
		for row in readRoms:
			romList.append(rom.Rom(row[1],row[0]))

def initFuncades(funList):
	#Reading the csv file to get the rom list (Displayed name,address,username,password) with "," delimiter
	#Username and password are there in case no known_hosts file is found in the program directory
	with open('funcade.csv') as funFile:
		readFun = csv.reader(funFile, delimiter=',')
		for row in readFun:
			funList.append(fun.Funcade(row[0],row[1],row[2],row[3]))
