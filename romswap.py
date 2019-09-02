from tkinter import *
import pathlib
import os
import bCallbacks

################################################################
# A simple python GUI for swapping arcade roms on              #
# Raspberry Pis running retropie.                              #
# Writes a new autostart.sh script with the chosen             #
# rom name from the roms list (defined in the romlist.csv)     #
# and tries to upload it to the corresponding arcade           #
# (defined in the funcade.csv file) using user - pass          #
# authentication if no known_hosts file is found in the        #
# program directory. Contact me for help.                      #
# Use funcade.csv and romlist.csv as a template for your setup #
################################################################

__author__ = "Orfeas Artinopoulos aka psyborg0ne"
__copyright__ = "Copyright 2019"
__version__ = "1.0"
__maintainer__ = "Orfeas Artinopoulos"
__email__ = "artinopoulosorfeas@gmail.com"
__status__ = "Production"

#Declaration
funcades = []
roms 	 = []

#Change local working path to program folder
print("Changing local working path...")
os.chdir(pathlib.Path(__file__).parent)

#Initialize roms and funcades
bCallbacks.initRoms(roms)
bCallbacks.initFuncades(funcades)

window = Tk()
window.title("Arcade Rom Swapper")

signature = Label(window, text="psyborg0ne, making things work since 1997", bd=0, relief=SUNKEN)
signature.grid(row=0, columnspan=3)

#Initialization of the arcade listbox
funcadeLb = Listbox(window, selectmode=SINGLE, exportselection=0)
for i in funcades:
	funcadeLb.insert(END, i.name)
funcadeLb.select_set(0)
funcadeLb.grid(row=1, column=0)

#Load button initialization											  		V Funcade object from listbox V   	 V Rom object from listbox V
loadB = Button(window, text="Load", command=lambda:bCallbacks.loadRom(funcades[funcadeLb.curselection()[0]], roms[romsLb.curselection()[0]], statusL))
loadB.grid(row=1, column=1)

#Initialization and sort of the roms listbox
romsLb = Listbox(window, selectmode=SINGLE, exportselection=0)
roms.sort(key=lambda x: x.name)
for i in roms:
	romsLb.insert(END, i.name)
romsLb.select_set(0)
romsLb.grid(row=1, column=2)

romsBar = Scrollbar(window, orient="vertical")
romsBar.config(command=romsLb.yview)

romsLb.config(yscrollcommand=romsBar.set)
romsBar.grid(row=1,column=4)

#Status bar initialization
statusL = Label(window, text="Waiting...", bd=0, relief=SUNKEN)
statusL.grid(row=2, columnspan=3, sticky=W)

window.mainloop()
