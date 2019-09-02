import pysftp
import os

#Declaring the remote path where autostart script is placed
REMOTE_DIR = '/opt/retropie/configs/all/'

class Funcade:
	def __init__(self, name, ftpAdress, ftpUser, ftpPassword):
		self.name = name
		self.addr = ftpAdress
		self.user = ftpUser
		self.password = ftpPassword

	def swapRom(self, status, rom):
		cnopts = pysftp.CnOpts()

		if os.path.isfile('known_hosts'): #If known_hosts file found in program dir use that
			print('known_hosts file found.')
			print('Using it to connect securely.')
			cnopts.hostkeys.load('known_hosts')
		else: 								#Else use only user - pass authentication
			print('known_hosts file not found.')
			print('WARNING!')
			print('Connecting without key. Security is compromised.')
			cnopts.hostkeys=None

		try:
			#Try to connect and upload script file
			arcade = pysftp.Connection(host=self.addr, username=self.user, password=self.password, cnopts=cnopts)
			print("Connected succesfully to" + self.name + '!')
			print('Uploading...')

			arcade.chdir(REMOTE_DIR)
			arcade.put('autostart.sh')
			print("Rebooting " + self.name + " at " + self.addr)
			arcade.execute('sudo reboot')
			arcade.close()

			status.config(text="Operation complete! Loaded " + rom.name + " to " + self.name)

		except:
			#Print exception if no connection is possible
			print("Connection to " + self.name + ' failed!')
			print('Aborting operation...')
			status.config(text="Operation aborted! " + self.name + " is unreachable")

		#Remove the local script file after operation
		print("Removing local autostart.sh...")
		os.remove('autostart.sh')
