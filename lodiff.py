#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright Viktor Kartashov 2014
"""
"""

import sys,uno,os
from time import sleep
from com.sun.star.beans import PropertyValue
from com.sun.star.beans.PropertyState import DIRECT_VALUE

# launching libreoffice
newpid = os.fork()
if newpid == 0:
	os.system("startlo.sh")
	sys.exit()
sleep(1)


local = uno.getComponentContext()
resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)

url1 = "file://" + str(os.path.abspath(sys.argv[1]))
url2 = "file://" + str(os.path.abspath(sys.argv[2]))

#print ("First argument: %s" % str(sys.argv[1]))
#print ("Second argument: %s" % str(sys.argv[2]))

props = []
props.append(PropertyValue('ShowTrackedChanges',0,True,DIRECT_VALUE))
document = desktop.loadComponentFromURL(url2, "_blank", 0, (tuple(props)))

#frame = document.getCurrentController().getFrame()
#frame = desktop.getCurrentFrame
dispatcher = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.DispatchHelper",context)
#dispatcher = context.ServiceManager.createInstance("com.sun.star.frame.DispatchHelper")
dispatcher.executeDispatch(document.getCurrentController().getFrame(), ".uno:ShowTrackedChanges", "", 0, (tuple(props)))

props[0] = PropertyValue('URL',0,url1,DIRECT_VALUE)
#props.append( PropertyValue('URL',0,url1,DIRECT_VALUE))
dispatcher.executeDispatch(document.getCurrentController().getFrame(), ".uno:CompareDocuments", "", 0, (tuple(props)))
#dispatcher.executeDispatch(frame, ".uno:CompareDocuments", "", 0, (tuple(props)))

sys.exit()
