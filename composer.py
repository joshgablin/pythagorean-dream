import matplotlib.pyplot as plt



class noteobj_plot:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

fig = plt.figure()
#ax = fig.add_subplot(111)


#set the frequency axis to logarithmic
plt.yscale("log")
#set the axes length
#xlim will be adjustable by the user to scroll through the composition
ax.set_ylim([20, 20000])
ax.set_xlim([0, 10])

notearray = []

#i = 0
#framelim = ax.get_lim()
#framelength = framelim[1] - framelim[0]

#while i != framelength:
#    notearray.append([])
#    i = i + 1


def onclick(event):
    #snap the x value to a note grid
    #DEVNOTE: might want to make this oprtional for a "freeform" mode)

    intx = round(event.xdata)
    notefreq = event.ydata

    #Tell us where we added the note 
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, intx, notefreq))
    #note = noteobj_plot(intx, notefreq, "note")
    plt.plot(intx, notefreq, 'ro', picker=5)

    #notearray[i].append(notefreq)
    fig.canvas.draw()
    

point = plt.plot(5,5)
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()