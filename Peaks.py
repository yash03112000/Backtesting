



class Peaks:

    percentage = 0.4
    tick = 0


    minimaIndices = []
    maximaIndices = []
    trend = "UP"
    prev = (0,0)



    def __init__(self,df):
        self.df = df
        self.prev = (df['Open'][0],0)
        self.tick = self.percentage*df['Open'][0]/100


        
    def getPeaks(self,priceA,priceB,i):
        status = "None"
        if(priceB > priceA):
            if self.trend=="DOWN":
                self.trend = "UP"
                self.prev = (priceA,i-1)
            else:
                # check minima condition
                exp = priceB - self.prev[0]
                if(exp > self.tick):
                    # Execute Minima
                    self.minimaIndices.append(self.prev[1])
                    status = "MINIMA"
        elif(priceB<priceA):
            if self.trend=="UP":
                self.trend = "DOWN"
                self.prev = (priceA,i-1)
            else:
                # check maxima
                exp = self.prev[0] - priceB
                if(exp > self.tick):
                    # Execute Maxima
                    status = "MAXIMA"
                    self.maximaIndices.append(self.prev[1])



        return (self.minimaIndices,self.maximaIndices,status)