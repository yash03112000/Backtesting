import tkinter as tk
import pandas as pd




class Window1:

	def __init__(self):


		self.root=tk.Tk()

		self.root.geometry("600x400")




		self.instrument = tk.StringVar()
	
		self.instrumentEntry = tk.Entry(self.root,textvariable = self.instrument, font=('calibre',10,'normal'))
		self.instrumentLabel = tk.Label(self.root, text = 'Instrument', font = ('calibre',10,'bold'))


		self.submitBtn = tk.Button(self.root,text = 'Submit', command = self.submit)



		self.instrumentLabel.grid(row=1,column=0)
		self.instrumentEntry.grid(row=1,column=1)
		self.submitBtn.grid(row=2,column=1)



	def submit(self):
		self.root.destroy()
	def execute(self):
		self.root.mainloop()

	def getValues(self):
		return self.instrument.get()



