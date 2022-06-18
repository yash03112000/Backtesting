import imp
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from peaks import *



def plot(time,close,df):
    xar = []
    yar = []
    def animate(i):
        i+=1
        if(i<=369):
            xar = time[0:i]
            yar = close[0:i]
        # print("xar",xar)
        ax1.clear()
        ax1.plot(xar,yar)
        every_nth = 20
        for n, label in enumerate(ax1.xaxis.get_ticklabels()):
            if n % every_nth != 0:
                label.set_visible(False)
        i = i + 10
        getPeaks(df)




    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
