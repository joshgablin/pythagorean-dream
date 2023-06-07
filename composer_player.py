import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import math
import numpy
import pyaudio


class noteobj_plot:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

fig = plt.figure()
ax = fig.add_subplot(111)


#set the frequency axis to logarithmic
plt.yscale("log")
#set the axes length
ax.set_ylim([20, 20000])
ax.set_xlim([0, 10])



#build the note array
#this is not the master note array, it only handles notes in the current fram
#DEVNOTE: update to change the frame position in the master note array

notearray = []
framebounds = ax.get_xlim()
framelen = framebounds[1] - framebounds[0]

#make and show the grid notes will snap to
#DEVNOTE: make this optional to users
ax.grid(color='lightgrey', linestyle='dashed', linewidth=1)

#make the radio selector for the wave form


#buts = plt.figure()
#ax2 = buts.add_subplot(123)
#buts = widgets.RadioButtons(AXESSSS, ["sin", "saw"])



#fill the notearray with the measure length
i = 0
while i != framelen:
    i = i + 1
    notearray.append([])


def onclick(event):
    #snap the x value to a note grid
    #DEVNOTE: might want to make this optional for a "freeform" mode)

    intx = round(event.xdata)


    #Tell us where we added the note 
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, intx, event.ydata))
    note = noteobj_plot(intx, event.ydata, "new note")
    plt.plot(intx, event.ydata, 'ro', picker=5)
    notearray[intx].append(note)
    fig.canvas.draw()
    
def on_key(event):
    print('you pressed', event.key, event.xdata, event.ydata)
    i = 0
    j = len(notearray)

    while i <= j:
        playnote(notearray[i - 1])
        #print(len(notearray[i])
        print(i)
        i = i + 1


#Play the list of notes for this measure
#DEVNOTE: The audio will need to play in a separate thread
#         This will let the user adjus the composition as they hear it
def playnote(notelist):
    print(notelist)
        

    if notelist:
        num_notes = len(notelist)

        p = pyaudio.PyAudio()  # initialize pyaudio

        # sampling rate
        sample_rate = 22050

        # seconds to play sound
        #DEVNOTE: Make this adjustable
        LENGTH = .5  

        frames = int(sample_rate * LENGTH)

        wavedata = ''

        # generating waves
        stream = p.open(
            format=p.get_format_from_width(1),
            channels=1,
            rate=sample_rate,
            output=True)

        CHUNK = 256

        frequencies = []
        for tone in notelist:
            frequencies.append(tone.y * (2**(int(4)+ 1)))
            print(frequencies)


        y=0
        for x in range(frames//CHUNK):
            n=0
            wavedata=b''
            while n<CHUNK:
                wave=0
                for freqs in frequencies:
                    wave += math.sin((y) / ((sample_rate / freqs) / math.pi)) * 127 + 128
                wave = wave/num_notes
                wavedata += bytes([int(wave)])
                y+=1
                n+=1

            stream.write(wavedata)

        stream.stop_stream()
        stream.close()
        p.terminate()
    else:
        print("You haven't selected any notes!")

















point = plt.plot(5,5)
cid = fig.canvas.mpl_connect('button_press_event', onclick)
cie = fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()