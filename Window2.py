import tkinter as tk
import pandas as pd




class Window2:

	def __init__(self):


		self.root=tk.Tk()

		self.root.geometry("600x400")


		filePath=r"./Spreadsheats/Dropdowns.xlsx"

		excel = pd.read_excel(filePath)

		self.operandList = [i for i in excel['Operand'] if str(i)!='nan']
		self.operatorList = [i for i in excel['Operator'] if str(i)!='nan']


		self.operand = tk.StringVar()
		self.operand.set(self.operandList[0])
		self.operatorVar = tk.StringVar()
		self.operatorVar.set(self.operatorList[0])
		self.value = tk.IntVar()
		self.condition = {
			'operand':'',
			'operator':'',
			'value':0
		}
		self.entryConditions = []


		self.operandDrop = tk.OptionMenu(self.root,self.operand,*self.operandList)
		self.operatorDrop = tk.OptionMenu(self.root,self.operatorVar,*self.operatorList)
		self.valueEntry = tk.Entry(self.root,textvariable=self.value,font=('calibre',10,'normal'))
		self.headLabel = tk.Label(self.root,text = 'Entry Conditions', font = ('calibre',10,'bold'))
		self.operatorLabel = tk.Label(self.root,text = 'Operator', font = ('calibre',10,'bold'))
		self.operandLabel = tk.Label(self.root,text = 'Operand', font = ('calibre',10,'bold'))
		self.valueLabel = tk.Label(self.root,text = 'Value', font = ('calibre',10,'bold'))


		self.AddBtn = tk.Button(self.root,text='Add Entry Condition',command=self.addEntryCondition)
		self.submitBtn = tk.Button(self.root,text = 'Submit', command = self.submit)

		self.headLabel.grid(row=0,column=1)
		self.operandLabel.grid(row=1,column=0)
		self.operatorLabel.grid(row=1,column=1)
		self.valueLabel.grid(row=1,column=2)
		self.rowIndex = 2

		self.operandDrop.grid(row=self.rowIndex+1,column=0)
		self.operatorDrop.grid(row=self.rowIndex+1,column=1)
		self.valueEntry.grid(row=self.rowIndex+1,column=2)
		self.AddBtn.grid(row = self.rowIndex+2, column=1)
		self.submitBtn.grid(row=self.rowIndex+3,column=1)


	def submit(self):
		self.root.destroy()
	def execute(self):
		self.root.mainloop()

	def getValues(self):
		return self.entryConditions

	def addEntryCondition(self):
		self.condition['operand'] = self.operand.get()
		self.condition['operator'] = self.operatorVar.get()
		self.condition['value'] = self.value.get()
		self.entryConditions.append(self.condition.copy())
		a = tk.Label(self.root,text = self.condition['operand'], font = ('calibre',10,'bold'))
		b = tk.Label(self.root,text = self.condition['operator'], font = ('calibre',10,'bold'))
		c = tk.Label(self.root,text = self.condition['value'], font = ('calibre',10,'bold'))
		a.grid(row = self.rowIndex, column=0)
		b.grid(row = self.rowIndex, column=1)
		c.grid(row = self.rowIndex, column=2)
		self.operandDrop.grid(row=self.rowIndex+1,column=0)
		self.operatorDrop.grid(row=self.rowIndex+1,column=1)
		self.valueEntry.grid(row=self.rowIndex+1,column=2)
		self.AddBtn.grid(row = self.rowIndex+2, column=1)
		self.submitBtn.grid(row=self.rowIndex+3,column=1)
		self.rowIndex+=1





