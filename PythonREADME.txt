Directions to use Python Scripts for Newbies (like me):

- Common packages
os, os.path, sys, shutil, imp

- Add a directory to default paths python uses for modules etc
import sys	*only first time*
sys.path.append(<dir>)

- Module management
import imp
<var> = imp.load_source(<filename>,<path>)
imp.reload(<modulename>)

- Clear the interpreter window
>>> import os *only first time*
>>> clear = lambda: os.system('cls')
>>> clear()

- Exit the interpreter
quit()