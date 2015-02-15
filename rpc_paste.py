# -*- coding: utf-8 -*-

"""
Overview:
    This program is one of a pair rpc_copy/rpc_paste that allows copy and paste
    between 2 computers with a network connection and runing Python
    Author:  russ_hensel, see:  http:www.opencircuits.com/User:Russ_hensel
    Download: Instructable:  ClipBoard Communication PC

Environment:
    OS:        Win 7 / Raspbian ( should work on other OSs with Python)
    IDE:       Spyder 2.3.1 and Idle
    Language:  Python 2.6 and 2.7

Reminders, notes:
    logs to console, watch the output there for debugging
    to terminate the program you can use ctrl-c or close the python interperter window

status/history

    working may still be enhancements

    enhancements ! = in process, * = done

"""

VERSION       = "2015 Feb 14.2"


import rpyc

import os
import sys
import pyperclip


# this is where you can paste the copy from the remote
# need a way to close this guy down, how?

class RPCGetCopy( rpyc.Service ):

    def xx__init__(self ): ### (1a)
        self.myName         = "RPCGetCopy  class instance"


    def on_connect(self):
        # code that runs when a connection is created
        # (to init the serivce, if needed)
        pass

    def on_disconnect(self):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        pass

    def exposed_update_clip( self, new_clip ):

        pyperclip.copy( new_clip )
        #print "got clip >>", new_clip  ;  sys.stdout.flush()    # for debug
        #if new_clip[0:8]  == "rpc stop":    # for later implementation?
            # how do we stop this guy return
            #pass

if __name__ == "__main__":

    print "Starting  server rpc_paste ...( stop by ctrl-c or closing interperter)"
    sys.stdout.flush()
    #os.system.
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer( RPCGetCopy, port = 18861 )
    t.start()
    #print "now after t.start()"   # for debug
    sys.stdout.flush()




