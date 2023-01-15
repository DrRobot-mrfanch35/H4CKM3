#!/usr/bin/python3

import os


print("***************************************\n**       Codé par MISTER FANCH       **\n***************************************\n \n  _    _          _____ _  __  __  __ ______ \n | |  | |   /\   / ____| |/ / |  \/  |  ____|\n | |__| |  /  \ | |    | ' /  | \  / | |__   \n |  __  | / /\ \| |    |  <   | |\/| |  __|  \n | |  | |/ ____ \ |____| . \  | |  | | |____ \n |_|  |_/_/    \_\_____|_|\_\ |_|  |_|______|\n \n")

def main():
	n = input("0 > Mise à jour de Linux\n1 > SEToolkit\n2 > Metasploit Framework\n3 > Attaques Wifi\n4 > Generateur de mot de passe\n5 > Hacker la Nasa\n\n\nPour quitter, appuyez sur CTRL + C \n\nChoisissez une option : ")

	if n == '0':
		os.system("apt-get update && apt-get full-upgrade -y")

	if n == '1':
		os.system("setoolkit") 

	if n == '2':
		os.system("msfconsole")

	if n == '3':
		os.system("wifite")

	if n == '4':
		os.system("apt-get install cupp && cupp -i")

	if n == '5':
		os.system("apt-get install hollywood -y && hollywood")


if __name__ == "__main__":
	main()
