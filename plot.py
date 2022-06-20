import imp
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from Peaks import *
from User import *


def plot(df):
    def animate(i):
        i+=1
        if(i<=360):
            xar = time[0:i+1]
            yar = close[0:i+1]
        elif(i==361):
            user.exitProcedure(close[-1],time[i])
        
        if(i<=360):
            ax1.clear()
            ax1.plot(xar,yar)
            every_nth = 20
            for n, label in enumerate(ax1.xaxis.get_ticklabels()):
                if n % every_nth != 0:
                    label.set_visible(False)
            if(i>0):
                indices = peaks.getPeaks(close[i-1],close[i],i)
                minimaY = []
                minimaX = []
                maximaY = []
                maximaX = []

                for ind in indices[0]:
                    minimaY.append(close[ind])
                    minimaX.append(time[ind])

                for ind in indices[1]:
                    maximaY.append(close[ind])
                    maximaX.append(time[ind])
                plt.scatter(minimaX,minimaY,color="red")
                plt.scatter(maximaX,maximaY,color="green")
                user.checkTargetAndStoploss(close[i],time[i])
                if(indices[2]=="MAXIMA"):
                    user.shortSell(close[i],time[i])
                elif(indices[2]=="MINIMA"):
                    user.buy(close[i],time[i])


    close = []
    time = []
    close = df['Close']
    dateTime = df.index.tolist()
    for i in dateTime:
        timetemp =  i.strftime("%H:%M")
        time.append(timetemp)    
    peaks = Peaks(df)
    user = User()
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ani = animation.FuncAnimation(fig, animate, interval=0)
    plt.show()
