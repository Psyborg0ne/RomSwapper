# RomSwapper
A basic python GUI to change the active rom on arcade cabinets I built running retropie (mame-libretro) on RPis
## Usage
1. Install python3 (if not already installed)
2. Install pysftp module `pip3 install pysftp`
3. Configure *romlist.csv* and *funcade.csv* according to your preferences <br>Use the ones provided as a template
4. Use `python3 romswap.py` from inside script directory to execute
5. Choose your arcade cabinet from the left listbox and the rom to use on the right. <br>Finally press load and let it do the job
## Warning
**It's best to use a known_hosts file in the directory of the script with the arcades you are going to connect to for improved security.**<br>
Don't worry if you don't have one. The username - password in the funcade.csv file is used when no such file is found!
### Contact
Contact me via e-mail or PM if you need assistance with anything related to the program. Also, feedback is much appreciated!

### Backstory
*I work as an IT assistant and arcade room supervisor in a hotel. I made some arcade cabinets using RPis this year and we slowly started migrating from the traditional cabinets. Thing is we still use some of the old ones. And the old ones are prone to errors. The cabinets I built use retropie, a coin mech for the credits and load only one rom at boot. So long story short when one of the old cabinets misbehave and is put out of order, I have to manually edit the remote files on the arcades I built to change the rom and then reboot them and this usually takes some time due to the RPis using wireless connection instead of ethernet. In the end I made this piece of automation to make things faster and easier for me and the rest of my co-workers.*
