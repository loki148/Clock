import tkinter, time , re, math, threading
from datetime import datetime


win = tkinter.Tk()
win.title('Clock')
canvas = tkinter.Canvas(win,width=400,height=400,bg='#292322',borderwidth = 0, highlightthickness = 0)
#win.overrideredirect(1)
canvas.pack()
print(time.daylight)
print(time.ctime())
print(time.strptime(time.ctime()))
digital = True


def displayer():
    global digital

    if digital == True:
        canvas.config(bg='#292322')
        canvas.delete('all')
    else:
        canvas.delete('all')
        canvas.create_oval(10,10,390,390,fill='#232e21',outline='#232e21',tags='analog')
        canvas.create_oval(20,20,380,380,fill='white',outline='white',stipple='gray25',tags='analog')
        canvas.config(bg='#350792')
        canvas.create_oval(190,190,210,210,fill='black',tags='analog')
        l = 0
        '''for x in range(180):
            canvas.create_line(200,200,math.sin(x)*200+150,50)
            canvas.create_line(200,200,math.sin(x)*(-200)+150,350)
            canvas.create_line(200,200,50,math.cos(x)*200+150)
            canvas.create_line(200,200,350,math.cos(x)*(-200)+150)
            canvas.update()
            print(x)
            print(str(math.sin(x)))''' # sin cos experiment
        canvas.create_line(200,30,200,10,width=5)
        canvas.create_line(390,200,370,200,width=5)
        canvas.create_line(200,390,200,370,width=5)
        canvas.create_line(10,200,30,200,width=5)
        
        '''canvas.create_line(65,65,80,80,width=5)
        canvas.create_line(335,65,320,80,width=5)
        canvas.create_line(335,335,320,320,width=5)
        canvas.create_line(65,335,80,320,width=5)'''
        canvas.create_text(200,50,text='12', font='arial 20 bold')
        canvas.create_text(350,200,text='3', font='arial 20 bold')
        canvas.create_text(200,350,text='6', font='arial 20 bold')
        canvas.create_text(50,200,text='9',font='arial 20 bold')

        
        for x in range(12):
            m = x*30
            if x == 0 or x == 3 or x == 6 or x == 9:
                pass
            else:
                
                canvas.create_text(200,200,text='                                                —',font='arial 20 bold',angle=m)
        for x in range(60):
            n = x*6
            if x == 0 or x == 15 or x == 30 or x == 45:
                print(x)
            elif x == 5 or x == 20 or x == 35 or x == 50:
                print(x)
                
            
            else:
                canvas.create_text(200,200,text='                                                                            —',font='arial 13 ',angle=n)
        updater()



def updater():
    global digital
    pls = time.ctime()
    print(time.ctime())
    # time
    #timeRegex = re.compile(r'\d(\d)?:\d(\d)?:\d(\d)?') # doesnt work
    timeRegex = re.compile(r'(([0-9]+):([0-9]+):([0-9]+))')
    curtimetpl = timeRegex.findall(str(pls))
    
    curtime = curtimetpl[0]
    bbbb = curtime[0]
    print(curtime)
    #curtimetpl1 = timeRegex.search(str(time.ctime()))
    hours = curtime[1]
    minutes = curtime[2]
    seconds = curtime[3]
    print(minutes)
    # date and year
    dateRegex = re.compile(r'\w+\s\d\d')
    curdatetpl = dateRegex.findall(str(time.ctime()))
    curdate = curdatetpl[0]
    yearRegex = re.compile(r'\d\d\d\d\d?')
    curyeartpl = yearRegex.findall(str(time.ctime()))
    curyear = curyeartpl[0]
    # day
    dayRegex = re.compile(r'\w\w\w?')
    curdaytpl = dayRegex.findall(str(time.ctime()))
    curday = curdaytpl[0]
    if digital == True:
        canvas.delete('dg')
        canvas.create_text(200,170,text=bbbb,font='Terminal 40 bold', fill = '#9e9292',tags='dg')
        canvas.create_text(200,220,text=curdate+' '+curyear,font='Terminal 20 bold', fill = '#9e9292',tags='dg')
        canvas.create_text(200,250,text=curday,font='Terminal 20 bold', fill = '#9e9292',tags='dg')

    else:
        canvas.delete('lines')

        sec = int(seconds) * 6
        minute = int(minutes) * 6
        allsec = 90+360-sec
        allminute = 90+360-minute
        if int(hours) > 12:
            hours = int(hours) - 12
        hr = int(hours) * 30
        allhr= 90+360-hr
        print(allhr)
        canvas.create_text(200,200,text='           ———',font='arial 30 bold',angle=allhr,tags='lines')
        canvas.create_text(200,200,text='             ————',font='arial 25 bold',angle=allminute,tags='lines')
        #secodns arm
        canvas.create_text(200,200,text='                  —————',font='arial 25 bold',angle=allsec,tags='lines')
    canvas.update()

    
def perpete():
    updater()
    time.sleep(1)
    perpete()

    
def click(event):
    global digital
    if digital == True:
        digital = False
    else:
        digital = True
    displayer()
canvas.bind_all('<Button-1>',click)
displayer()
t1 = threading.Thread(target=perpete)
t1.start()
win.mainloop()

        
