import tkinter as tk
from turtle import st
import pandas as pd




class Window1:

	def __init__(self):


		self.root=tk.Tk()

		self.root.geometry("600x400")


		filePath=r"./Spreadsheats/Dropdowns.xlsx"

		excel = pd.read_excel(filePath)

		self.instrumentList = [i for i in excel['Stock'] if str(i)!='nan']
		self.timeFrameList = [i for i in excel['TimeFrame'] if str(i)!='nan']
		self.chartList = [i for i in excel['Chart'] if str(i)!='nan']
		self.tradetypeList = [i for i in excel['Tradetype'] if str(i)!='nan']
		self.productList = [i for i in excel['Product'] if str(i)!='nan']



		self.strategyName=tk.StringVar()
		self.strategyName.set("Name")
		self.instrument = tk.StringVar()
		self.instrument.set(self.instrumentList[0])
		self.timeFrame = tk.StringVar()
		self.timeFrame.set(self.timeFrameList[0])
		self.days = tk.IntVar()
		self.days.set(1)
		self.chart = tk.StringVar()
		self.chart.set(self.chartList[0])
		self.volume = tk.IntVar()
		self.volume.set(1)
		self.tradetype = tk.StringVar()
		self.tradetype.set(self.tradetypeList[0])
		self.product = tk.StringVar()
		self.product.set(self.productList[0])

		self.instrumentDrop = tk.OptionMenu( self.root , self.instrument , *self.instrumentList )
		self.timeFrameDrop = tk.OptionMenu( self.root , self.timeFrame , *self.timeFrameList )
		self.chartDrop = tk.OptionMenu( self.root , self.chart , *self.chartList )
		self.tradetypeDrop = tk.OptionMenu( self.root , self.tradetype , *self.tradetypeList )
		self.productDrop = tk.OptionMenu( self.root , self.product , *self.productList )



		self.strategyEntry = tk.Entry(self.root,textvariable = self.strategyName, font=('calibre',10,'normal'))
		self.daysEntry = tk.Entry(self.root,textvariable = self.days, font=('calibre',10,'normal'))
		self.volumeEntry = tk.Entry(self.root,textvariable = self.volume, font=('calibre',10,'normal'))

		self.strategyLabel = tk.Label(self.root, text = 'Strategy Name', font=('calibre',10, 'bold'))
		self.instrumentLabel = tk.Label(self.root, text = 'Instrument', font = ('calibre',10,'bold'))
		self.timeFrameLabel = tk.Label(self.root, text = 'TimeFrame', font = ('calibre',10,'bold'))
		self.daysLabel = tk.Label(self.root, text = 'Select Days', font = ('calibre',10,'bold'))
		self.chartLabel = tk.Label(self.root,text = 'Chart', font = ('calibre',10,'bold'))
		self.volumeLabel = tk.Label(self.root,text = 'Volume', font = ('calibre',10,'bold'))
		self.tradetypeLabel = tk.Label(self.root,text = 'Trade Type', font = ('calibre',10,'bold'))
		self.productLabel = tk.Label(self.root,text = 'Product', font = ('calibre',10,'bold'))



		self.submitBtn = tk.Button(self.root,text = 'Submit', command = self.submit)


		self.strategyLabel.grid(row=0,column=0)
		self.strategyEntry.grid(row=0,column=1)
		self.instrumentLabel.grid(row=1,column=0)
		self.instrumentDrop.grid(row=1,column=1)
		self.timeFrameLabel.grid(row=2,column=0)
		self.timeFrameDrop.grid(row=2,column=1)
		self.chartLabel.grid(row=3,column=0)
		self.chartDrop.grid(row=3,column=1)
		self.daysLabel.grid(row=4,column=0)
		self.daysEntry.grid(row=4,column=1)
		self.volumeLabel.grid(row=5,column=0)
		self.volumeEntry.grid(row=5,column=1)
		self.tradetypeLabel.grid(row=6,column=0)
		self.tradetypeDrop.grid(row=6,column=1)
		self.productLabel.grid(row=7,column=0)
		self.productDrop.grid(row=7,column=1)
		self.submitBtn.grid(row=8,column=1)



	def submit(self):
		self.root.destroy()
	def execute(self):
		self.root.mainloop()

	def getValues(self):
		return self.strategyName.get(), self.chart.get(), self.days.get(), self.instrument.get(), self.timeFrame.get(), self.volume.get(), self.tradetype.get(), self.product.get()



