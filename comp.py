#!/usr/bin/env python

import os
from subprocess import call
import subprocess
import colorama
from colorama import Fore
from colorama import Style
import sys

EDITOR = os.environ.get('EDITOR','vim')


cpp_file = sys.argv[1]


    
if not cpp_file.endswith(".cpp"):
    cpp_file += ".cpp"
    
if not os.system('g++ ' + cpp_file + ' -o a') == 0:
    print(Fore.RED+ "FALIURE" + Style.RESET_ALL)
    exit()
    
os.system("echo Compiling " + cpp_file)
os.system('g++ ' + cpp_file + ' -o a -Wall')

os.system("echo Running ")
os.system("echo -------------------")


f = 'in'

call([EDITOR, f])

f = open('in', 'r')
content = f.read()

os.system("./a < in > out")
print("\nINPUT: \n")
print(content)
os.system("echo -------------------")
f.close()


print(Fore.GREEN+ "\nOUTPUT: \n" + Style.RESET_ALL)
out = open("out" , "r")
content = out.read()
print(content)
os.system("echo -------------------")
out.close()

os.system("rm in")
os.system("rm out")
os.system("rm a")

