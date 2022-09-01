import tkinter as tk
import pandas as pd




class Window1:

	def __init__(self):


		self.root=tk.Tk()

		self.root.geometry("600x400")
		filePath=r"./Spreadsheats/Dropdowns.xlsx"

		excel = pd.read_excel(filePath)


		filePath=r"./Spreadsheats/Dropdowns.xlsx"

		excel = pd.read_excel(filePath)

		self.timeFrameList = [i for i in excel['TimeFrame'] if str(i)!='nan']
		self.chartList = [i for i in excel['Chart'] if str(i)!='nan']
		self.indexList = [i for i in excel['Index'] if str(i)!='nan']





		self.screenerName=tk.StringVar()
		self.screenerName.set("Name")
		self.timeFrame = tk.StringVar()
		self.timeFrame.set(self.timeFrameList[0])
		self.chart = tk.StringVar()
		self.chart.set(self.chartList[0])
		self.index = tk.StringVar()
		self.index.set(self.indexList[0])

		self.timeFrameDrop = tk.OptionMenu( self.root , self.timeFrame , *self.timeFrameList )
		self.chartDrop = tk.OptionMenu( self.root , self.chart , *self.chartList )
		self.indexDrop = tk.OptionMenu( self.root , self.index , *self.indexList )




		self.screenerEntry = tk.Entry(self.root,textvariable = self.screenerName, font=('calibre',10,'normal'))

		self.screenerLabel = tk.Label(self.root, text = 'screener Name', font=('calibre',10, 'bold'))
		self.timeFrameLabel = tk.Label(self.root, text = 'TimeFrame', font = ('calibre',10,'bold'))
		self.chartLabel = tk.Label(self.root,text = 'Chart', font = ('calibre',10,'bold'))
		self.indexLabel = tk.Label(self.root,text = 'Index', font = ('calibre',10,'bold'))




		self.submitBtn = tk.Button(self.root,text = 'Submit', command = self.submit)


		self.screenerLabel.grid(row=0,column=0)
		self.screenerEntry.grid(row=0,column=1)
		self.timeFrameLabel.grid(row=1,column=0)
		self.timeFrameDrop.grid(row=1,column=1)
		self.chartLabel.grid(row=2,column=0)
		self.chartDrop.grid(row=2,column=1)
		self.indexLabel.grid(row=3,column=0)
		self.indexDrop.grid(row=3,column=1)
		self.submitBtn.grid(row=4,column=1)



	def submit(self):
		self.root.destroy()
	def execute(self):
		self.root.mainloop()

	def getValues(self):
		return self.screenerName.get(), self.chart.get(), self.timeFrame.get(), self.index.get()



