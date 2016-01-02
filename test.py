#!/bin/env python
import re
import sys
import shutil
import subprocess
def err(msg): print msg; exit(1)
if len(sys.argv) < 2:
    err("Usage: test.py <name> [<test#>]")
name = sys.argv[1]
if len(sys.argv) > 2:
    test_n = int(sys.argv[2])
else:
    test_n = None
tests = []
in_lines = open("%s.in"%name).readlines()
state = None
for line in map(str.rstrip, in_lines):
    if line in ('input', '??????? ??????'):
        tests.append(['',''])
        state = 0
    elif line in ('output', '???????? ??????'):
        state = 1
    else:
        tests[-1][state] += line + "\n"
print "%d tests total"%len(tests)
if os.path.isfile('%s.py'%name):
    cmd = "python %s.py"%name
elif os.path.isfile('%s.cpp'%name):
    if not os.path.isfile('Makefile'):
        shutil.copy2('../Makefile', '.')
    subprocess.check_output('make', shell=True)
    cmd = "%s.exe"%name
else:
    err("Couldn't find either %s.py or %s.cpp"%(name, name))
