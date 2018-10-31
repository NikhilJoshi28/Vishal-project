import matplotlib.pyplot as plt
import numpy as np

class hydrophobicity:
    def get_plot(user_input,windoww):
        # user_input = input("Type your amino acid sequence: ")
        # windoww = input("window size: ")
        window = int(windoww)
        user_input = user_input.upper()
        length = len(user_input)
        arrayy = []
        scores = {'G':0.00,'C':1.15,'I':0.97,'L':0.87,'F':0.85,'V':0.83,'W':0.67,'Y':0.60,'M':0.54,'A':0.33,'P':0.32,'H':0.25,'T':0.21,'S':0.05,'R':-0.01,'Q':-0.05,'N':-0.07,'D':-0.22,'E':-0.24,'K':-0.40}

        for x in user_input:
            arrayy.append(scores[x])

        yaxis=[]
        count = 0
        summ = 0

        for x in arrayy:
            summ = x+summ
            count=count+1
            if count%window==0:
                yaxis.append(summ/window)
                summ=0

        print ("Length of amino acid sequence: %d" %(length))
        print ("Window Size: %d" %(window))

        y_axis= np.array(yaxis)
        length = length - length%window
        t = np.arange(0, length, window)
        x_axis=np.array(t)
        print ("Number of points plotted: %d" %(len(x_axis)))
        fig, ax = plt.subplots()
        ax.plot(x_axis, y_axis)
        ax.set(xlabel='Amino acid sequence position', ylabel='Hydrophobicity score',
               title='''  Bandyopadhyay-Mehler Hydropathy plot  ''')

        ax.grid()
        fig.savefig("test.pdf")
        plt.show()

"""if __name__=="__main__":
    h = hydrophobicity()
    h.get_plot()
"""