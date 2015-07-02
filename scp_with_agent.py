#!/usr/bin/env python

import sys
import os

ssh_prog = '/usr/bin/ssh'
scp_prog = '/usr/bin/scp'

def scp_calling_as_ssh(argv):
    return ((sys.argv[1] == '-x') and 
            (sys.argv[-1].startswith('scp -t') or 
             sys.argv[-1].startswith('/usr/bin/scp -t')));    

def removeForwardAgentArg(argv):
    try:
        argv.remove('-oForwardAgent=no')
        argv.remove('-oForwardAgent no')
    except ValueError:
        pass

if(scp_calling_as_ssh(sys.argv)): #Being called as ssh from scp
    newArgs = sys.argv[1:]
    removeForwardAgentArg(newArgs)
    newArgs.insert(0, ssh_prog)
    os.execv(newArgs[0], newArgs)
else: #Being called as scp
    newArgs = [scp_prog, '-S' + os.path.abspath(sys.argv[0])] + sys.argv[1:]
    os.execv(newArgs[0], newArgs)
