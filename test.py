#!/bin/env python
import os
import re
import sys
import shutil
import subprocess
def err(msg): print msg; exit(1)
if len(sys.argv) < 2:
    err("Usage: test.py <name> [<test#>]")
name = sys.argv[1]
tests = []
in_lines = open("%s.in"%name).readlines()
state = None
for line in in_lines:
    line = line.rstrip(' \r\n')
    if line in ('input', '??????? ??????'):
        tests.append(['',''])
        state = 0
    elif line in ('output', '???????? ??????'):
        state = 1
    else:
        tests[-1][state] += line + "\n"
if len(sys.argv) > 2:
    # run only the test specified by user
    # test # starts with 1
    tests = [tests[int(sys.argv[2])-1]]
print "Tests to run: %d"%len(tests)
if os.path.isfile('%s.cpp'%name):
    if not os.path.isfile('Makefile'):
        shutil.copy2('../Makefile', '.')
    subprocess.check_call('make', shell=True)
    cmd = "%s.exe"%name
elif os.path.isfile('%s.py'%name):
    cmd = "%s %s.py"%(sys.executable, name)
else:
    err("Couldn't find either %s.py or %s.cpp"%(name, name))

for i,test in enumerate(tests):
    print "Running test #%d"%(i+1)
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (sout, serr) = p.communicate(test[0])
    if serr != "":
        print sout
        err("While running: %s\nGot err output:\n%s"%(cmd, serr))
    expected = test[1].rstrip()
    got = sout.replace('\r','').rstrip()
    if got == expected:
        print "TEST SUCCESSFUL"
    else:
        print "TEST #%d FAILED"%(i+1)
        print "-- INPUT:\n", test[0].rstrip()
        print "-- EXPECTED OUTPUT:\n", expected
        print "-- OUTPUT:\n", got
        #print "DEBUG: %s %s"%(repr(expected), repr(got))
        print

