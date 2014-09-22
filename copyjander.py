import sys
from Tkinter import *
from tkFileDialog import askdirectory
from shutil import copy

class App:

	def __init__(self, root):
	
		frame = Frame(root)
		frame.pack()
	
		frame_open = Frame(frame)
		frame_open.pack()
	
		# Label 'Escull directori amb les commareas de origen: '
		self.txt_dir = StringVar() # Literal del label
		self.lbl_dir = Label(frame_open, textvariable=self.txt_dir, anchor=W, width=100)
		self.lbl_dir.pack(side=LEFT)
		self.txt_dir.set("Escull directori amb les commareas de origen: ")
		
		# Boto Obrir
		self.bt_open = Button(frame_open, text="Obrir", anchor=W, command=self.open)
		self.bt_open.pack(side=LEFT)			
		
		# Label 'Selecciona l'entorn on copiar les commareas:'
		self.txt_dst = StringVar()
		self.lbl_dst = Label(frame, textvariable=self.txt_dst, anchor=W, height=1, width=100)
		self.lbl_dst.pack()	
		self.txt_dst.set("Selecciona l\'entorn on copiar les commareas:")
		
		# Listbox amb els entorns
		self.list_targets = Listbox(frame, selectmode=EXTENDED, height=4)
		self.list_targets.pack(fill=BOTH, expand=1)
		
		targets = [
			('Local', ['z:\\']), 
			('Test', ['\\\\was-ts8\microinf\commareas']), 
			('Pre', ['\\\\was-pre8\microinf\commareas']), 
			('Produccio', [
					'\\\\was-c01\microinf\commareas', 
					'\\\\was-c02\microinf\commareas',
					'\\\\was-c03\microinf\commareas',
					'\\\\was-c04\microinf\commareas',
					'\\\\was85-b01\microinf\commareas',
					'\\\\was85-b02\microinf\commareas'
				]
			)
		]
		for key, value in targets:
			self.list_targets.insert(END, key)
		self.targets = targets	

		# Message Log
		self.txt_log = StringVar()
		self.msg_log = Message(frame, textvariable=self.txt_log, anchor=W, width=200).pack()

		# Label Missatges
		self.txt_msg = StringVar()
		self.lbl_msg = Label(frame, textvariable=self.txt_msg, fg="red", anchor=W, height=1, width=100).pack()
		
		
		button_opt = {'fill': BOTH, 'padx': 5, 'pady': 5, 'side': LEFT}
		
		# Boto Tancar
		self.bt_close = Button(frame, text="Tancar", command=frame.quit).pack(**button_opt)
		
		# Boto Copiar
		self.bt_copy = Button(frame, text="Copiar", command=self.sync).pack(**button_opt)


	def open(self):
		self.dir = askdirectory()		
		# self.vDir = StringVar()
		# self.vDir.set(dir)
		self.txt_dir.set("Directori origen: {0}".format(str(self.dir)))

		
	def sync(self):
		items = self.list_targets.curselection()
		items = [self.targets[int(item)] for item in items]
		for item in items:			
			for server in item[1]:
				#self.copyFileToServer(self.vDir.get(), server)
				self.copyFileToServer(str(self.dir), server)

				
	def copyFileToServer(self, src, dst):
		try:
			self.txt_log.set("Copiant {0} a {1}... ".format(src, dst))			
			copy(src, dst)
		except IOError as e:
			self.txt_msg.set("IOError({0}) : {1}".format(e.errno, e.strerror))
		except:
			print "Unexpected error: ", sys.exc_info()[0]
			raise
		

		
root = Tk()
app = App(root)
root.mainloop()