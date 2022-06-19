#! /usr/bin/env python3
import os,sys
import re
import subprocess
import tempfile
import argparse

WRAPPER_FILE = f'{os.path.dirname(os.path.realpath(__file__))}/wrapper.asm'


banner = '''

   _____ _          _ _               _          
  / ____| |        | | |             | |         
 | (___ | |__   ___| | | ___ ___   __| | ___     
  \___ \| '_ \ / _ \ | |/ __/ _ \ / _` |/ _ \    
  ____) | | | |  __/ | | (_| (_) | (_| |  __/    
 |_____/|_| |_|\___|_|_|\___\___/ \__,_|\___|    
  / ____|                         | |            
 | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                 

  ** https://github.com/AmitNiz/shellcode_generator.git **
'''
if len(sys.argv) == 1 or '-h' in sys.argv or '--help' in sys.argv:
	print(banner)



parser = argparse.ArgumentParser()

parser.add_argument('ifile',metavar='IFILE',type=str,help = 'input file')

parser.add_argument('-a','--arch',metavar='ARCH',type=str,default='elf32', 
					help = 'shell code architecture: elf32 (default), elf64, \
							macho32, macho64, win32, win64')

parser.add_argument('-f','--format',metavar='FORMAT',type=str,default='hex', 
					help = "output format.\nfor example '\\x' -> '\\xde\\xad\\xbe\\xef',\
											'' -> deadbeef. print as hexadecimal as default")

parser.add_argument('-v','--verbose',action='store_true',help='verbose mode')

if __name__ == '__main__':

	args = parser.parse_args()

	with open(WRAPPER_FILE,'r') as wrapper_file:
		wrapper = wrapper_file.read() # read the wrapper
	
	try:
		with open(args.ifile,'r') as code_file:
			assembly_code = code_file.read() # read the assembly code
	except:
		print(f'[!] ERROR:  can\'t open: {args.ifile}')
		exit(1)

	# create a temporary whole assembly file
	with tempfile.NamedTemporaryFile('w',delete=False) as asm_file: 
		asm_file.write(wrapper.format(CODE=assembly_code)) 


	obj_file = tempfile.NamedTemporaryFile('w+b',delete=False)
	
	#compile the assembly file
	res = subprocess.run(f'nasm -f {args.arch} -o {obj_file.name} {asm_file.name}',capture_output=True,shell=True)
	if res.returncode:
		print(f"[!] ERROR: {res.stderr.decode().split(':')[3]}")
		os.unlink(asm_file.name)
		exit(res.returncode)

	#disassemble
	res = subprocess.run(f'objdump -d --x86-asm-syntax=att {obj_file.name}',capture_output=True,shell=True)

	#delete temporary files
	os.unlink(asm_file.name)
	os.unlink(obj_file.name)

	#extract the opcodes
	opcodes = re.findall(r'\b([0-9a-f]{2})\s',res.stdout.decode())
	
	if args.verbose:
		print(f'[+] shellcode length: {len(opcodes)}')
		print('\n[+] objdump output:')
		print('-'*30)
		print(''.join(re.findall(r'\s+\w+: [\S.\s]*',res.stdout.decode())))
		print('\n[+] shellcode:')
		print('-'*30)
	if args.format == 'hex':
		print(''.join([chr(int(op,16)) for op in opcodes]))
	else:
		print(f'{args.format}'+f'{args.format}'.join(opcodes))

