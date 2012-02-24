#!/usr/bin/env python

#second attempt at getting something from Glade to run in python, so I can make pretty things

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade

class HellowWorldGTK:

	def __init__(self):
		self.gladefile = "pyhelloworld.glade"
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		self.glade.connect_signals(self)
		self.glade.get_object("MainWindow").show_all()
		
	def on_MainWindow_delete_event(self, widget, event):
		gtk.main_quit()
		
if __name__ =="__main__":
	try:
		a = HellowWorldGTK()
		gtk.main()
	except KeyboardInterrupt:
		pass