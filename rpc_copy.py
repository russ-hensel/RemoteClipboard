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

import pyperclip     # system clipboard access
import rpyc          # remote procedure call support

import sys
import time


# 60 * 5 = 5 minutes
TRY_TIMES     = 60       # how many time this will attempt to connect
TRY_SLEEP     = 5       # time in sec it will sleep between attempts

VERSION       = "2015 Feb 14.2"

class RpcCopy:
    """
    This class supports copying to a clipboard on a remote computer
    """

    def __init__(self  ):

        self.connection  =  None

    def connectNow( self,  ipadr ):
        rval    = True
        try:
            print "RpcCopy trying connect to ip_adr = ", ipadr
            sys.stdout.flush()
            self.connection  = rpyc.connect( ipadr, 18861)

        except Exception as inst:
            rval   = False
            
        if rval:
            print "RpcCopy connected"
            sys.stdout.flush()
        else:
            pass
        return rval

    def tryConnect( self, ipadr, times = 1, sleep = 0 ):
        for ix in range( times ):
          if rpc_copy.connectNow( ipadr ):
              return True

          else:
              time.sleep( sleep )

        return False


    def runn( self,  ):
        """
        Infinite loop, poll 
        """
        old_clip = ""
        while True:  # infinite loop

            new_clip  = pyperclip.paste()

            if new_clip != "":
                if new_clip != old_clip:
                    # next for debug
                    # print "new clip ", new_clip ; sys.stdout.flush()
                    old_clip = new_clip

                    self.connection.root.update_clip( new_clip )   # call server to update it
                    #if new_clip[0:8]  == "rpc stop":
                        #return
            time.sleep( .5 )    # this is how often the remote computer is updated


        return "done"

if __name__ == '__main__':

     # client is where cliips
     print "rpc_copy: enable rpc copying from this computer"

     # modify this to match the tcpip address of your remote computer which will paste
     ip_adr            = "192.168.0.103"
     ip_adr_smithers   = "192.168.0.108"
     ip_adr_xp         = "192.168.0.109"    # xp
     ip_adr_pi         = "192.168.0.175"


     rpc_copy    = RpcCopy( )   #


     rval  = rpc_copy.tryConnect( ip_adr_pi, times=TRY_TIMES, sleep = TRY_SLEEP )
     if rval:

         rpc_copy.runn()

     print "rpc_copy all done"




