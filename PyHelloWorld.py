#!/usr/bin/env python

#import the needed libraries

import sys
try:
	import pygtk
	pygtk.require("2.0")
except:
	pass
try:
	import gtk
	import gtk.glade
except:
	sys.exit(1)

# create main class

class HelloWorldGTK:
	"""This is an Hello World GTK application"""
	
	def __init__(self):
	
		#set the Glade file
		self.gladefile = "pyhelloworld.glade"
		self.wTree = gtk.glade.XML(self.gladefile)
		
		#Get the Main Window, and connect the "destroy" event
		#self.window = self.wTree.get_widget("MainWindow")
		#if (self.window):
			#self.window.connect("destroy", gtk.main_quit)
			
			
			
		#Create our dictionary and connect it
		dic = { "on_btnHelloWorld_clicked" : self.btnHellowWorld_clicked, "on_MainWindow_destroy" : gtk.main_quit }
		self.wTree.signal_autoconnect(dic)

	def btnHelloWorld_clicked(self, widget):
		print "Hello World!"
if __name__ == "__main__":
	hwg = HelloWorldGTK()
	gtk.main()