# ddos by SBC MY
import subprocess


def ping(target):
	command = ["ping", target, "-t", turbo]
	return subprocess.call(command)

print()
print()
print()
print( "░██████╗██████╗░░█████╗░  ███╗░░░███╗██╗░░░██╗")
print( "██╔════╝██╔══██╗██╔══██╗  ████╗░████║╚██╗░██╔╝")
print( "╚█████╗░██████╦╝██║░░╚═╝  ██╔████╔██║░╚████╔╝░")
print( "░╚═══██╗██╔══██╗██║░░██╗  ██║╚██╔╝██║░░╚██╔╝░░")
print( "██████╔╝██████╦╝╚█████╔╝  ██║░╚═╝░██║░░░██║░░░")
print( "╚═════╝░╚═════╝░░╚════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░")
print()
print()
print()

target = input("masukkan website target: ")
turbo = input("masukkan nilai turbo [max = 255]: ")
print(ping(target))

