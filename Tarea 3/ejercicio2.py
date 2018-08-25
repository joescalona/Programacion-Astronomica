import sys

personal= ['Ana','Maria','Itziar']

print("Hello. Please enter your name:")

name = sys.stdin.readline().strip()

if name in personal:
	print('Access granted.')
else:
	print('Acces denied.')