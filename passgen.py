import random
from termcolor import cprint

cprint("""


	██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗
	██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║
	██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
	██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
	██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║
	╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
	                                  		 Made by hei$enberg                         
                                                 


	""", 'red')

try:
	l=int(input('	enter the lenght of your password> '))
	i=0
	p=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '$', '@', '!', '#', '&', '*']
	password = ''

	while i!=l:
		password += random.choice(p)
		i+=1

	cprint(f'	your password is> {password}', 'blue')
	k=len(password)
	cprint(f'	//the length: {k}//', 'yellow')
except KeyboardInterrupt:
	cprint('exiting...', 'red')