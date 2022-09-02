import pandas as pd
class HeikinAshi:
    @staticmethod
    def convert(df):
        newdf = df.copy()
        # print(df)
        dateTime = df.index.tolist()

        for i in range(0,len(df)):
            newdf.at[dateTime[i],'Close'] = round((df['Open'][i] + df['Close'][i] + df['High'][i] + df['Low'][i])/4,2)
            if(i==0):
                newdf.at[dateTime[i],'Open'] = round((df['Open'][i]+df['Close'][i])/2,2)
            else:
                newdf.at[dateTime[i],'Open'] = round((newdf['Open'][i-1]+df['Close'][i-1])/2,2)
            newdf.at[dateTime[i],'High'] = max(df['High'][i],newdf['Open'][i],newdf['Close'][i])
            newdf.at[dateTime[i],'Low'] = min(df['Low'][i],newdf['Open'][i],newdf['Close'][i])
        # print(newdf)
        
        return newdf
