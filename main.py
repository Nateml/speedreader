import tkinter as tk
import tkinter.font as font
from time import sleep

wn = tk.Tk()
wn.geometry('800x200')


text = "There is blood under my fingernails. I wonder how many of my people I’ve killed this time I thrust my hands into the barrel beside the stables. The ice- coldwater bites at my skin, but the blood clings. I shouldn’t bother, because it will all be gone in an hour anyway, but I hate this. The blood. The not knowing. Hooves ring against the cobblestones somewhere behind me, followed by the jingle of a horse’s bridle. I don’t need to look. My guard commander always follows at asafe distance until the transition is complete.Guard commander. As if Grey has men left to command. As if he didn’t earn the title by default. I swipe the water from my hands and turn. Grey stands a fewyards back, holding the reins of Ironheart, the fastest horse in thestables. The animal is blowing hard, its chest and flanks damp withsweat despite the early- morning chill."
wpm = 400
time = 1 / (wpm / 60)
def start():
    global wn
    global text
    btn.destroy()
    myFont = font.Font(family='Helvetica', size=69, weight='bold')
    T = tk.Text(wn, height=1, width=20)
    T.grid(row=1, column=0)
    i = 0
    curWord = []
    for let in text:
        if let == " ":
            word = "".join(curWord)
            print(word)
            T.insert("1.0", word)
            T["font"] = myFont
            curWord = []
            wn.update()
            sleep(time)
            T.delete("1.0", "end")
        else:
            curWord.append(let)
    


    T["font"] = myFont
    T.tag_configure("center", justify='center')
    T.tag_add("center", 1.0, "end")
    

btn = tk.Button(master=wn, text="HI", command=start)
btn.grid(row=0, column=0)



    

wn.mainloop()
