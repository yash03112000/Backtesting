import tkinter as tk
import pandas as pd



	
class Window1:

	def __init__(self):
		self.root=tk.Tk()
		self.root.geometry("600x400")
		self.screenerBtn = tk.Button(self.root, text = 'Stocker Screener', command = lambda : self.submit("Screener"))
		self.strategyBtn = tk.Button(self.root, text = "Strategy Backtesting", command = lambda : self.submit("Strategy"))
		self.sarimaBtn = tk.Button(self.root, text = "Sarima Forecasting", command = lambda : self.submit("Sarima"))
		self.screenerBtn.pack()
		self.strategyBtn.pack()
		self.sarimaBtn.pack()



	def submit(self,key):
		self.key = key
		self.root.destroy()
	def execute(self):
		self.root.mainloop()

	def getValues(self):
		return self.key

