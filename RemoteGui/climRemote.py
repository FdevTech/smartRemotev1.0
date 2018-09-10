from tkinter import *
from pynput.keyboard import *
import time
import subprocess

device=""
variable=""
keyboard = Controller()
def climRemote(root,dev,var):
    global device ,variable
    device=dev
    variable=var
    window = Toplevel(root)
    window.title('Clim Remote')
    window.geometry("700x500+500+100")
    window.resizable(0, 0)
    window.configure(background='grey10')

    #Menu Bar
    menubar = Menu(window)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Créer")
    menu1.add_command(label="Editer")
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=window.quit)
    menubar.add_cascade(label="Fichier", menu=menu1)

    menu2 = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Editer", menu=menu2)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos")
    menubar.add_cascade(label="Aide", menu=menu3)

    window.config(menu=menubar)


    MainFrame = Frame(window,bg='grey10')
    MainFrame.grid(row=0,column=0,padx=8,pady=8)

    #Row One
    buttonOnOff = Button(MainFrame, text='POWER', width=15, height=2, bg='red2', fg='white' ,command=power)
    buttonOnOff.grid(row=0, column=0, padx=5, pady=5)
    # buttonMode = Button(MainFrame, text='MODE', width=15, height=2, bg='red2', fg='white', command=mode)
    # buttonMode.grid(row=0, column=2, padx=5, pady=5)
    #Row Two
    button1 = Button(MainFrame, text='16', width=15, height=2, fg='white', bg='grey45', command=t16)
    button1.grid(row=2, column=0, padx=5, pady=5)

    button2 = Button(MainFrame, text='17', width=15, height=2, bg='grey45', fg='white', command=t17)
    button2.grid(row=2, column=1, padx=5, pady=5)

    button3 = Button(MainFrame, text='18', width=15, height=2, bg='grey45', fg='white', command=t18)
    button3.grid(row=2, column=2, padx=5, pady=5)

    button4 = Button(MainFrame, text='19', width=15, height=2, bg='grey45', fg='white', command=t19)
    button4.grid(row=2, column=3, padx=5, pady=5)

    # Row Three
    button5 = Button(MainFrame, text='20', width=15, height=2, fg='white', bg='grey45', command=t20)
    button5.grid(row=3, column=0, padx=5, pady=5)

    button6 = Button(MainFrame, text='21', width=15, height=2, bg='grey45', fg='white', command=t21)
    button6.grid(row=3, column=1, padx=5, pady=5)

    button7 = Button(MainFrame, text='22', width=15, height=2, bg='grey45', fg='white', command=t22)
    button7.grid(row=3, column=2, padx=5, pady=5)

    button8 = Button(MainFrame, text='23', width=15, height=2, bg='grey45', fg='white', command=t23)
    button8.grid(row=3, column=3, padx=5, pady=5)

    # Row Four
    button9 = Button(MainFrame, text='24', width=15, height=2, fg='white', bg='grey45', command=t24)
    button9.grid(row=4, column=0, padx=5, pady=5)

    button10 = Button(MainFrame, text='25', width=15, height=2, bg='grey45', fg='white', command=t25)
    button10.grid(row=4, column=1, padx=5, pady=5)

    button11 = Button(MainFrame, text='26', width=15, height=2, bg='grey45', fg='white', command=t26)
    button11.grid(row=4, column=2, padx=5, pady=5)

    button12 = Button(MainFrame, text='27', width=15, height=2, bg='grey45', fg='white', command=t27)
    button12.grid(row=4, column=3, padx=5, pady=5)

    # Row Five
    button13 = Button(MainFrame, text='28', width=15, height=2, fg='white', bg='grey45', command=t28)
    button13.grid(row=5, column=0, padx=5, pady=5)

    button14 = Button(MainFrame, text='29', width=15, height=2, bg='grey45', fg='white', command=t29)
    button14.grid(row=5, column=1, padx=5, pady=5)

    button15 = Button(MainFrame, text='30', width=15, height=2, bg='grey45', fg='white', command=t30)
    button15.grid(row=5, column=2, padx=5, pady=5)

    # Row Six
    button16 = Button(MainFrame, text='Modhot', width=15, height=2, fg='white', bg='red', command=hot)
    button16.grid(row=6, column=0, padx=5, pady=5)

    button17 = Button(MainFrame, text='Modcold', width=15, height=2, bg='deep sky blue', fg='white', command=cold)
    button17.grid(row=6, column=1, padx=5, pady=5)

    button18 = Button(MainFrame, text='Moddry', width=15, height=2, bg='green3', fg='white', command=dry)
    button18.grid(row=6, column=2, padx=5, pady=5)

    button19 = Button(MainFrame, text='Modwind', width=15, height=2, bg='azure3', fg='white', command=wind)
    button19.grid(row=6, column=3, padx=5, pady=5)

    # Row Seven
    button20 = Button(MainFrame, text='End recording', width=15, height=2, bg='red', fg='white', command=end4)
    button20.grid(row=7, column=0, padx=5, pady=5)
    button21 = Button(MainFrame, text='End recording', width=15, height=2, bg='deep sky blue', fg='white', command=end1)
    button21.grid(row=7, column=1, padx=5, pady=5)
    button22 = Button(MainFrame, text='End recording', width=15, height=2, bg='green3', fg='white', command=end2)
    button22.grid(row=7, column=2, padx=5, pady=5)
    button23 = Button(MainFrame, text='End recording', width=15, height=2, bg='azure3', fg='white', command=end3)
    button23.grid(row=7, column=3, padx=5, pady=5)


    window.mainloop()
def cold () :
    
    exec1 = "lxterminal  --command='sudo /etc/init.d/lircd stop'"
    subprocess
    os.system(exec1)
    time.sleep(2)
    exec2 = "lxterminal  --command='sudo irrecord -f -d /dev/lirc0 ~/lirc.conf'"
    os.system(exec2)
    subprocess
    time.sleep(4)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(4)
    keyboard.type(device+"_modecold")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def hot () :
    print(device)
    exec1 = "lxterminal  --command='sudo /etc/init.d/lircd stop'"
    subprocess
    os.system(exec1)
    time.sleep(2)
    exec2 = "lxterminal  --command='sudo irrecord -f -d /dev/lirc0 ~/lirc.conf'"
    os.system(exec2)
    subprocess
    time.sleep(4)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(4)
    keyboard.type(device+"_modehot")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def wind():
    exec1 = "lxterminal  --command='sudo /etc/init.d/lircd stop'"
    subprocess
    os.system(exec1)
    time.sleep(2)
    exec2 = "lxterminal  --command='sudo irrecord -f -d /dev/lirc0 ~/lirc.conf'"
    os.system(exec2)
    subprocess
    time.sleep(4)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(4)
    keyboard.type(device+"_modewind")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def dry():
    exec1 = "lxterminal  --command='sudo /etc/init.d/lircd stop'"
    subprocess
    os.system(exec1)
    time.sleep(2)
    exec2 = "lxterminal  --command='sudo irrecord -f -d /dev/lirc0 ~/lirc.conf'"
    os.system(exec2)
    subprocess
    time.sleep(4)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(4)
    keyboard.type(device+"_modedry")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def power ():
    time.sleep(2)
    keyboard.type("KEY_POWER")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def mode ():
    time.sleep(3)
    keyboard.type("KEY_ALS_TOGGLE")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t16 ():
    time.sleep(3)
    keyboard.type("KEY_0")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t17 ():
    time.sleep(3)
    keyboard.type("KEY_1")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def  t18 ():
    time.sleep(3)
    keyboard.type("KEY_2")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t19 ():
    time.sleep(3)
    keyboard.type("KEY_102ND")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t20():
    time.sleep(3)
    keyboard.type("KEY_3")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t21 ():
    time.sleep(3)
    keyboard.type("KEY_4")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t22 ():
    time.sleep(3)
    keyboard.type("KEY_5")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t23():
    time.sleep(3)
    keyboard.type("KEY_6")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t24 ():
    time.sleep(3)
    keyboard.type("KEY_7")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t25 ():
    time.sleep(3)
    keyboard.type("KEY_8")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t26 ():
    time.sleep(3)
    keyboard.type("KEY_9")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t27():
    time.sleep(3)
    keyboard.type("KEY_A")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t28 ():
    time.sleep(3)
    keyboard.type("KEY_AB")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t29():
    time.sleep(3)
    keyboard.type("KEY_ADDRESSBOOK")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def t30 ():
    time.sleep(3)
    keyboard.type("KEY_AGAIN")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def end1 ():
    global variable,device
    device
    variable
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    exec1 = "lxterminal  --command=''"
    subprocess
    os.system(exec1)
    time.sleep(2)
    keyboard.type("cat "+device+"_modecold.lircd.conf>>/etc/lirc/lircd.conf")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type("exit")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def end2 ():
    global variable,device
    device
    variable
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    exec1 = "lxterminal  --command=''"
    subprocess
    os.system(exec1)
    time.sleep(2)
    keyboard.type("cat "+device+"_modedry.lircd.conf>>/etc/lirc/lircd.conf")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type("exit")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def end3 ():
    global variable,device
    device
    variable
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    exec1 = "lxterminal  --command=''"
    subprocess
    os.system(exec1)
    time.sleep(2)
    keyboard.type("cat "+device+"_modewind.lircd.conf>>/etc/lirc/lircd.conf")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type("exit")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def end4 ():
    global variable,device
    device
    variable
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    exec1 = "lxterminal  --command=''"
    subprocess
    os.system(exec1)
    time.sleep(2)
    keyboard.type("cat "+device+"_modehot.lircd.conf>>/etc/lirc/lircd.conf")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type("exit")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)



if __name__ == '__main__':
    climRemote()




