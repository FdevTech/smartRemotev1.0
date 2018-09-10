from tkinter import *
from pynput.keyboard import *
import time
import tkinter.messagebox
from pynput.keyboard import *
import time
import remoteGUI
import climRemote
import sqlite3
import subprocess



device=""
variable=""
keyboard = Controller()
def QueryReq (Query,conn): #define fct to read the query and excute it from the object conn wich is a funct cnxdb
    cursor = conn.cursor() #define a cusor for read
    cursor.execute(Query) #for execute the Query
    row = cursor.fetchall() #for the cursor search one value and their is fetchall
    conn.commit()  # to give us the possibility to write on our data base
    cursor.close() # must do it because we defined the the cursor in this function so we must end it
    print(row)
    return row

def cnxdb():
    cnx = None # for initialisation of the variable
    try: # we must use it because their is a possibility to lose the connection with our data base
        cnx = sqlite3.connect('cerist.db')
    except Error as e:
        print(e)
    return cnx

def getAnswer (e1,radioVar) :
    global variable,device

    variable = radioVar.get()
    device =  str(e1.get())
    print(variable)
    print(device)

    if variable=="TV" :
        id=1
        Query = ("insert into device_name(name,type) values ('"+device+"','TV');")  # our first Query
        conn = cnxdb()
        editDB = QueryReq(Query, conn)


    elif variable== "AC" :

        Query = ("insert into device_name(name,type) values ('"+device+"','AC');")  # our first Query
        conn = cnxdb()
        ShowTable = QueryReq(Query, conn)

    return device,variable



def g ( ):
    global device,variable

    print (device)
    print (variable)

def stop():
        
       
    climRemote.climRemote(window,device,variable)



def gui ():

    remoteGUI.remote(window,device,variable)
def getDevice ():
    return device
def getVariable ():
    return  variable
		    

def Record ():

    print(device)
    print(variable)
    if variable == "TV":

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
        keyboard.type(device)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        gui()


    elif variable == "AC":


        stop()




def main():
    window.title('Remote1 Ccntrol')
    window.geometry("500x170+500+100")
    window.resizable(0, 0)
    window.configure(background='grey83')
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

    # window.config(menu=menubar)


    MainFrame = Frame(window,bg='grey83')
    MainFrame.grid(row=0,column=0,padx=8,pady=8)
    lab1=Label(MainFrame,text="device_name", width=15, height=1, bg='grey83', fg='black')
    lab1.grid(row=1 , sticky=E)
    en1=Entry(MainFrame)

    radioFrame= Frame(MainFrame)
    radioFrame.grid(row=3 , column=1)
    var = StringVar()
    radio1 = Radiobutton(radioFrame, text="TV", variable=var, value="TV")
    radio2 = Radiobutton(radioFrame, text="clim", variable=var, value="AC")
    var.set("TV")

    lab2 = Label(MainFrame, text="device_type", width=15, height=1, bg='grey83', fg='black')
    lab2.grid(row=3, sticky=E)
    en1.grid(row=1,column=1)
    radio1.pack(side=LEFT)
    radio2.pack(side=LEFT)


    # bp=tkinter.c3

    #Row One

    buttonOnOff = Button(MainFrame, text='Record', width=15, height=2, bg='red2', fg='white' ,command=Record )
    buttonOnOff.grid(row=0, column=0, padx=5, pady=5)

    buttonSave = Button(MainFrame, text='save', width=15, height=2, bg='red2', fg='white', command=lambda: getAnswer(en1,var) )
    buttonSave.grid(row=0, column=3, padx=5, pady=5)

    # buttonOnOff = Button(MainFrame, text='clim', width=15, height=2, bg='red2', fg='white')
    # buttonOnOff.grid(row=0, column=1, padx=5, pady=5)
    # buttonMedia = Button(MainFrame, text='Menu', width=15, height=2, bg='grey45', fg='white')
    # buttonMedia.grid(row=0, column=2, padx=5, pady=5)

    

if __name__ == '__main__':
    window = Tk()
    main()

    window.mainloop()

