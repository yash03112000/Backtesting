

def getPeaks(df):
    
    percentage = 0.4
    tick = percentage*df['Open'][0]/100
    minimaY = []
    minimaX = []

    maximaY = []
    maximaX = []

    minimaIndices = []
    maximaIndices = []

    print("tick",tick)



    trend = "UP"
    prev = (df['Open'][0],0)

    for i in range(1,len(time),1):
        if(close[i] > close[i-1]):
            if trend=="DOWN":
                trend = "UP"
                prev = (close[i-1],i-1)
            else:
                # check minima condition
                exp = close[i] - prev[0]
                if(exp > tick):
                    # Execute Minima
                    minimaIndices.append(prev[1])
        elif(close[i]<close[i-1]):
            if trend=="UP":
                trend = "DOWN"
                prev = (close[i-1],i-1)
            else:
                # check maxima
                exp = prev[0] - close[i]
                if(exp > tick):
                    # Execute Maxima
                    maximaIndices.append(prev[1])



    for i in minimaIndices:
        minimaY.append(close[i])
        minimaX.append(time[i])

    for i in maximaIndices:
        maximaY.append(close[i])
        maximaX.append(time[i])