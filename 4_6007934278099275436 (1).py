from  tkinter  import  *
from  PIL import ImageTk,Image
import tkinter.font as TkFont
from tkinter import ttk
import webbrowser
from sqlite3 import Cursor
import sqlite3
import customtkinter

from sqlite3 import Cursor

import sqlite3
db =sqlite3.connect("Data.db")
cr=db.cursor()
db.commit()
def open1():
    webbrowser.open('https://ikoora.live-kooora.com/')
from  tkinter  import  *
from  PIL import ImageTk,Image
import tkinter.font as TkFont
import customtkinter
from threading import *
import threading
import time


class VerticalScrolledFrame(Frame):
        """A pure Tkinter scrollable frame that actually works!
        * Use the 'interior' attribute to place widgets inside the scrollable frame
        * Construct and pack/place/grid normally
        * This frame only allows vertical scrolling

        """
        def __init__(self, parent, *args, **kw):
            Frame.__init__(self, parent, *args, **kw)

            # create a canvas object and a vertical scrollbar for scrolling it
            vscrollbar = customtkinter.CTkScrollbar(self, orientation=VERTICAL)
            vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
            canvas = Canvas(self, bd=0, highlightthickness=0,
                            yscrollcommand=vscrollbar.set,bg="#463e78")
            canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
            vscrollbar.configure(command=canvas.yview)

            # reset the view
            canvas.xview_moveto(0)
            canvas.yview_moveto(0)

            # create a frame inside the canvas which will be scrolled with it
            self.interior = interior = Frame(canvas)
            interior_id = canvas.create_window(0, 0, window=interior,
                                               anchor=NW)

            # track changes to the canvas and frame width and sync them,
            # also updating the scrollbar
            def _configure_interior(event):
                # update the scrollbars to match the size of the inner frame
                size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
                canvas.config(scrollregion="0 0 %s %s" % size)
                if interior.winfo_reqwidth() != canvas.winfo_width():
                    # update the canvas's width to fit the inner frame
                    canvas.config(width=interior.winfo_reqwidth())
            interior.bind('<Configure>', _configure_interior)

            def _configure_canvas(event):
                if interior.winfo_reqwidth() != canvas.winfo_width():
                    # update the inner frame's width to fill the canvas
                    canvas.itemconfigure(interior_id, width=canvas.winfo_width())
            canvas.bind('<Configure>', _configure_canvas)
class Table:
    # Initialize a constructor
    def __init__(self, gui,list1):
        self.entry=[]
        # An approach for creating the table
        self.list=list1
        self.gui=gui
    def ko(self):
        row = 15
        for i in range(len(self.list)):
                coulmn=0
                for j in range(len(self.list[i])):

                    if i ==0:
                        self.entry.append(customtkinter.CTkEntry(self.gui.interior,bg_color="#f22693", width=150,height=20, text_color='#fffaf7',fg_color='#10af6f',
                                           text_font=('Lato', 16, 'bold')))

                        self.entry[-1].insert(END, self.list[i][j])
                        self.entry[-1].place(x=coulmn,y=row)
                    else:
                        self.entry.append(customtkinter.CTkEntry(self.gui.interior,bg_color="#f22693",width=150,height=20,text_color="#5c236a", fg_color='#ffffff',
                                   text_font=('Lato', 16, '')))
                        self.entry[-1].insert(END, self.list[i][j])

                        self.entry[-1].place(x=coulmn,y=row)
                    coulmn+=150
                row += 30

    def top(self):
       command = threading.Thread(target=self.ko).start()
       self.gui

class cora2():
    global cora1
    global cora3
    def __init__(self, root):
        for widget in root.winfo_children():
            threading.Thread(target=widget.destroy).start()
        self.root = root
        self.root.geometry('1400x700+40+40')
        self.root.title("الدوري الانجليزي الممتاز")

        def open1():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=675&competition_ids%5B%5D=70&team_ids%5B%5D=691')
        def open2():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=682&competition_ids%5B%5D=8&team_ids%5B%5D=667')
        def open3():
            webbrowser.open('https://ar.soccerway.com/matches/1932/03/19/england/premier-league/everton-football-club/huddersfield-town-fc/604139/head2head/')
        def open4():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=680&competition_ids%5B%5D=70&team_ids%5B%5D=698')
        def open5():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=682&competition_ids%5B%5D=70&team_ids%5B%5D=691')
        def open6():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=675&competition_ids%5B%5D=8&team_ids%5B%5D=667')
        def open7():
            webbrowser.open('https://mobile.btolat.com/matches/details/3170807')
        def open8():
            webbrowser.open('https://mobile.btolat.com/matches/details/2618446')

        def open9():
            webbrowser.open('https://mobile.btolat.com/matches/details/2378622')

        def open10():
            webbrowser.open('https://mobile.btolat.com/matches/details/2882262')

        def open11():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=675&competition_ids%5B%5D=70&team_ids%5B%5D=726')

        def open12():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=682&competition_ids%5B%5D=8&team_ids%5B%5D=680')
        def open13():
            webbrowser.open('https://ar.soccerway.com/matches/1929/01/05/england/premier-league/burnley-fc/cardiff-city-fc/606104/head2head/')

        def open14():
            webbrowser.open('https://mobile.btolat.com/matches/details/2882262')

        def open15():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=675&competition_ids%5B%5D=70&team_ids%5B%5D=726')

        def open16():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=682&competition_ids%5B%5D=8&team_ids%5B%5D=680')
        def open17():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=670&competition_ids%5B%5D=260&team_ids%5B%5D=2729')

        def open18():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=711&competition_ids%5B%5D=8&team_ids%5B%5D=667')

        def open19():
            webbrowser.open('https://tribuna.com/ar/match/huddersfield-town-vs-watford/stat/')

        def open20():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=664&competition_ids%5B%5D=8&team_ids%5B%5D=680')
        def open21():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=259&team_ids%5B%5D=2729&competition_ids%5B%5D=8&team_ids%5B%5D=711')

        def open22():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=667&competition_ids%5B%5D=8&team_ids%5B%5D=670')

        def open23():
            webbrowser.open('https://ar.soccerway.com/matches/1950/04/11/england/premier-league/huddersfield-town-fc/newcastle-united-football-club/599574/')

        def open24():
            webbrowser.open('https://mobile.btolat.com/matches/details/2993962')
        def open25():
            webbrowser.open('https://mobile.btolat.com/matches/details/3170636')

        def open26():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=667&competition_ids%5B%5D=8&team_ids%5B%5D=664')

        def open27():
            webbrowser.open('https://mobile.btolat.com/matches/details/2750708')

        def open28():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=711&competition_ids%5B%5D=8&team_ids%5B%5D=680')
        def open29():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=259&team_ids%5B%5D=2729&competition_ids%5B%5D=8&team_ids%5B%5D=664')

        def open30():
            webbrowser.open('https://www.eplworld.com/match/O2zBoY/oatford-vs-folham/headtohead')

        def open31():
            webbrowser.open('https://ar.soccerway.com/matches/2014/08/09/england/championship/huddersfield-town-fc/afc-bournemouth/1704659/')

        def open32():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=670&competition_ids%5B%5D=8&team_ids%5B%5D=680')
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")

        f1 = Frame(root, width=340, height=320, bd=2, bg='#0B4C5F')
        f1.place(x=1055, y=4)

        l1=Label(f1,text='يوم المباراة 15 من إجمالي 30',font=('tajawal',12,'bold'))
        l1.place(x=115,y=10)
        sc=Scrollbar(root,orient=VERTICAL)
        sc.pack(side=RIGHT,fill=Y,expand=False)
        f2=Frame(f1,width=200,height=50,bd=2,bg='#98AFC7')
        f2.place(x=125,y=50)
        l2 = Label(f2, text='توتنهام', font=('tajawal', 10, 'bold'),bg='#98AFC7')
        l2.place(x=135, y=0)
        l3 = Label(f2, text='كارديف', font=('tajawal', 10, 'bold'),bg='#98AFC7')
        l3.place(x=138, y=25)
        bt1 = Button(f1, text='الثلاثاء8/23م1:30', font=('tajawal', 12, 'bold'), command=open1, cursor='mouse',bg='#98AFC7')
        bt1.place(x=4, y=50,width=125,height=51)
        f3 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
        f3.place(x=125, y=105)
        l2 = Label(f3, text='فولهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l2.place(x=135, y=0)
        l3 = Label(f3, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l3.place(x=118, y=25)
        bt2 = Button(f1, text='الثلاثاء8/23م4:00', font=('tajawal', 12, 'bold'), command=open2, cursor='mouse', bg='#98AFC7')
        bt2.place(x=4, y=105, width=125, height=51)
        f4 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
        f4.place(x=125, y=160)
        l2 = Label(f4, text='هدرسفيلد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l2.place(x=125, y=0)
        l3 = Label(f4, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l3.place(x=133, y=25)
        bt2 = Button(f1, text='الثلاثاء8/23م6:30', font=('tajawal', 12, 'bold'), command=open3, cursor='mouse',bg='#98AFC7')
        bt2.place(x=4, y=160, width=125, height=51)

        f5 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
        f5.place(x=125, y=215)
        l4 = Label(f5, text='ولفرهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l4.place(x=110, y=0)
        l5 = Label(f5, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l5.place(x=140, y=25)
        bt3 = Button(f1, text='الثلاثاء8/23م10:00', font=('tajawal', 12, 'bold'), command=open4, cursor='mouse', bg='#98AFC7')
        bt3.place(x=4, y=215, width=125, height=51)

        #####fr2
        f6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        f6.place(x=1055, y=290)
        l6 = Label(f6, text='يوم المباراة 16 من إجمالي 30', font=('tajawal', 12, 'bold'))
        l6.place(x=116, y=10)

        f7 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f7.place(x=125, y=50)
        l7 = Label(f7, text='كارديف', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l7.place(x=135, y=0)
        l8 = Label(f7, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l8.place(x=120, y=25)
        bt4 = Button(f6, text='الاثنين8/29م6:00', font=('tajawal', 12, 'bold'), command=open5, cursor='mouse',bg='#98AFC7')
        bt4.place(x=4, y=51, width=120, height=51)
        f8 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f8.place(x=125, y=105)
        l9 = Label(f8, text='فولهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l9.place(x=135, y=0)
        l10 = Label(f8, text='توتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l10.place(x=135, y=25)
        bt5 = Button(f6, text='الاثنين8/29م9:00', font=('tajawal', 12, 'bold'), command=open6, cursor='mouse',bg='#98AFC7')
        bt5.place(x=4, y=105, width=120, height=51)
        f9 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f9.place(x=125, y=160)
        l11 = Label(f9, text='هدرسفيلد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l11.place(x=120, y=0)
        l12 = Label(f9, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l12.place(x=141, y=25)
        bt6 = Button(f6, text='الاثنين8/29م9:00', font=('tajawal', 12, 'bold'), command=open7, cursor='mouse',bg='#98AFC7')
        bt6.place(x=4, y=160, width=120, height=51)
        f10 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f10.place(x=125, y=215)
        l13 = Label(f10, text='ولفرهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l13.place(x=110, y=0)
        l14 = Label(f10, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l14.place(x=135, y=25)
        bt7 = Button(f6, text='الاثنين8/29م12:00', font=('tajawal', 12, 'bold'), command=open8, cursor='mouse',bg='#98AFC7')
        bt7.place(x=4, y=215, width=120, height=51)
        ##f3
        fr1 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        fr1.place(x=725, y=4)
        lab1 = Label(fr1, text='يوم المباراة 17 من إجمالي 30', font=('tajawal', 12, 'bold'))
        lab1.place(x=115, y=10)
        fr2 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fr2.place(x=125, y=50)
        lab2 = Label(fr2, text='كارديف', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab2.place(x=138, y=0)
        lab3 = Label(fr2, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab3.place(x=138, y=25)
        btn1 = Button(fr1, text='الجمعة9/5م2:00', font=('tajawal', 12, 'bold'), command=open9, cursor='mouse',bg='#98AFC7')
        btn1.place(x=4, y=51, width=120, height=51)
        fr3 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fr3.place(x=125, y=105)
        lab4 = Label(fr3, text='فولهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab4.place(x=138, y=0)
        lab5 = Label(fr3, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab5.place(x=146, y=25)
        btn2 = Button(fr1, text='الجمعة9/5م5:00', font=('tajawal', 12, 'bold'), command=open10, cursor='mouse',bg='#98AFC7')
        btn2.place(x=4, y=105, width=120, height=51)
        fra4 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fra4.place(x=125, y=160)
        lab6 = Label(fra4, text='هدرسفيلد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab6.place(x=125, y=0)
        lab7 = Label(fra4, text='توتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab7.place(x=137, y=25)
        btn3 = Button(fr1, text='الجمعة9/5م10:00', font=('tajawal', 12, 'bold'), command=open11, cursor='mouse',bg='#98AFC7')
        btn3.place(x=4, y=160, width=120, height=51)
        fr5 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fr5.place(x=125, y=215)
        lab8 = Label(fr5, text='ولفرهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab8.place(x=110, y=0)
        lab9 = Label(fr5, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab9.place(x=115, y=25)
        btn4 = Button(fr1, text='الجمعة9/5م1:00', font=('tajawal', 12, 'bold'), command=open12, cursor='mouse',bg='#98AFC7')
        btn4.place(x=4, y=215, width=120, height=51)
        #fr4
        fr6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        fr6.place(x=725, y=290)
        lab10 = Label(fr6, text='يوم المباراة 18 من إجمالي 30', font=('tajawal', 12, 'bold'))
        lab10.place(x=115, y=10)
        fr7 = Frame(fr6, width=200, height=49, bd=2, bg='#98AFC7')
        fr7.place(x=125, y=50)
        lab11 = Label(fr7, text='كارديف', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab11.place(x=140, y=0)
        lab12 = Label(fr7, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab12.place(x=145, y=25)
        btn5 = Button(fr6, text='الخميس9/13م7:00', font=('tajawal', 12, 'bold'), command=open13, cursor='mouse',bg='#98AFC7')
        btn5.place(x=4, y=50, width=130, height=51)
        fr8 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
        fr8.place(x=125, y=105)
        lab13 = Label(fr8, text='فولهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab13.place(x=135, y=0)
        lab14 = Label(fr8, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab14.place(x=135, y=25)
        btn6 = Button(fr6, text='الخميس9/13م9:30', font=('tajawal', 12, 'bold'), command=open14, cursor='mouse',bg='#98AFC7')
        btn6.place(x=4, y=105, width=130, height=51)
        fra5 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
        fra5.place(x=125, y=160)
        lab15 = Label(fra5, text='هدرسفيلد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab15.place(x=120, y=0)
        lab16 = Label(fra5, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab16.place(x=115, y=25)
        btn7 = Button(fr6, text='الخميس9/13م9:30', font=('tajawal', 12, 'bold'), command=open15, cursor='mouse',bg='#98AFC7')
        btn7.place(x=4, y=160, width=130, height=51)
        fr9 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
        fr9.place(x=125, y=215)
        lab17 = Label(fr9, text='ولفرهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab17.place(x=115, y=0)
        lab18 = Label(fr9, text='توتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab18.place(x=135, y=25)
        btn8 = Button(fr6, text='الخميس9/13م12:00', font=('tajawal', 12, 'bold'), command=open16, cursor='mouse',bg='#98AFC7')
        btn8.place(x=4, y=215, width=130, height=51)
        #fr5
        frr1 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        frr1.place(x=395, y=4)
        laa1 = Label(frr1, text='يوم المباراة 19 من إجمالي 30', font=('tajawal', 12, 'bold'))
        laa1.place(x=117, y=10)
        frr2 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr2.place(x=125, y=50)
        laa2 = Label(frr2, text='كارديف', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa2.place(x=140, y=0)
        laa3 = Label(frr2, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa3.place(x=110, y=25)
        btt1 = Button(frr1, text='الثلاثاء9/23م6:00', font=('tajawal', 12, 'bold'), command=open17, cursor='mouse',bg='#98AFC7')
        btt1.place(x=4, y=51, width=120, height=51)
        frr3 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr3.place(x=125, y=105)
        laa4 = Label(frr3, text='فولهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa4.place(x=140, y=0)
        laa5 = Label(frr3, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa5.place(x=135, y=25)
        btt2 = Button(frr1, text='الثلاثاء9/23م9:00', font=('tajawal', 12, 'bold'), command=open18, cursor='mouse',bg='#98AFC7')
        btt2.place(x=4, y=105, width=120, height=51)
        frr4 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr4.place(x=125, y=160)
        laa6 = Label(frr4, text='هدرسفيلد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa6.place(x=125, y=0)
        laa7 = Label(frr4, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa7.place(x=140, y=25)
        btt3 = Button(frr1, text='الثلاثاء9/23م9:00', font=('tajawal', 12, 'bold'), command=open19, cursor='mouse',bg='#98AFC7')
        btt3.place(x=4, y=160, width=120, height=51)
        frr5 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr5.place(x=125, y=215)
        laa8 = Label(frr5, text='ولفرهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa8.place(x=115, y=0)
        laa9 = Label(frr5, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa9.place(x=130, y=25)
        btt4 = Button(frr1, text='الثلاثاء9/23م11:00', font=('tajawal', 12, 'bold'), command=open20, cursor='mouse',bg='#98AFC7')
        btt4.place(x=4, y=215, width=120, height=51)
        #fr6
        frr6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        frr6.place(x=395, y=290)
        laa10 = Label(frr6, text='يوم المباراة 20 من إجمالي 30', font=('tajawal', 12, 'bold'))
        laa10.place(x=116, y=10)
        frr7 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr7.place(x=125, y=50)
        laa11 = Label(frr7, text='كارديف', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa11.place(x=140, y=0)
        laa12 = Label(frr7, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa12.place(x=135, y=25)
        btt5 = Button(frr6, text='السبت10/1م3:00', font=('tajawal', 12, 'bold'), command=open21, cursor='mouse',bg='#98AFC7')
        btt5.place(x=4, y=51, width=120, height=51)
        frr8 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr8.place(x=125, y=105)
        laa13 = Label(frr8, text='فولهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa13.place(x=140, y=0)
        laa14 = Label(frr8, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa14.place(x=110, y=25)
        btt6 = Button(frr6, text='السبت10/1م5:30', font=('tajawal', 12, 'bold'), command=open22, cursor='mouse',bg='#98AFC7')
        btt6.place(x=4, y=105, width=120, height=51)
        frr9 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr9.place(x=125, y=160)
        laa15 = Label(frr9, text='هدرسفيلد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa15.place(x=125, y=0)
        laa16 = Label(frr9, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa16.place(x=130, y=25)
        btt7 = Button(frr6, text='السبت10/1م9:00', font=('tajawal', 12, 'bold'), command=open23, cursor='mouse',bg='#98AFC7')
        btt7.place(x=4, y=160, width=120, height=51)
        frr10 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr10.place(x=125, y=215)
        laa17 = Label(frr10, text='ولفرهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa17.place(x=115, y=0)
        laa18 = Label(frr10, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa18.place(x=135, y=25)
        btt8 = Button(frr6, text='السبت10/1م11:00', font=('tajawal', 12, 'bold'), command=open24, cursor='mouse',bg='#98AFC7')
        btt8.place(x=4, y=215, width=120, height=51)
        #fr7
        fa1 = Frame(root, width=335, height=300, bd=2, bg='#0B4C5F')
        fa1.place(x=58, y=4)
        laa19 = Label(fa1, text='يوم المباراة 21 من إجمالي 30', font=('tajawal', 12, 'bold'))
        laa19.place(x=124, y=10)
        fa2 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa2.place(x=130, y=51)
        laa20 = Label(fa2, text='كارديف', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa20.place(x=138, y=0)
        laa21 = Label(fa2, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa21.place(x=135, y=25)
        btt9 = Button(fa1, text='السبت10/08 7:00م', font=('tajawal', 12, 'bold'), command=open25, cursor='mouse',bg='#98AFC7')
        btt9.place(x=6, y=51, width=135, height=51)
        fa3 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa3.place(x=130, y=105)
        laa22 = Label(fa3, text='فولهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa22.place(x=135, y=0)
        laa23 = Label(fa3, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa23.place(x=130, y=25)
        btt10 = Button(fa1, text='السبت10/08 9:00م', font=('tajawal', 12, 'bold'), command=open26, cursor='mouse',bg='#98AFC7')
        btt10.place(x=6, y=105, width=135, height=51)
        fa4 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa4.place(x=130, y=160)
        laa24 = Label(fa4, text='هدرسفيلد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa24.place(x=125, y=0)
        laa25 = Label(fa4, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa25.place(x=110, y=25)
        btt11 = Button(fa1, text='السبت10/08 9:00م', font=('tajawal', 12, 'bold'), command=open27, cursor='mouse',bg='#98AFC7')
        btt11.place(x=6, y=160, width=135, height=51)
        fa5 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa5.place(x=130, y=215)
        laa26 = Label(fa5, text='ولفرهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa26.place(x=110, y=0)
        laa27 = Label(fa5, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa27.place(x=130, y=25)
        btt12 = Button(fa1, text='السبت10/08 11:30م', font=('tajawal', 12, 'bold'), command=open28, cursor='mouse',bg='#98AFC7')
        btt12.place(x=6, y=215, width=135, height=51)
        frm1 = Frame(root, width=60, height=700, bd=2, bg='#0B4C5F')
        frm1.place(x=0, y=4)
        #fr8
        far = Frame(root, width=335, height=300, bd=2, bg='#0B4C5F')
        far.place(x=58, y=290)
        lar1 = Label(far, text='يوم المباراة 22 من إجمالي 30', font=('tajawal', 12, 'bold'))
        lar1.place(x=122, y=10)
        far1 = Frame(far, width=200, height=50, bd=2, bg='#98AFC7')
        far1.place(x=130, y=51)
        lar2 = Label(far1, text='كارديف', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar2.place(x=133, y=0)
        lar3 = Label(far1, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar3.place(x=128, y=25)
        btr1 = Button(far, text='الاحد10/09 7:00م', font=('tajawal', 12, 'bold'), command=open25, cursor='mouse',bg='#98AFC7')
        btr1.place(x=6, y=51, width=135, height=51)
        far2 = Frame(far, width=200, height=50, bd=2, bg='#98AFC7')
        far2.place(x=130, y=105)
        lar4 = Label(far2, text='فولهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar4.place(x=135, y=0)
        lar5 = Label(far2, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar5.place(x=135, y=25)
        btr2 = Button(far, text='الاحد10/09 9:00م', font=('tajawal', 12, 'bold'), command=open26, cursor='mouse',bg='#98AFC7')
        btr2.place(x=6, y=105, width=135, height=51)
        far3 = Frame(far, width=200, height=50, bd=2, bg='#98AFC7')
        far3.place(x=130, y=160)
        lar6 = Label(far3, text='هدرسفيلد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar6.place(x=123, y=0)
        lar7 = Label(far3, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar7.place(x=130, y=25)
        btr3 = Button(far, text='الاحد10/09 9:00م', font=('tajawal', 12, 'bold'), command=open27, cursor='mouse',bg='#98AFC7')
        btr3.place(x=6, y=160, width=135, height=51)
        far4 = Frame(far, width=200, height=50, bd=2, bg='#98AFC7')
        far4.place(x=130, y=215)
        lar8 = Label(far4, text='ولفرهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar8.place(x=110, y=0)
        lar9 = Label(far4, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar9.place(x=105, y=25)
        btr4 = Button(far, text='الاحد10/09 11:30م', font=('tajawal', 12, 'bold'), command=open28, cursor='mouse',bg='#98AFC7')
        btr4.place(x=6, y=215, width=135, height=51)

        b = customtkinter.CTkButton(root, text="main", width=20, command=main2, bg_color="#0B4C5F")
        b.place(x=1350, y=0)
        b2 = customtkinter.CTkButton(root, text="Next", width=80, command=lambda: next(root), bg_color="#0B4C5F")
        b2.place(x=600, y=560)
        b3 = customtkinter.CTkButton(root, text="back", width=80, command=lambda: back(root), bg_color="#0B4C5F")
        b3.place(x=800, y=560)
        #
        def next(root):
            cora3(root)
        def back(root):
            cora1(root)
        #
        frm3 = Frame(root, width=1323, height=200, bd=2, bg='#0B4C5F')
        frm3.place(x=60, y=590)
class cora3():
    global cora1
    global cora2

    def __init__(self, root):
        for widget in root.winfo_children():
            threading.Thread(target=widget.destroy).start()
        self.root = root
        self.root.geometry('1400x700+40+40')
        self.root.title("الدوري الانجليزي الممتاز")
        self.root.iconbitmap("icon.ico")

        def open1():
            webbrowser.open('https://www.btolat.com/matches/details/2618913')
        def open2():
            webbrowser.open('https://www.btolat.com/matches/details/2618871')
        def open3():
            webbrowser.open('https://www.btolat.com/matches/details/2618833')
        def open4():
            webbrowser.open('https://www.btolat.com/matches/details/2882304')
        def open5():
            webbrowser.open('https://www.btolat.com/matches/details/2618884')
        def open6():
            webbrowser.open('https://www.btolat.com/matches/details/3162626')
        def open7():
            webbrowser.open('https://www.btolat.com/matches/details/2059157')
        def open8():
            webbrowser.open('https://www.btolat.com/matches/details/3162176')

        def open9():
            webbrowser.open('https://www.btolat.com/matches/details/3162286')

        def open10():
            webbrowser.open('https://www.btolat.com/matches/details/3162332')

        def open11():
            webbrowser.open('https://www.btolat.com/matches/details/3162137')

        def open12():
            webbrowser.open('https://www.btolat.com/matches/details/2994164')
        def open13():
            webbrowser.open('https://www.btolat.com/matches/details/2882202')

        def open14():
            webbrowser.open('https://www.btolat.com/matches/details/2618864')

        def open15():
            webbrowser.open('https://www.btolat.com/matches/details/2618908')

        def open16():
            webbrowser.open('https://www.btolat.com/matches/details/2618589')
        def open17():
            webbrowser.open('https://www.btolat.com/matches/details/2882229')

        def open18():
            webbrowser.open('https://www.btolat.com/matches/details/3162191')

        def open19():
            webbrowser.open('https://www.btolat.com/matches/details/3162368')

        def open20():
            webbrowser.open('https://www.btolat.com/matches/details/2994143')
        def open21():
            webbrowser.open('https://www.btolat.com/matches/details/3162337')

        def open22():
            webbrowser.open('https://www.btolat.com/matches/details/3162155')

        def open23():
            webbrowser.open('https://www.btolat.com/matches/details/2994190')

        def open24():
            webbrowser.open('https://www.btolat.com/matches/details/3162149')
        def open25():
            webbrowser.open('https://www.btolat.com/matches/details/2882192')

        def open26():
            webbrowser.open('https://www.btolat.com/matches/details/2882181')

        def open27():
            webbrowser.open('https://www.btolat.com/matches/details/2882547')

        def open28():
            webbrowser.open('https://www.btolat.com/matches/details/2618854')
        def open29():
            webbrowser.open('https://www.btolat.com/matches/details/3162316')

        def open30():
            webbrowser.open('https://www.btolat.com/matches/details/3162380/')

        def open31():
            webbrowser.open('https://www.btolat.com/matches/details/2994172')

        def open32():
            webbrowser.open('https://www.btolat.com/matches/details/3162336')
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")

        f1 = Frame(root, width=340, height=320, bd=2, bg='#0B4C5F')
        f1.place(x=1055, y=4)

        l1=Label(f1,text='يوم المباراة 23 من إجمالي 30',font=('tajawal',12,'bold'))
        l1.place(x=110,y=10)
        sc=Scrollbar(root,orient=VERTICAL)
        sc.pack(side=RIGHT,fill=Y,expand=False)
        f2=Frame(f1,width=200,height=50,bd=2,bg='#98AFC7')
        f2.place(x=125,y=50)
        l2 = Label(f2, text='توتنهام', font=('tajawal', 10, 'bold'),bg='#98AFC7')
        l2.place(x=135, y=0)
        l3 = Label(f2, text='كريستال بالاس', font=('tajawal', 10, 'bold'),bg='#98AFC7')
        l3.place(x=95, y=25)
        bt1 = Button(f1, text='الاربعاء8/24م1:30', font=('tajawal', 12, 'bold'), command=open1, cursor='mouse',bg='#98AFC7')
        bt1.place(x=4, y=50,width=125,height=51)
        f3 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
        f3.place(x=125, y=105)
        l2 = Label(f3, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l2.place(x=115, y=0)
        l3 = Label(f3, text='أرسنال', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l3.place(x=135, y=25)
        bt2 = Button(f1, text='الاربعاء8/24م4:00', font=('tajawal', 12, 'bold'), command=open2, cursor='mouse', bg='#98AFC7')
        bt2.place(x=4, y=105, width=125, height=51)
        f4 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
        f4.place(x=125, y=160)
        l2 = Label(f4, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l2.place(x=133, y=0)
        l3 = Label(f4, text='ليفربول', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l3.place(x=133, y=25)
        bt2 = Button(f1, text='الاربعاء8/24م6:30', font=('tajawal', 12, 'bold'), command=open3, cursor='mouse',bg='#98AFC7')
        bt2.place(x=4, y=160, width=125, height=51)

        f5 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
        f5.place(x=125, y=215)
        l4 = Label(f5, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l4.place(x=140, y=0)
        l5 = Label(f5, text='تشيلسي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l5.place(x=125, y=25)
        bt3 = Button(f1, text='الاربعاء8/24م10:00', font=('tajawal', 12, 'bold'), command=open4, cursor='mouse', bg='#98AFC7')
        bt3.place(x=4, y=215, width=125, height=51)

        #####fr2
        f6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        f6.place(x=1055, y=290)
        l6 = Label(f6, text='يوم المباراة 24 من إجمالي 30', font=('tajawal', 12, 'bold'))
        l6.place(x=113, y=10)

        f7 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f7.place(x=125, y=50)
        l7 = Label(f7, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l7.place(x=105, y=0)
        l8 = Label(f7, text='مان يونايتيد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l8.place(x=112, y=25)
        bt4 = Button(f6, text='الثلاثاء8/30م6:00', font=('tajawal', 12, 'bold'), command=open5, cursor='mouse',bg='#98AFC7')
        bt4.place(x=4, y=51, width=120, height=51)
        f8 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f8.place(x=125, y=105)
        l9 = Label(f8, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l9.place(x=132, y=0)
        l10 = Label(f8, text='برايتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l10.place(x=140, y=25)
        bt5 = Button(f6, text='الثلاثاء8/30م9:00', font=('tajawal', 12, 'bold'), command=open6, cursor='mouse',bg='#98AFC7')
        bt5.place(x=4, y=105, width=120, height=51)
        f9 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f9.place(x=125, y=160)
        l11 = Label(f9, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l11.place(x=140, y=0)
        l12 = Label(f9, text='وست هام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l12.place(x=125, y=25)
        bt6 = Button(f6, text='الثلاثاء8/30م9:00', font=('tajawal', 12, 'bold'), command=open7, cursor='mouse',bg='#98AFC7')
        bt6.place(x=4, y=160, width=120, height=51)
        f10 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f10.place(x=125, y=215)
        l13 = Label(f10, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l13.place(x=135, y=0)
        l14 = Label(f10, text='مان سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l14.place(x=130, y=25)
        bt7 = Button(f6, text='الثلاثاء8/30م12:00', font=('tajawal', 12, 'bold'), command=open8, cursor='mouse',bg='#98AFC7')
        bt7.place(x=4, y=215, width=120, height=51)
        ##f3
        fr1 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        fr1.place(x=725, y=4)
        lab1 = Label(fr1, text='يوم المباراة 25 من إجمالي 30', font=('tajawal', 12, 'bold'))
        lab1.place(x=113, y=10)
        fr2 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fr2.place(x=125, y=50)
        lab2 = Label(fr2, text='توتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab2.place(x=138, y=0)
        lab3 = Label(fr2, text='أرسنال', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab3.place(x=138, y=25)
        btn1 = Button(fr1, text='السبت9/6م2:00', font=('tajawal', 12, 'bold'), command=open9, cursor='mouse',bg='#98AFC7')
        btn1.place(x=4, y=51, width=120, height=51)
        fr3 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fr3.place(x=125, y=105)
        lab4 = Label(fr3, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab4.place(x=120, y=0)
        lab5 = Label(fr3, text='كريستال بالاس', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab5.place(x=95, y=25)
        btn2 = Button(fr1, text='السبت9/6م5:00', font=('tajawal', 12, 'bold'), command=open10, cursor='mouse',bg='#98AFC7')
        btn2.place(x=4, y=105, width=120, height=51)
        fra4 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fra4.place(x=125, y=160)
        lab6 = Label(fra4, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab6.place(x=140, y=0)
        lab7 = Label(fra4, text='تشيلسي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab7.place(x=133, y=25)
        btn3 = Button(fr1, text='السبت9/6م10:00', font=('tajawal', 12, 'bold'), command=open11, cursor='mouse',bg='#98AFC7')
        btn3.place(x=4, y=160, width=120, height=51)
        fr5 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fr5.place(x=125, y=215)
        lab8 = Label(fr5, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab8.place(x=145, y=0)
        lab9 = Label(fr5, text='ليفربول', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab9.place(x=135, y=25)
        btn4 = Button(fr1, text='السبت9/6م1:00', font=('tajawal', 12, 'bold'), command=open12, cursor='mouse',bg='#98AFC7')
        btn4.place(x=4, y=215, width=120, height=51)
        #fr4
        fr6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        fr6.place(x=725, y=290)
        lab10 = Label(fr6, text='يوم المباراة 26 من إجمالي 30', font=('tajawal', 12, 'bold'))
        lab10.place(x=113, y=10)
        fr7 = Frame(fr6, width=200, height=49, bd=2, bg='#98AFC7')
        fr7.place(x=125, y=50)
        lab11 = Label(fr7, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab11.place(x=110, y=0)
        lab12 = Label(fr7, text='برايتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab12.place(x=135, y=25)
        btn5 = Button(fr6, text='الجمعة9/14م7:00', font=('tajawal', 12, 'bold'), command=open13, cursor='mouse',bg='#98AFC7')
        btn5.place(x=4, y=50, width=130, height=51)
        fr8 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
        fr8.place(x=125, y=105)
        lab13 = Label(fr8, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab13.place(x=135, y=0)
        lab14 = Label(fr8, text='مان يونايتيد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab14.place(x=120, y=25)
        btn6 = Button(fr6, text='الجمعة9/14م9:30', font=('tajawal', 12, 'bold'), command=open14, cursor='mouse',bg='#98AFC7')
        btn6.place(x=4, y=105, width=130, height=51)
        fra5 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
        fra5.place(x=125, y=160)
        lab15 = Label(fra5, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab15.place(x=140, y=0)
        lab16 = Label(fra5, text='مان سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab16.place(x=125, y=25)
        btn7 = Button(fr6, text='الجمعة9/14م9:30', font=('tajawal', 12, 'bold'), command=open15, cursor='mouse',bg='#98AFC7')
        btn7.place(x=4, y=160, width=130, height=51)
        fr9 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
        fr9.place(x=125, y=215)
        lab17 = Label(fr9, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab17.place(x=135, y=0)
        lab18 = Label(fr9, text='وست هام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab18.place(x=130, y=25)
        btn8 = Button(fr6, text='الجمعة9/14م12:00', font=('tajawal', 12, 'bold'), command=open16, cursor='mouse',bg='#98AFC7')
        btn8.place(x=4, y=215, width=130, height=51)
        #fr5
        frr1 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        frr1.place(x=395, y=4)
        laa1 = Label(frr1, text='يوم المباراة 27 من إجمالي 30', font=('tajawal', 12, 'bold'))
        laa1.place(x=113, y=10)
        frr2 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr2.place(x=125, y=50)
        laa2 = Label(frr2, text='توتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa2.place(x=140, y=0)
        laa3 = Label(frr2, text='ليفربول', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa3.place(x=140, y=25)
        btt1 = Button(frr1, text='الاربعاء9/24م6:00', font=('tajawal', 12, 'bold'), command=open17, cursor='mouse',bg='#98AFC7')
        btt1.place(x=4, y=51, width=120, height=51)
        frr3 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr3.place(x=125, y=105)
        laa4 = Label(frr3, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa4.place(x=120, y=0)
        laa5 = Label(frr3, text='تشيلسي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa5.place(x=135, y=25)
        btt2 = Button(frr1, text='الاربعاء9/24م9:00', font=('tajawal', 12, 'bold'), command=open18, cursor='mouse',bg='#98AFC7')
        btt2.place(x=4, y=105, width=120, height=51)
        frr4 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr4.place(x=125, y=160)
        laa6 = Label(frr4, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa6.place(x=140, y=0)
        laa7 = Label(frr4, text='كريستال بالاس', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa7.place(x=95, y=25)
        btt3 = Button(frr1, text='الاربعاء9/24م9:00', font=('tajawal', 12, 'bold'), command=open19, cursor='mouse',bg='#98AFC7')
        btt3.place(x=4, y=160, width=120, height=51)
        frr5 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr5.place(x=125, y=215)
        laa8 = Label(frr5, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa8.place(x=145, y=0)
        laa9 = Label(frr5, text='أرسنال', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa9.place(x=140, y=25)
        btt4 = Button(frr1, text='الاربعاء9/24م11:00', font=('tajawal', 12, 'bold'), command=open20, cursor='mouse',bg='#98AFC7')
        btt4.place(x=4, y=215, width=120, height=51)
        #fr6
        frr6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        frr6.place(x=395, y=290)
        laa10 = Label(frr6, text='يوم المباراة 28 من إجمالي 30', font=('tajawal', 12, 'bold'))
        laa10.place(x=113, y=10)
        frr7 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr7.place(x=125, y=50)
        laa11 = Label(frr7, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa11.place(x=105, y=0)
        laa12 = Label(frr7, text='وست هام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa12.place(x=120, y=25)
        btt5 = Button(frr6, text='الأحد10/2م3:00', font=('tajawal', 12, 'bold'), command=open21, cursor='mouse',bg='#98AFC7')
        btt5.place(x=4, y=51, width=120, height=51)
        frr8 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr8.place(x=125, y=105)
        laa13 = Label(frr8, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa13.place(x=130, y=0)
        laa14 = Label(frr8, text='مان سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa14.place(x=123, y=25)
        btt6 = Button(frr6, text='الأحد10/2م5:30', font=('tajawal', 12, 'bold'), command=open22, cursor='mouse',bg='#98AFC7')
        btt6.place(x=4, y=105, width=120, height=51)
        frr9 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr9.place(x=125, y=160)
        laa15 = Label(frr9, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa15.place(x=135, y=0)
        laa16 = Label(frr9, text='مان يونايتيد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa16.place(x=109, y=25)
        btt7 = Button(frr6, text='الأحد10/2م9:00', font=('tajawal', 12, 'bold'), command=open23, cursor='mouse',bg='#98AFC7')
        btt7.place(x=4, y=160, width=120, height=51)
        frr10 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr10.place(x=125, y=215)
        laa17 = Label(frr10, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa17.place(x=130, y=0)
        laa18 = Label(frr10, text='برايتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa18.place(x=140, y=25)
        btt8 = Button(frr6, text='الأحد10/2م11:00', font=('tajawal', 12, 'bold'), command=open24, cursor='mouse',bg='#98AFC7')
        btt8.place(x=4, y=215, width=120, height=51)
        #fr7
        fa1 = Frame(root, width=335, height=300, bd=2, bg='#0B4C5F')
        fa1.place(x=58, y=4)
        laa19 = Label(fa1, text='يوم المباراة 29 من إجمالي 30', font=('tajawal', 12, 'bold'))
        laa19.place(x=122, y=10)
        fa2 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa2.place(x=130, y=51)
        laa20 = Label(fa2, text='توتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa20.place(x=138, y=0)
        laa21 = Label(fa2, text='تشيلسي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa21.place(x=130, y=25)
        btt9 = Button(fa1, text='الأحد10/09 7:00م', font=('tajawal', 12, 'bold'), command=open25, cursor='mouse',bg='#98AFC7')
        btt9.place(x=6, y=51, width=135, height=51)
        fa3 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa3.place(x=130, y=105)
        laa22 = Label(fa3, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa22.place(x=120, y=0)
        laa23 = Label(fa3, text='ليفربول', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa23.place(x=135, y=25)
        btt10 = Button(fa1, text='الأحد10/09 9:00م', font=('tajawal', 12, 'bold'), command=open26, cursor='mouse',bg='#98AFC7')
        btt10.place(x=6, y=105, width=135, height=51)
        fa4 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa4.place(x=130, y=160)
        laa24 = Label(fa4, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa24.place(x=135, y=0)
        laa25 = Label(fa4, text='أرسنال', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa25.place(x=135, y=25)
        btt11 = Button(fa1, text='الأحد10/09 9:00م', font=('tajawal', 12, 'bold'), command=open27, cursor='mouse',bg='#98AFC7')
        btt11.place(x=6, y=160, width=135, height=51)
        fa5 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa5.place(x=130, y=215)
        laa26 = Label(fa5, text='كريستال بالاس', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa26.place(x=95, y=0)
        laa27 = Label(fa5, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa27.place(x=140, y=25)
        btt12 = Button(fa1, text='الأحد10/09 11:30م', font=('tajawal', 12, 'bold'), command=open28, cursor='mouse',bg='#98AFC7')
        btt12.place(x=6, y=215, width=135, height=51)
        frm1 = Frame(root, width=60, height=700, bd=2, bg='#0B4C5F')
        frm1.place(x=0, y=4)
        #fr8
        far = Frame(root, width=335, height=300, bd=2, bg='#0B4C5F')
        far.place(x=58, y=290)
        lar1 = Label(far, text='يوم المباراة 30 من إجمالي 30', font=('tajawal', 12, 'bold'))
        lar1.place(x=120, y=10)
        far1 = Frame(far, width=200, height=50, bd=2, bg='#98AFC7')
        far1.place(x=130, y=51)
        lar2 = Label(far1, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar2.place(x=110, y=0)
        lar3 = Label(far1, text='مان سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar3.place(x=128, y=25)
        btr1 = Button(far, text='الاثنين10/10 7:00م', font=('tajawal', 12, 'bold'), command=open25, cursor='mouse',bg='#98AFC7')
        btr1.place(x=6, y=51, width=135, height=51)
        far2 = Frame(far, width=200, height=50, bd=2, bg='#98AFC7')
        far2.place(x=130, y=105)
        lar4 = Label(far2, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar4.place(x=135, y=0)
        lar5 = Label(far2, text='وست هام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar5.place(x=125, y=25)
        btr2 = Button(far, text='الاثنين10/10 9:00م', font=('tajawal', 12, 'bold'), command=open26, cursor='mouse',bg='#98AFC7')
        btr2.place(x=6, y=105, width=135, height=51)
        far3 = Frame(far, width=200, height=50, bd=2, bg='#98AFC7')
        far3.place(x=130, y=160)
        lar6 = Label(far3, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar6.place(x=140, y=0)
        lar7 = Label(far3, text='برايتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar7.place(x=140, y=25)
        btr3 = Button(far, text='الاثنين10/10 9:00م', font=('tajawal', 12, 'bold'), command=open27, cursor='mouse',bg='#98AFC7')
        btr3.place(x=6, y=160, width=135, height=51)
        far4 = Frame(far, width=200, height=50, bd=2, bg='#98AFC7')
        far4.place(x=130, y=215)
        lar8 = Label(far4, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar8.place(x=132, y=0)
        lar9 = Label(far4, text='مان يونايتيد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lar9.place(x=115, y=25)
        btr4 = Button(far, text='الاثنين10/10 11:30م', font=('tajawal', 12, 'bold'), command=open28, cursor='mouse',bg='#98AFC7')
        btr4.place(x=6, y=215, width=135, height=51)

        b = customtkinter.CTkButton(root, text="main", width=20, command=main2, bg_color="#0B4C5F")
        b.place(x=1350, y=0)
        b3 = customtkinter.CTkButton(root, text="back", width=80, command=lambda:matches(root), bg_color="#0B4C5F")
        b3.place(x=800, y=560)
        def next(root):
            cora3(root)
        def back(root):
            cora2(root)
        frm3 = Frame(root, width=1323, height=200, bd=2, bg='#0B4C5F')
        frm3.place(x=60, y=590)

class cora1():
    global cora3
    global cora2
    def __init__(self, root):
        for widget in root.winfo_children():
            threading.Thread(target=widget.destroy).start()
        self.root = root
        self.root.geometry('1400x700+40+40')
        self.root.title("الدوري الانجليزي الممتاز")

        def open1():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=682&competition_ids%5B%5D=8&team_ids%5B%5D=675')
        def open2():
            webbrowser.open('https://www.btolat.com/matches/details/2618724')
        def open3():
            webbrowser.open('https://www.scores.belgoal.com/match/10333118/h2h')
        def open4():
            webbrowser.open('https://www.btolat.com/matches/details/2618888')
        def open5():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=674&competition_ids%5B%5D=8&team_ids%5B%5D=675')
        def open6():
            webbrowser.open('https://www.btolat.com/matches/details/2618543')
        def open7():
            webbrowser.open('https://www.btolat.com/matches/details/2994211')
        def open8():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=711&competition_ids%5B%5D=8&team_ids%5B%5D=664')

        def open9():
            webbrowser.open('https://www.alremontada.com/h2h/%D8%A8%D9%8A%D8%B1%D9%86%D9%84%D9%8A-%D9%88%D8%AA%D9%88%D8%AA%D9%86%D9%87%D8%A7%D9%85?fixture_id=157296')

        def open10():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=674&competition_ids%5B%5D=8&team_ids%5B%5D=682')

        def open11():
            webbrowser.open('https://scores.belgoal.com/match/11867514/h2h')

        def open12():
            webbrowser.open('https://www.yallakora.com/epl/2596/Match/66122/%D9%88%D8%A7%D8%AA%D9%81%D9%88%D8%B1%D8%AF-%D8%A8%D9%88%D8%B1%D9%86%D9%85%D9%88%D8%AB-%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84%D8%A5%D9%86%D8%AC%D9%84%D9%8A%D8%B2%D9%8A')
        def open13():
            webbrowser.open('https://www.alremontada.com/h2h/%D8%AA%D9%88%D8%AA%D9%86%D9%87%D8%A7%D9%85-%D9%88%D8%B3%D8%A7%D9%88%D8%AB%D9%87%D8%A7%D9%85%D8%A8%D8%AA%D9%88%D9%86?fixture_id=157083')

        def open14():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=711&competition_ids%5B%5D=8&team_ids%5B%5D=682')

        def open15():
            webbrowser.open('https://www.btolat.com/matches/details/2734264')

        def open16():
            webbrowser.open('https://www.btolat.com/matches/details/2882095')
        def open17():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=711&competition_ids%5B%5D=8&team_ids%5B%5D=675')

        def open18():
            webbrowser.open('https://scores.belgoal.com/match/10332788/h2h')

        def open19():
            webbrowser.open('https://www.btolat.com/matches/details/2994117')

        def open20():
            webbrowser.open('https://www.alremontada.com/h2h/%D8%A8%D9%8A%D8%B1%D9%86%D9%84%D9%8A-%D9%88%D9%88%D8%A7%D8%AA%D9%81%D9%88%D8%B1%D8%AF?fixture_id=157143')
        def open21():
            webbrowser.open('https://www.alremontada.com/h2h/%D8%AA%D9%88%D8%AA%D9%86%D9%87%D8%A7%D9%85-%D9%88%D9%88%D8%A7%D8%AA%D9%81%D9%88%D8%B1%D8%AF?fixture_id=157103')

        def open22():
            webbrowser.open('https://scores.belgoal.com/match/10333095/h2h')

        def open23():
            webbrowser.open('https://www.alremontada.com/h2h/%D8%A5%D9%8A%D9%81%D8%B1%D8%AA%D9%88%D9%86-%D9%88%D8%B3%D8%A7%D9%88%D8%AB%D9%87%D8%A7%D9%85%D8%A8%D8%AA%D9%88%D9%86?fixture_id=157350')

        def open24():
            webbrowser.open('https://www.yallakora.com/epl/2596/Match/67402/%D8%A8%D9%88%D8%B1%D9%86%D9%85%D9%88%D8%AB-%D8%A8%D9%8A%D8%B1%D9%86%D9%84%D9%8A--%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84%D8%A5%D9%86%D8%AC%D9%84%D9%8A%D8%B2%D9%8A')
        def open25():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=664&competition_ids%5B%5D=8&team_ids%5B%5D=675')

        def open26():
            webbrowser.open('https://www.alremontada.com/h2h/%D9%88%D8%A7%D8%AA%D9%81%D9%88%D8%B1%D8%AF-%D9%88%D9%84%D9%8A%D8%B3%D8%AA%D8%B1-%D8%B3%D9%8A%D8%AA%D9%8A?fixture_id=157157')

        def open27():
            webbrowser.open('https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=711&competition_ids%5B%5D=8&team_ids%5B%5D=674')

        def open28():
            webbrowser.open('https://www.btolat.com/matches/details/2618798')
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")

        f1 = Frame(root, width=340, height=320, bd=2, bg='#0B4C5F')
        f1.place(x=1055, y=4)

        l1=Label(f1,text='يوم المباراة 8 من إجمالي 30',font=('tajawal',12,'bold'))
        l1.place(x=119,y=10)
        sc=Scrollbar(root,orient=VERTICAL)
        sc.pack(side=RIGHT,fill=Y,expand=False)
        f2=Frame(f1,width=200,height=50,bd=2,bg='#98AFC7')
        f2.place(x=125,y=50)
        l2 = Label(f2, text='توتنهام', font=('tajawal', 10, 'bold'),bg='#98AFC7')
        l2.place(x=130, y=0)
        l3 = Label(f2, text='ليستر سيتي', font=('tajawal', 10, 'bold'),bg='#98AFC7')
        l3.place(x=115, y=25)
        bt1 = Button(f1, text='الاثنين8/22م1:30', font=('tajawal', 12, 'bold'), command=open1, cursor='mouse',bg='#98AFC7')
        bt1.place(x=4, y=51,width=120,height=51)
        f3 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
        f3.place(x=125, y=105)
        l2 = Label(f3, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l2.place(x=135, y=0)
        l3 = Label(f3, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l3.place(x=140, y=25)
        bt2 = Button(f1, text='الاثنين8/22م4:00', font=('tajawal', 12, 'bold'), command=open2, cursor='mouse', bg='#98AFC7')
        bt2.place(x=4, y=105, width=120, height=51)
        f4 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
        f4.place(x=125, y=160)
        l2 = Label(f4, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l2.place(x=110, y=0)
        l3 = Label(f4, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l3.place(x=130, y=25)
        bt2 = Button(f1, text='الاثنين8/22م6:30', font=('tajawal', 12, 'bold'), command=open3, cursor='mouse',bg='#98AFC7')
        bt2.place(x=4, y=160, width=120, height=51)

        f5 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
        f5.place(x=125, y=215)
        l4 = Label(f5, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l4.place(x=135, y=0)
        l5 = Label(f5, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l5.place(x=130, y=25)
        bt3 = Button(f1, text='الاثنين8/22م10:00', font=('tajawal', 12, 'bold'), command=open4, cursor='mouse', bg='#98AFC7')
        bt3.place(x=4, y=215, width=120, height=51)

        #####fr2
        f6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        f6.place(x=1055, y=290)
        l6 = Label(f6, text='يوم المباراة 9 من إجمالي 30', font=('tajawal', 12, 'bold'))
        l6.place(x=121, y=10)

        f7 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f7.place(x=125, y=50)
        l7 = Label(f7, text='توتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l7.place(x=133, y=0)
        l8 = Label(f7, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l8.place(x=135, y=25)
        bt4 = Button(f6, text='الاحد8/28م6:00', font=('tajawal', 12, 'bold'), command=open5, cursor='mouse',bg='#98AFC7')
        bt4.place(x=4, y=51, width=120, height=51)
        f8 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f8.place(x=125, y=105)
        l9 = Label(f8, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l9.place(x=120, y=0)
        l10 = Label(f8, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l10.place(x=140, y=25)
        bt5 = Button(f6, text='الاحد8/28م9:00', font=('tajawal', 12, 'bold'), command=open6, cursor='mouse',bg='#98AFC7')
        bt5.place(x=4, y=105, width=120, height=51)
        f9 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f9.place(x=125, y=160)
        l11 = Label(f9, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l11.place(x=110, y=0)
        l12 = Label(f9, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l12.place(x=141, y=25)
        bt6 = Button(f6, text='الاحد8/28م9:00', font=('tajawal', 12, 'bold'), command=open7, cursor='mouse',bg='#98AFC7')
        bt6.place(x=4, y=160, width=120, height=51)
        f10 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
        f10.place(x=125, y=215)
        l13 = Label(f10, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l13.place(x=135, y=0)
        l14 = Label(f10, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        l14.place(x=135, y=25)
        bt7 = Button(f6, text='الاحد8/28م12:00', font=('tajawal', 12, 'bold'), command=open8, cursor='mouse',bg='#98AFC7')
        bt7.place(x=4, y=215, width=120, height=51)
        ##f3
        fr1 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        fr1.place(x=725, y=4)
        lab1 = Label(fr1, text='يوم المباراة 10 من إجمالي 30', font=('tajawal', 12, 'bold'))
        lab1.place(x=119, y=10)
        fr2 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fr2.place(x=125, y=50)
        lab2 = Label(fr2, text='توتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab2.place(x=130, y=0)
        lab3 = Label(fr2, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab3.place(x=141, y=25)
        btn1 = Button(fr1, text='الخميس9/4م2:00', font=('tajawal', 12, 'bold'), command=open9, cursor='mouse',bg='#98AFC7')
        btn1.place(x=4, y=51, width=120, height=51)
        fr3 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fr3.place(x=125, y=105)
        lab4 = Label(fr3, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab4.place(x=115, y=0)
        lab5 = Label(fr3, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab5.place(x=135, y=25)
        btn2 = Button(fr1, text='الخميس9/4م5:00', font=('tajawal', 12, 'bold'), command=open10, cursor='mouse',bg='#98AFC7')
        btn2.place(x=4, y=105, width=120, height=51)
        fra4 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fra4.place(x=125, y=160)
        lab6 = Label(fra4, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab6.place(x=110, y=0)
        lab7 = Label(fra4, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab7.place(x=130, y=25)
        btn3 = Button(fr1, text='الخميس9/4م10:00', font=('tajawal', 12, 'bold'), command=open11, cursor='mouse',bg='#98AFC7')
        btn3.place(x=4, y=160, width=120, height=51)
        fr5 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
        fr5.place(x=125, y=215)
        lab8 = Label(fr5, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab8.place(x=135, y=0)
        lab9 = Label(fr5, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab9.place(x=139, y=25)
        btn4 = Button(fr1, text='الخميس9/4م1:00', font=('tajawal', 12, 'bold'), command=open12, cursor='mouse',bg='#98AFC7')
        btn4.place(x=4, y=215, width=120, height=51)
        #fr4
        fr6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        fr6.place(x=725, y=290)
        lab10 = Label(fr6, text='يوم المباراة 11 من إجمالي 30', font=('tajawal', 12, 'bold'))
        lab10.place(x=120, y=10)
        fr7 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
        fr7.place(x=125, y=50)
        lab11 = Label(fr7, text='توتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab11.place(x=135, y=0)
        lab12 = Label(fr7, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab12.place(x=110, y=25)
        btn5 = Button(fr6, text='الاربعاء9/12م7:00', font=('tajawal', 12, 'bold'), command=open13, cursor='mouse',bg='#98AFC7')
        btn5.place(x=4, y=51, width=120, height=51)
        fr8 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
        fr8.place(x=125, y=105)
        lab13 = Label(fr8, text='ليستر سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab13.place(x=118, y=0)
        lab14 = Label(fr8, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab14.place(x=130, y=25)
        btn6 = Button(fr6, text='الاربعاء9/12م9:30', font=('tajawal', 12, 'bold'), command=open14, cursor='mouse',bg='#98AFC7')
        btn6.place(x=4, y=105, width=120, height=51)
        fra5 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
        fra5.place(x=125, y=160)
        lab15 = Label(fra5, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab15.place(x=139, y=0)
        lab16 = Label(fra5, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab16.place(x=141, y=25)
        btn7 = Button(fr6, text='الاربعاء9/12م9:30', font=('tajawal', 12, 'bold'), command=open15, cursor='mouse',bg='#98AFC7')
        btn7.place(x=4, y=160, width=120, height=51)
        fr9 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
        fr9.place(x=125, y=215)
        lab17 = Label(fr9, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab17.place(x=145, y=0)
        lab18 = Label(fr9, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        lab18.place(x=135, y=25)
        btn8 = Button(fr6, text='الاربعاء9/12م12:00', font=('tajawal', 12, 'bold'), command=open16, cursor='mouse',bg='#98AFC7')
        btn8.place(x=4, y=215, width=120, height=51)
        #fr5
        frr1 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        frr1.place(x=395, y=4)
        laa1 = Label(frr1, text='يوم المباراة 12 من إجمالي 30', font=('tajawal', 12, 'bold'))
        laa1.place(x=117, y=10)
        frr2 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr2.place(x=125, y=50)
        laa2 = Label(frr2, text='توتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa2.place(x=135, y=0)
        laa3 = Label(frr2, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa3.place(x=130, y=25)
        btt1 = Button(frr1, text='الاثنين9/22م6:00', font=('tajawal', 12, 'bold'), command=open17, cursor='mouse',bg='#98AFC7')
        btt1.place(x=4, y=51, width=120, height=51)
        frr3 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr3.place(x=125, y=105)
        laa4 = Label(frr3, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa4.place(x=117, y=0)
        laa5 = Label(frr3, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa5.place(x=110, y=25)
        btt2 = Button(frr1, text='الاثنين9/22م9:00', font=('tajawal', 12, 'bold'), command=open18, cursor='mouse',bg='#98AFC7')
        btt2.place(x=4, y=105, width=120, height=51)
        frr4 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr4.place(x=125, y=160)
        laa6 = Label(frr4, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa6.place(x=136, y=0)
        laa7 = Label(frr4, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa7.place(x=130, y=25)
        btt3 = Button(frr1, text='الاثنين9/22م9:00', font=('tajawal', 12, 'bold'), command=open19, cursor='mouse',bg='#98AFC7')
        btt3.place(x=4, y=160, width=120, height=51)
        frr5 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
        frr5.place(x=125, y=215)
        laa8 = Label(frr5, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa8.place(x=136, y=0)
        laa9 = Label(frr5, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa9.place(x=145, y=25)
        btt4 = Button(frr1, text='الاثنين9/22م11:00', font=('tajawal', 12, 'bold'), command=open20, cursor='mouse',bg='#98AFC7')
        btt4.place(x=4, y=215, width=120, height=51)
        #fr6
        frr6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
        frr6.place(x=395, y=290)
        laa10 = Label(frr6, text='يوم المباراة 13 من إجمالي 30', font=('tajawal', 12, 'bold'))
        laa10.place(x=114, y=10)
        frr7 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr7.place(x=125, y=50)
        laa11 = Label(frr7, text='تنوتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa11.place(x=131, y=0)
        laa12 = Label(frr7, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa12.place(x=135, y=25)
        btt5 = Button(frr6, text='الثلاثاء9/30م3:00', font=('tajawal', 12, 'bold'), command=open21, cursor='mouse',bg='#98AFC7')
        btt5.place(x=4, y=51, width=120, height=51)
        frr8 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr8.place(x=125, y=105)
        laa13 = Label(frr8, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa13.place(x=115, y=0)
        laa14 = Label(frr8, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa14.place(x=130, y=25)
        btt6 = Button(frr6, text='الثلاثاء9/30م5:30', font=('tajawal', 12, 'bold'), command=open22, cursor='mouse',bg='#98AFC7')
        btt6.place(x=4, y=105, width=120, height=51)
        frr9 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr9.place(x=125, y=160)
        laa15 = Label(frr9, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa15.place(x=137, y=0)
        laa16 = Label(frr9, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa16.place(x=105, y=25)
        btt7 = Button(frr6, text='الثلاثاء9/30م9:00', font=('tajawal', 12, 'bold'), command=open23, cursor='mouse',bg='#98AFC7')
        btt7.place(x=4, y=160, width=120, height=51)
        frr10 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
        frr10.place(x=125, y=215)
        laa17 = Label(frr10, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa17.place(x=140, y=0)
        laa18 = Label(frr10, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa18.place(x=130, y=25)
        btt8 = Button(frr6, text='الثلاثاء9/30م11:00', font=('tajawal', 12, 'bold'), command=open24, cursor='mouse',bg='#98AFC7')
        btt8.place(x=4, y=215, width=120, height=51)
        #fr7
        fa1 = Frame(root, width=335, height=300, bd=2, bg='#0B4C5F')
        fa1.place(x=58, y=4)
        laa19 = Label(fa1, text='يوم المباراة 14 من إجمالي 30', font=('tajawal', 12, 'bold'))
        laa19.place(x=124, y=10)
        fa2 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa2.place(x=130, y=51)
        laa20 = Label(fa2, text='توتنهام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa20.place(x=133, y=0)
        laa21 = Label(fa2, text='نيوكاسل', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa21.place(x=128, y=25)
        btt9 = Button(fa1, text='الجمعة10/07 7:00م', font=('tajawal', 12, 'bold'), command=open25, cursor='mouse',bg='#98AFC7')
        btt9.place(x=6, y=51, width=135, height=51)
        fa3 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa3.place(x=130, y=105)
        laa22 = Label(fa3, text='ليسترسيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa22.place(x=115, y=0)
        laa23 = Label(fa3, text='واتفورد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa23.place(x=130, y=25)
        btt10 = Button(fa1, text='الجمعة10/07 9:00م', font=('tajawal', 12, 'bold'), command=open26, cursor='mouse',bg='#98AFC7')
        btt10.place(x=6, y=105, width=135, height=51)
        fa4 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa4.place(x=130, y=160)
        laa24 = Label(fa4, text='ايفرتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa24.place(x=135, y=0)
        laa25 = Label(fa4, text='بورنموث', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa25.place(x=130, y=25)
        btt11 = Button(fa1, text='الجمعة10/07 9:00م', font=('tajawal', 12, 'bold'), command=open27, cursor='mouse',bg='#98AFC7')
        btt11.place(x=6, y=160, width=135, height=51)
        fa5 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
        fa5.place(x=130, y=215)
        laa26 = Label(fa5, text='بيرنلي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa26.place(x=140, y=0)
        laa27 = Label(fa5, text='ساوثهامبتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
        laa27.place(x=110, y=25)
        btt12 = Button(fa1, text='الجمعة10/07 11:30م', font=('tajawal', 12, 'bold'), command=open28, cursor='mouse',bg='#98AFC7')
        btt12.place(x=6, y=215, width=135, height=51)
        frm1 = Frame(root, width=60, height=700, bd=2, bg='#0B4C5F')
        frm1.place(x=0, y=4)
        frm2 = Frame(root, width=333, height=500, bd=2, bg='#0B4C5F')
        frm2.place(x=60, y=280)
        b = customtkinter.CTkButton(root, text="main", width=20, command=main2, bg_color="#98AFC7")
        b.place(x=1350, y=0)
        b2 = customtkinter.CTkButton(root, text="Next", width=80, command=lambda: next(root), bg_color="#0B4C5F")
        b2.place(x=600, y=570)
        b3 = customtkinter.CTkButton(root, text="back", width=80, command=lambda:matches(root), bg_color="#0B4C5F")
        b3.place(x=800, y=570)
        def next(root):
            cora2(root)
        def back(root):
            cora1(root)
        frm3 = Frame(root, width=1323, height=200, bd=2, bg='#0B4C5F')
        frm3.place(x=60, y=590)

class programmes():
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x500')
        self.root.title("الدوري الانجليزي الممتاز")
        self.root.iconbitmap("icon.ico")
        for widget in root.winfo_children():
            threading.Thread(target=widget.destroy).start()
        photo1 = ImageTk.PhotoImage(Image.open(r'k19.jpg').resize((800, 500)))
        mad = customtkinter.CTkLabel(root, image=photo1, width=800, height=500)
        mad.pack()
        l1 = Label(root, text=':قام ببرمجة هذا المشروع', font=('tajawal', 12, 'bold'))
        l1.place(x=600, y=10)
        l2 = Label(root, text='المهندس: محمد صبري محمود شهاب الدين', font=('tajawal', 12, 'bold'),fg='yellow',bg='#0B4C5F')
        l2.place(x=465, y=50)
        l2 = Label(root, text='المهندس: محمد أحمد محمد امام', font=('tajawal', 12, 'bold'), fg='yellow',bg='#0B4C5F')
        l2.place(x=539, y=90)
        l2 = Label(root, text='المهندسة: فاطمة ابراهيم كامل ابراهيم', font=('tajawal', 12, 'bold'), fg='yellow', bg='#0B4C5F')
        l2.place(x=494, y=130)
        l2 = Label(root, text='المهندس: محمد طارق أمين اسماعيل', font=('tajawal', 12, 'bold'), fg='yellow', bg='#0B4C5F')
        l2.place(x=507, y=170)
        l2 = Label(root, text='المهندسة: لقاء محمد عبدالله عبدالسلام', font=('tajawal', 12, 'bold'), fg='yellow', bg='#0B4C5F')
        l2.place(x=488, y=210)
        l2 = Label(root, text='المهندس: محمد بهجت عبدالخالق بيومي', font=('tajawal', 12, 'bold'), fg='yellow', bg='#0B4C5F')
        l2.place(x=488, y=250)
        b = customtkinter.CTkButton(root, text="Back", width=20,command=main2)
        b.place(x=700,y=400)



# http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame

def leauge():
        global var
        for widget in var.winfo_children():
            threading.Thread(target=widget.destroy).start()
        var.update()
        var.geometry('800x600')
        var.update()
        class Table:
            # Initialize a constructor
            def __init__(self, gui,lis):
                self.entry = []
                # An approach for creating the table
                lis=[("team name",'common name',"matches","points" )]+lis
                for i in range(20):
                    for j in range(4):
                        print(i)
                        w = 0
                        if i == 0:
                            self.entry.append(customtkinter.CTkEntry(gui.interior, width=200, text_color='#ffffff',
                                                                     fg_color='#12b474',
                                                                     text_font=('Lato', 16, 'bold')))

                            self.entry[-1].insert(END, lis[i][j])
                            self.entry[-1].grid(column=j, row=i + 11)
                        else:
                            self.entry.append(customtkinter.CTkEntry(gui.interior, width=200, text_color="#2d2a47",
                                                                     bg_color="#2d2a47", fg_color='#ffffff',
                                                                     text_font=('Lato', 16, '')))
                            self.entry[-1].insert(END, lis[i][j])

                            self.entry[-1].grid(column=j, row=i + 11)
        # find total number of rows and
        # columns in list

        # create root window
        f1 = customtkinter.CTkFrame(var,bg_color="#10af6f",fg_color="#10af6f")
        f1.pack(fill='x')
        image = ImageTk.PhotoImage(
            Image.open(r"k9.jpeg").resize((800, 120), Image.ANTIALIAS))
        l = []
        l.append(customtkinter.CTkLabel(f1, image=image, fg_color="white", bg_color='white', width=800, height=120))
        l[-1].grid(column=0, row=0)
        f = VerticalScrolledFrame(var)
        f.pack(fill='both', expand=True)
        teams = cr.execute("SELECT * from Teams2 order by points DESC").fetchall()
        print(teams)
        table = Table(f,teams)
        b = customtkinter.CTkButton(f1, text="Back", width=20,command=main2)
        b.place(x=750,y=0)
        var.update()
        var.mainloop()
def page_player():
    global var
    for widget in var.winfo_children():
        threading.Thread(target=widget.destroy).start()
    var.update()
    var.geometry('860x600')
    var.update()

    # here infortion of leauge us load

    # create root window
    f1=customtkinter.CTkFrame(var)
    f1.pack(fill='x')
    image=ImageTk.PhotoImage(Image.open(r"k13.jpeg").resize((var.winfo_width(),var.winfo_height() ),Image.ANTIALIAS) )
    l = []
    l.append(customtkinter.CTkLabel(f1,image=image,fg_color="white",bg_color='white',width=var.winfo_width(),height=var.winfo_height() ))
    l[-1].grid(column=0, row=0)
    b=customtkinter.CTkButton(f1,text="Back",width=20,command=main2,bg_color="#f22693")
    b.grid(column=0,row=0,sticky=NE)
    s2=customtkinter.StringVar()
    c1=customtkinter.CTkComboBox(f1,width=150,variable=s2,dropdown_color="#463e78",fg_color="#463e78",values=["full_name","age","birthday","position","Current_Club","nationality","appearances_overall","goals_overall","assists_overall"],text_font=('Lato', 16, ''))
    c1.place(x=450,y=300)
    e1=customtkinter.CTkEntry(f1,width=150 ,fg_color="#463e78",placeholder_text='Enter name',text_font=('Lato', 16, ''))
    e1.place(x=150,y=300)
    b2=customtkinter.CTkButton(f1,fg_color="#b91f16",bg_color="#2e436b",command=lambda:page2_players(s2.get(),e1.get()),text="Search",width=60,text_font=('Lato', 16, ''))
    b2.place(x=350,y=400)
    def w(str1):
        e1.configure(placeholder_text="Enter "+str1)

    s2.set('full_name')
    s2.trace( 'w',lambda x,r,t: w(s2.get()))
    var.mainloop()
def page2_players(choose,text):
    print(choose,text)
    global var
    for widget in var.winfo_children():
        threading.Thread(target=widget.destroy).start()
    var.geometry('860x600')
    var.update()

    f3=VerticalScrolledFrame(var)

    f3.pack(expand=True,fill='both')

    #here we pu
    teams=list(cr.execute(f"SELECT *  from players WHERE {choose}  LIKE '%{text}%'"))

    def o():
        from tkinter import ttk
        style=ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#c9c4cd",
                        foreground="black",
                        rowheight=55,
                        fieldbackground="#463e78")
        # Change selected color:
        style.map("Treeview",
                  background=[('selected', '#463e78')])
        style.configure("Treeview.Heading", foreground='white',background="#463e78")  # <----
        tree = ttk.Treeview(f3.interior, style="Treeview",column=("full_name","age","birthday","position","Current_Club","nationality","appearances_overall","goals_overall","assists_overall"), show='headings', height=50)

        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Name")
        tree.column("# 2", anchor=CENTER,width=70)
        tree.heading("# 2", text="age")
        tree.column("# 3", anchor=CENTER,width=70)
        tree.heading("# 3", text="birthday")
        tree.column("# 4", anchor=CENTER,width=70)
        tree.heading("# 4", text="position")
        tree.column("# 5", anchor=CENTER,width=90)
        tree.heading("# 5", text="Current_Club")
        tree.column("# 6", anchor=CENTER,width=70)
        tree.heading("# 6", text="nationality")
        tree.column("# 7", anchor=CENTER,width=70)
        tree.heading("# 7", text="appearances_overall")
        tree.column("# 8", anchor=CENTER,width=70)
        tree.heading("# 8", text="goals_overall")
        tree.column("# 9", anchor=CENTER,width=70)
        tree.heading("# 9", text="assists_overall")
        for i in list(teams)[:50]:
            print(i)
            tree.insert('', 'end', text="1", values=i)
        tree.grid(column=0,row=0)
    command = threading.Thread(target=o).start()
    b = customtkinter.CTkButton(f3.interior, text="Back", width=20, command=page_player, bg_color="white")
    b.place(x=800,y=0)
    var.update()
    var.configure(bg="#f22693")
    var.mainloop()
  #here we put the data of player

var = customtkinter.CTk()
var.geometry('1000x600')
var.config(background='#0B2F3A')
var.title("الدوري الانجليزي الممتاز")
var.iconbitmap(r'Premier_League-Logo.wine.png')
def add_matches():

    global var
    for widget in var.winfo_children():
        threading.Thread(target=widget.destroy).start()
    var.update()
    var.geometry('860x600')
    var.update()
    l1=['Arsenal', 'Tottenham Hotspur', 'Manchester City', 'Leicester City', 'Crystal Palace', 'Everton', 'Burnley', 'Southampton', 'AFC Bournemouth', 'Manchester United', 'Liverpool', 'Chelsea', 'West Ham United', 'Watford', 'Newcastle United', 'Cardiff City', 'Fulham', 'Brighton & Hove Albion', 'Huddersfield Town', 'Wolverhampton Wanderers']

    l2=['Arsenal', 'Tottenham Hotspur', 'Manchester City', 'Leicester City', 'Crystal Palace', 'Everton', 'Burnley', 'Southampton', 'AFC Bournemouth', 'Manchester United', 'Liverpool', 'Chelsea', 'West Ham United', 'Watford', 'Newcastle United', 'Cardiff City', 'Fulham', 'Brighton & Hove Albion', 'Huddersfield Town', 'Wolverhampton Wanderers']

    # here infortion of leauge us load
    l12 =['Arsenal', 'Tottenham Hotspur', 'Manchester City', 'Leicester City', 'Crystal Palace', 'Everton', 'Burnley', 'Southampton', 'AFC Bournemouth', 'Manchester United', 'Liverpool', 'Chelsea', 'West Ham United', 'Watford', 'Newcastle United', 'Cardiff City', 'Fulham', 'Brighton & Hove Albion', 'Huddersfield Town', 'Wolverhampton Wanderers']


    l22 = ['Arsenal', 'Tottenham Hotspur', 'Manchester City', 'Leicester City', 'Crystal Palace', 'Everton', 'Burnley', 'Southampton', 'AFC Bournemouth', 'Manchester United', 'Liverpool', 'Chelsea', 'West Ham United', 'Watford', 'Newcastle United', 'Cardiff City', 'Fulham', 'Brighton & Hove Albion', 'Huddersfield Town', 'Wolverhampton Wanderers']


    # create root window
    print(list(map(lambda x:x[0],cr.execute("select common_name from Teams2").fetchall())))
    f1=customtkinter.CTkFrame(var)
    f1.pack(fill='x')
    image=ImageTk.PhotoImage(Image.open(r"k14.jpeg").resize((var.winfo_width(),var.winfo_height() ),Image.ANTIALIAS) )
    l = []
    l.append(customtkinter.CTkLabel(f1,image=image,fg_color="white",bg_color='white',width=var.winfo_width(),height=var.winfo_height() ))
    l[-1].grid(column=0, row=0)
    b=customtkinter.CTkButton(f1,text="Back",width=20,command=main2,bg_color="#f22693")
    b.grid(column=0,row=0,sticky=NE)
    s2=customtkinter.StringVar()
    s1=customtkinter.StringVar()
    c1=customtkinter.CTkComboBox(f1,width=150,variable=s1,values=l1,dropdown_color="#463e78",command=lambda s:k1(s1.get(),c2),fg_color="#463e78",text_font=('Lato', 16, ''))
    c1.place(x=450,y=200)
    c2=customtkinter.CTkComboBox(f1,width=150,variable=s2,values=l2,dropdown_color="#463e78",command=lambda s:k2(s2.get(),c1),fg_color="#463e78",text_font=('Lato', 16, ''))
    c2.place(x=150,y=200)
    sp1=Spinbox(f1,width=3,activebackground="black",bd=2,fg="white",bg='#463e78',from_ =0 ,to =99,font=('Lato', 16, ''))
    sp1.place(x=190,y=300)
    sp2=Spinbox(f1,width=3,bd=2,fg="white",bg='#463e78',from_ =0 ,to =99,font=('Lato', 16, ''))
    sp2.place(x=490,y=300)
    b2=customtkinter.CTkButton(f1,fg_color="#b91f16",bg_color="#2e436b",command =lambda :match(s1.get(),s2.get(),sp1.get(),sp2.get()),text="save",width=60,text_font=('Lato', 16, ''))
    b2.place(x=350,y=400)
    s2.set('Arsenal')
    s1.set('Manchester City')
    def k1 (w2,c2):
        global e12

        q=l1.copy()

        q.remove(w2)
        c2.place_forget()
        c2 = customtkinter.CTkComboBox(f1, width=150, variable=s2, values=q, dropdown_color="#463e78",
                                       command=lambda s: k2(s2.get(),c1), fg_color="#463e78", text_font=('Lato', 16, ''))
        c2.place(x=150, y=200)

        print(q)
        f1.update()
    def k2(w2,c1):
        global e12
        q=l1.copy()

        q.remove(w2)
        c1.place_forget()
        c1 = customtkinter.CTkComboBox(f1, width=150, variable=s1, values=q, dropdown_color="#463e78",
                                       command=lambda s: k1(s1.get(), c2), fg_color="#463e78",
                                       text_font=('Lato', 16, ''))
        c1.place(x=450, y=200)

        print(q)
        f1.update()

    var.mainloop()
def match(team1,team2,res1,res2):
    global cr
    global db
    if(res1>res2):
        cr.execute(f"update Teams2 set points=points+3 where common_name='{team1}'")

    elif(res2>res1):
        cr.execute(f"update Teams2 set points=points+3 where common_name='{team2}'")

    else:
        cr.execute(f"update Teams2 set points=points+1 where common_name='{team1}' or common_name='{team2}'")
    print(f'{team1}')
    cr.execute(f"update Teams2 set matches_played=matches_played+1 where common_name='{team1}' or common_name='{team2}'")
    print('saved')
    db.commit()
    print(cr.execute("select * from teams2 order by points").fetchall())

def main2():
    global var

    var.geometry("1050x600")
    for widget in var.winfo_children():
        threading.Thread(target=widget.destroy).start()
    var.update()
    photo1 = ImageTk.PhotoImage(Image.open(r'k10.jpeg').resize((1050,600)))
    mad = customtkinter.CTkLabel(var, image=photo1, width=810, height=600)
    mad.pack()
    photo2 = ImageTk.PhotoImage(Image.open(r"k12.jpeg").resize((100,100)))
    bt = customtkinter.CTkButton(var, image=photo2, text='المباريات', text_font=('tajawal', 16, 'bold'),command=lambda :matches(var), compound=TOP, border_width=2, fg_color='#b90066', width=118, bg_color="#84a202",height=143,text_color="#600048")
    bt.place(x=615, y=450)
    photo3 = ImageTk.PhotoImage(Image.open(r"k2.jpeg").resize((100,100)))
    bt1 = customtkinter.CTkButton(var, image=photo3, text='الأخبار',command=lambda:news(var), text_font=('tajawal', 16, 'bold'), compound=TOP, border_width=2, fg_color='#18ffff', bg_color="#84a202", width=118, height=143,text_color="#2f0c40")
    bt1.place(x=300, y=450)
    photo4 = ImageTk.PhotoImage(Image.open(r"k.jpeg").resize((100,100)))
    bt2 = customtkinter.CTkButton(var, image=photo4, text='الترتيب', bg_color="#9db38a", text_font=('tajawal', 16, 'bold'), command=leauge,compound=TOP, border_width=2, fg_color='#8D38C9', width=118, height=143,text_color="#2f0c40")
    bt2.place(x=10, y=450)
    photo5 = ImageTk.PhotoImage(Image.open(r"k13.jpeg").resize((100,100)))
    bt3 = customtkinter.CTkButton(var, image=photo5, text='الاعبون', bg_color="#9db38a",command=page_player,text_font=('tajawal', 16, 'bold'), compound=TOP, border_width=2, fg_color='#d4046f', width=118, height=143,text_color="#2f0c40")
    bt3.place(x=150, y=450)
    bt4 = customtkinter.CTkButton(var, text='مباريات اليوم', text_color="#2f0c40", text_font=('tajawal', 16, 'bold'),border_width=0,  fg_color='white', command=open1,cursor='mouse',bg_color="#84a202")
    bt4.place(x=450, y=550)
    photo6 = ImageTk.PhotoImage(Image.open(r"k14.jpeg").resize((100,100)))
    b9 = customtkinter.CTkButton(var, image=photo6, text='اضافة مباريات', bg_color="#efde05", text_font=('tajawal', 16, 'bold'), command=add_matches,compound=TOP, border_width=2, fg_color='#e6382d', width=118, height=143,text_color="#2f0c40")
    b9.place(x=750, y=450)
    bt10 = customtkinter.CTkButton(var, image=photo5, text="مبرمجون", bg_color="#9db38a",command=lambda :program(var),text_font=('tajawal', 16, 'bold'), compound=TOP, border_width=2, fg_color='#d4046f', width=118, height=143,text_color="#2f0c40")
    bt10.place(x=900, y=450)
    b=customtkinter.CTkButton(var,text="reset",width=20,command=reset,bg_color="#84a202")
    b.place(x=1000,y=0)
    def program(var):
        programmes(var)
    var.update()
    var.mainloop()
def reset ():
    cr.execute("update Teams2 set matches_played=0 ,points=0")
def matches(root):
    global cora1
    global cora2
    global cora3
    for widget in var.winfo_children():
        threading.Thread(target=widget.destroy).start()
    var.update()
    class Dawre():
        def __init__(self, root):
            self.root = root
            self.root.geometry('1400x700+40+10')
            self.root.title("الدوري الانجليزي الممتاز")

            def open1():
                webbrowser.open(
                    'https://www.alremontada.com/h2h/%D8%A7%D8%B1%D8%B3%D9%86%D8%A7%D9%84-%D9%88%D9%83%D8%B1%D9%8A%D8%B3%D8%AA%D8%A7%D9%84-%D8%A8%D8%A7%D9%84%D8%A7%D8%B3?fixture_id=157105')

            def open2():
                webbrowser.open('https://www.btolat.com/matches/details/2882492')

            def open3():
                webbrowser.open('https://www.btolat.com/matches/details/2618853')

            def open4():
                webbrowser.open('https://www.btolat.com/matches/details/2618795')

            def open5():
                webbrowser.open('https://www.btolat.com/matches/details/2882577')

            def open6():
                webbrowser.open('https://www.btolat.com/matches/details/2755951')

            def open7():
                webbrowser.open('https://ar.soccerway.com/teams/comparison/?team_ids[]=660&team_ids[]=661')

            def open8():
                webbrowser.open('https://www.btolat.com/matches/details/2618843')

            def open9():
                webbrowser.open('https://www.btolat.com/matches/details/2618841')

            def open10():
                webbrowser.open('https://www.btolat.com/matches/details/2618507')

            def open11():
                webbrowser.open('https://www.btolat.com/matches/details/2882150')

            def open12():
                webbrowser.open(
                    'https://www.alremontada.com/h2h/%D8%A8%D8%B1%D8%A7%D9%8A%D8%AA%D9%88%D9%86-%D9%88%D9%83%D8%B1%D9%8A%D8%B3%D8%AA%D8%A7%D9%84-%D8%A8%D8%A7%D9%84%D8%A7%D8%B3?fixture_id=157178')

            def open13():
                webbrowser.open('https://www.btolat.com/matches/details/2618539')

            def open14():
                webbrowser.open('https://tribuna.com/ar/match/arsenal-vs-west-ham-united/')

            def open15():
                webbrowser.open('https://www.btolat.com/matches/details/2882190')

            def open16():
                webbrowser.open('https://ar.soccerway.com/teams/comparison/?team_ids%5B0%5D=662&team_ids%5B1%5D=661')

            def open17():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=662&competition_ids%5B%5D=8&team_ids%5B%5D=679')

            def open18():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=703&competition_ids%5B%5D=8&team_ids%5B%5D=660')

            def open19():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=676&competition_ids%5B%5D=8&team_ids%5B%5D=663')

            def open20():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=684&competition_ids%5B%5D=8&team_ids%5B%5D=661')

            def open21():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=661&competition_ids%5B%5D=8&team_ids%5B%5D=679')

            def open22():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=663&competition_ids%5B%5D=8&team_ids%5B%5D=660')

            def open23():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=662&competition_ids%5B%5D=8&team_ids%5B%5D=684')

            def open24():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=676&competition_ids%5B%5D=8&team_ids%5B%5D=703')

            def open25():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=684&competition_ids%5B%5D=8&team_ids%5B%5D=679')

            def open26():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=662&competition_ids%5B%5D=8&team_ids%5B%5D=663')

            def open27():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=660&competition_ids%5B%5D=8&team_ids%5B%5D=676')

            def open28():
                webbrowser.open(
                    'https://ar.soccerway.com/teams/comparison/?competition_ids%5B%5D=8&team_ids%5B%5D=703&competition_ids%5B%5D=8&team_ids%5B%5D=661')

            self.root.resizable(False, False)
            self.root.iconbitmap(r"k4.jpeg")

            f1 = Frame(root, width=340, height=320, bd=2, bg='#0B4C5F')
            f1.place(x=1055, y=4)
            l1 = Label(f1, text='يوم المباراة 1 من إجمالي 7', font=('tajawal', 12, 'bold'))
            l1.place(x=130, y=10)
            sc = Scrollbar(root, orient=VERTICAL)
            sc.pack(side=RIGHT, fill=Y, expand=False)
            f2 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
            f2.place(x=125, y=50)
            l2 = Label(f2, text='كريستال بالاس', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l2.place(x=90, y=0)
            l3 = Label(f2, text='أرسنال', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l3.place(x=130, y=25)
            bt1 = Button(f1, text='الأحد 8/21  م1:30', font=('tajawal', 12, 'bold'), command=open1, cursor='mouse',
                         bg='#98AFC7')
            bt1.place(x=4, y=51, width=120, height=51)
            f3 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
            f3.place(x=125, y=105)
            l2 = Label(f3, text='ليفيربول', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l2.place(x=130, y=0)
            l3 = Label(f3, text='تشيلسي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l3.place(x=130, y=25)
            bt2 = Button(f1, text='الأحد 8/21  م4:00', font=('tajawal', 12, 'bold'), command=open2, cursor='mouse',
                         bg='#98AFC7')
            bt2.place(x=4, y=105, width=120, height=51)
            f4 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
            f4.place(x=125, y=160)
            l2 = Label(f4, text='مان يونايتد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l2.place(x=120, y=0)
            l3 = Label(f4, text='برايتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l3.place(x=139, y=25)
            bt2 = Button(f1, text='الأحد 8/21  م6:30', font=('tajawal', 12, 'bold'), command=open3, cursor='mouse',
                         bg='#98AFC7')
            bt2.place(x=4, y=160, width=120, height=51)

            f5 = Frame(f1, width=200, height=50, bd=2, bg='#98AFC7')
            f5.place(x=125, y=215)
            l4 = Label(f5, text='وست هام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l4.place(x=129, y=0)
            l5 = Label(f5, text='مان سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l5.place(x=130, y=25)
            bt3 = Button(f1, text='الأحد 8/21  م10:00', font=('tajawal', 12, 'bold'), command=open4, cursor='mouse',
                         bg='#98AFC7')
            bt3.place(x=4, y=215, width=120, height=51)

            #####fr2
            f6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
            f6.place(x=1055, y=290)
            l6 = Label(f6, text='يوم المباراة 2 من إجمالي 7', font=('tajawal', 12, 'bold'))
            l6.place(x=125, y=10)

            f7 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
            f7.place(x=125, y=50)
            l7 = Label(f7, text='وست هام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l7.place(x=127, y=0)
            l8 = Label(f7, text='برايتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l8.place(x=139, y=25)
            bt4 = Button(f6, text='السبت8/27م6:00', font=('tajawal', 12, 'bold'), command=open5, cursor='mouse',
                         bg='#98AFC7')
            bt4.place(x=4, y=51, width=120, height=51)
            f8 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
            f8.place(x=125, y=105)
            l9 = Label(f8, text='مان سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l9.place(x=130, y=0)
            l10 = Label(f8, text='مان يونايتيد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l10.place(x=120, y=25)
            bt5 = Button(f6, text='السبت8/27م9:00', font=('tajawal', 12, 'bold'), command=open6, cursor='mouse',
                         bg='#98AFC7')
            bt5.place(x=4, y=105, width=120, height=51)
            f9 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
            f9.place(x=125, y=160)
            l11 = Label(f9, text='تشيلسي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l11.place(x=130, y=0)
            l12 = Label(f9, text='أرسنال', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l12.place(x=141, y=25)
            bt6 = Button(f6, text='السبت8/27م9:00', font=('tajawal', 12, 'bold'), command=open7, cursor='mouse',
                         bg='#98AFC7')
            bt6.place(x=4, y=160, width=120, height=51)
            f10 = Frame(f6, width=200, height=50, bd=2, bg='#98AFC7')
            f10.place(x=125, y=215)
            l13 = Label(f10, text='ليفربول', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l13.place(x=138, y=0)
            l14 = Label(f10, text='كريستال بالاس', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            l14.place(x=100, y=25)
            bt7 = Button(f6, text='السبت8/27م12:00', font=('tajawal', 12, 'bold'), command=open8, cursor='mouse',
                         bg='#98AFC7')
            bt7.place(x=4, y=215, width=120, height=51)
            ##f3
            fr1 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
            fr1.place(x=725, y=4)
            lab1 = Label(fr1, text='يوم المباراة 3 من إجمالي 7', font=('tajawal', 12, 'bold'))
            lab1.place(x=125, y=10)
            fr2 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
            fr2.place(x=125, y=50)
            lab2 = Label(fr2, text='مان سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab2.place(x=127, y=0)
            lab3 = Label(fr2, text='تشيلسي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab3.place(x=141, y=25)
            btn1 = Button(fr1, text='الأربعاء9/3 م2:00', font=('tajawal', 12, 'bold'), command=open9, cursor='mouse',
                          bg='#98AFC7')
            btn1.place(x=4, y=51, width=120, height=51)
            fr3 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
            fr3.place(x=125, y=105)
            lab4 = Label(fr3, text='مان يونايتيد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab4.place(x=120, y=0)
            lab5 = Label(fr3, text='أرسنال', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab5.place(x=142, y=25)
            btn2 = Button(fr1, text='الأربعاء9/3 م5:00', font=('tajawal', 12, 'bold'), command=open10, cursor='mouse',
                          bg='#98AFC7')
            btn2.place(x=4, y=105, width=120, height=51)
            fra4 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
            fra4.place(x=125, y=160)
            lab6 = Label(fra4, text='وست هام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab6.place(x=130, y=0)
            lab7 = Label(fra4, text='ليفربول', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab7.place(x=141, y=25)
            btn3 = Button(fr1, text='الأربعاء9/3 م10:00', font=('tajawal', 12, 'bold'), command=open11, cursor='mouse',
                          bg='#98AFC7')
            btn3.place(x=4, y=160, width=120, height=51)
            fr5 = Frame(fr1, width=200, height=50, bd=2, bg='#98AFC7')
            fr5.place(x=125, y=215)
            lab8 = Label(fr5, text='برايتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab8.place(x=138, y=0)
            lab9 = Label(fr5, text='كريستال بالاس', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab9.place(x=100, y=25)
            btn4 = Button(fr1, text='الأربعاء9/3 م1:00', font=('tajawal', 12, 'bold'), command=open12, cursor='mouse',
                          bg='#98AFC7')
            btn4.place(x=4, y=215, width=120, height=51)
            # fr4
            fr6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
            fr6.place(x=725, y=290)
            lab10 = Label(fr6, text='يوم المباراة 4 من إجمالي 7', font=('tajawal', 12, 'bold'))
            lab10.place(x=125, y=10)
            fr7 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
            fr7.place(x=125, y=50)
            lab11 = Label(fr7, text='كريستال بالاس', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab11.place(x=95, y=0)
            lab12 = Label(fr7, text='مان سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab12.place(x=120, y=25)
            btn5 = Button(fr6, text='الثلاثاء9/11 7:00م', font=('tajawal', 12, 'bold'), command=open13, cursor='mouse',
                          bg='#98AFC7')
            btn5.place(x=4, y=51, width=120, height=51)
            fr8 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
            fr8.place(x=125, y=105)
            lab13 = Label(fr8, text='ارسنال', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab13.place(x=140, y=0)
            lab14 = Label(fr8, text='وست هام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab14.place(x=130, y=25)
            btn6 = Button(fr6, text='الثلاثاء9/11 9:30م', font=('tajawal', 12, 'bold'), command=open14, cursor='mouse',
                          bg='#98AFC7')
            btn6.place(x=4, y=105, width=120, height=51)
            fra5 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
            fra5.place(x=125, y=160)
            lab15 = Label(fra5, text='ليفربول', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab15.place(x=139, y=0)
            lab16 = Label(fra5, text='برايتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab16.place(x=141, y=25)
            btn7 = Button(fr6, text='الثلاثاء9/11 9:30م', font=('tajawal', 12, 'bold'), command=open15, cursor='mouse',
                          bg='#98AFC7')
            btn7.place(x=4, y=160, width=120, height=51)
            fr9 = Frame(fr6, width=200, height=50, bd=2, bg='#98AFC7')
            fr9.place(x=125, y=215)
            lab17 = Label(fr9, text='تشيلسي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab17.place(x=138, y=0)
            lab18 = Label(fr9, text='مان يونايتيد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            lab18.place(x=120, y=25)
            btn8 = Button(fr6, text='الثلاثاء9/11 12:00م', font=('tajawal', 12, 'bold'), command=open16, cursor='mouse',
                          bg='#98AFC7')
            btn8.place(x=4, y=215, width=120, height=51)
            # fr5
            frr1 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
            frr1.place(x=395, y=4)
            laa1 = Label(frr1, text='يوم المباراة 5 من إجمالي 7', font=('tajawal', 12, 'bold'))
            laa1.place(x=125, y=10)
            frr2 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
            frr2.place(x=125, y=50)
            laa2 = Label(frr2, text='كريستال بالاس', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa2.place(x=95, y=0)
            laa3 = Label(frr2, text='مان يونايتيد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa3.place(x=116, y=25)
            btt1 = Button(frr1, text='الأحد9/21 6:00م', font=('tajawal', 12, 'bold'), command=open17, cursor='mouse',
                          bg='#98AFC7')
            btt1.place(x=4, y=51, width=120, height=51)
            frr3 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
            frr3.place(x=125, y=105)
            laa4 = Label(frr3, text='ارسنال', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa4.place(x=136, y=0)
            laa5 = Label(frr3, text='برايتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa5.place(x=136, y=25)
            btt2 = Button(frr1, text='الأحد9/21 9:00م', font=('tajawal', 12, 'bold'), command=open18, cursor='mouse',
                          bg='#98AFC7')
            btt2.place(x=4, y=105, width=120, height=51)
            frr4 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
            frr4.place(x=125, y=160)
            laa6 = Label(frr4, text='ليفربول', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa6.place(x=136, y=0)
            laa7 = Label(frr4, text='مان سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa7.place(x=128, y=25)
            btt3 = Button(frr1, text='الأحد9/21 9:00م', font=('tajawal', 12, 'bold'), command=open19, cursor='mouse',
                          bg='#98AFC7')
            btt3.place(x=4, y=160, width=120, height=51)
            frr5 = Frame(frr1, width=200, height=50, bd=2, bg='#98AFC7')
            frr5.place(x=125, y=215)
            laa8 = Label(frr5, text='تشيلسي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa8.place(x=136, y=0)
            laa9 = Label(frr5, text='وست هام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa9.place(x=130, y=25)
            btt4 = Button(frr1, text='الأحد9/21 11:00م', font=('tajawal', 12, 'bold'), command=open20, cursor='mouse',
                          bg='#98AFC7')
            btt4.place(x=4, y=215, width=120, height=51)
            # fr6
            frr6 = Frame(root, width=328, height=300, bd=2, bg='#0B4C5F')
            frr6.place(x=395, y=290)
            laa10 = Label(frr6, text='يوم المباراة 6 من إجمالي 7', font=('tajawal', 12, 'bold'))
            laa10.place(x=125, y=10)
            frr7 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
            frr7.place(x=125, y=50)
            laa11 = Label(frr7, text='كريستال بالاس', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa11.place(x=95, y=0)
            laa12 = Label(frr7, text='تشيلسي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa12.place(x=130, y=25)
            btt5 = Button(frr6, text='الاثنين9/29 3:00م', font=('tajawal', 12, 'bold'), command=open21, cursor='mouse',
                          bg='#98AFC7')
            btt5.place(x=4, y=51, width=120, height=51)
            frr8 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
            frr8.place(x=125, y=105)
            laa13 = Label(frr8, text='ارسنال', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa13.place(x=136, y=0)
            laa14 = Label(frr8, text='ليفربول', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa14.place(x=136, y=25)
            btt6 = Button(frr6, text='الاثنين9/29 5:30م', font=('tajawal', 12, 'bold'), command=open22, cursor='mouse',
                          bg='#98AFC7')
            btt6.place(x=4, y=105, width=120, height=51)
            frr9 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
            frr9.place(x=125, y=160)
            laa15 = Label(frr9, text='مان يونايتيد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa15.place(x=117, y=0)
            laa16 = Label(frr9, text='وست هام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa16.place(x=128, y=25)
            btt7 = Button(frr6, text='الاثنين9/29 9:00م', font=('tajawal', 12, 'bold'), command=open23, cursor='mouse',
                          bg='#98AFC7')
            btt7.place(x=4, y=160, width=120, height=51)
            frr10 = Frame(frr6, width=200, height=50, bd=2, bg='#98AFC7')
            frr10.place(x=125, y=215)
            laa17 = Label(frr10, text='برايتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa17.place(x=136, y=0)
            laa18 = Label(frr10, text='مان سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa18.place(x=130, y=25)
            btt8 = Button(frr6, text='الاثنين9/29 11:00م', font=('tajawal', 12, 'bold'), command=open24, cursor='mouse',
                          bg='#98AFC7')
            btt8.place(x=4, y=215, width=120, height=51)
            # fr7
            fa1 = Frame(root, width=335, height=300, bd=2, bg='#0B4C5F')
            fa1.place(x=58, y=4)
            laa19 = Label(fa1, text='يوم المباراة 7 من إجمالي 7', font=('tajawal', 12, 'bold'))
            laa19.place(x=131, y=10)
            fa2 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
            fa2.place(x=130, y=51)
            laa20 = Label(fa2, text='كريستال بالاس', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa20.place(x=95, y=0)
            laa21 = Label(fa2, text='وست هام', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa21.place(x=130, y=25)
            btt9 = Button(fa1, text='الخميس10/06 7:00م', font=('tajawal', 12, 'bold'), command=open25, cursor='mouse',
                          bg='#98AFC7')
            btt9.place(x=6, y=51, width=135, height=51)
            fa3 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
            fa3.place(x=130, y=105)
            laa22 = Label(fa3, text='ليفربول', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa22.place(x=136, y=0)
            laa23 = Label(fa3, text='مان يونايتيد', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa23.place(x=115, y=25)
            btt10 = Button(fa1, text='الخميس10/06 9:00م', font=('tajawal', 12, 'bold'), command=open26, cursor='mouse',
                           bg='#98AFC7')
            btt10.place(x=6, y=105, width=135, height=51)
            fa4 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
            fa4.place(x=130, y=160)
            laa24 = Label(fa4, text='أرسنال', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa24.place(x=135, y=0)
            laa25 = Label(fa4, text='مان سيتي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa25.place(x=125, y=25)
            btt11 = Button(fa1, text='الخميس10/06 9:00م', font=('tajawal', 12, 'bold'), command=open27, cursor='mouse',
                           bg='#98AFC7')
            btt11.place(x=6, y=160, width=135, height=51)
            fa5 = Frame(fa1, width=200, height=50, bd=2, bg='#98AFC7')
            fa5.place(x=130, y=215)
            laa26 = Label(fa5, text='برايتون', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa26.place(x=136, y=0)
            laa27 = Label(fa5, text='تشيلسي', font=('tajawal', 10, 'bold'), bg='#98AFC7')
            laa27.place(x=130, y=25)
            btt12 = Button(fa1, text='الخميس10/06 11:30م', font=('tajawal', 12, 'bold'), command=open28, cursor='mouse',
                           bg='#98AFC7')
            btt12.place(x=6, y=215, width=135, height=51)
            frm1 = Frame(root, width=60, height=700, bd=2, bg='#0B4C5F')
            frm1.place(x=0, y=4)
            frm2 = Frame(root, width=333, height=500, bd=2, bg='#0B4C5F')
            frm2.place(x=60, y=280)
            frm3 = Frame(root, width=1323, height=200, bd=2, bg='#0B4C5F')
            frm3.place(x=60, y=590)
            b = customtkinter.CTkButton(root, text="Back", width=20, command=main2, bg_color="#98AFC7")
            b.place(x=1350, y=0)
            b2= customtkinter.CTkButton(root, text="Next", width=80, command=lambda : core(root), bg_color="#98AFC7")
            b2.place(x=600, y=600)
            def core(root):
                cora1(root)
    amd = Dawre(root)
    root.mainloop()
def news (pro):
    for widget in pro.winfo_children():
            threading.Thread(target=widget.destroy).start()
    pro.update()
    class Dawre1():
        def __init__(self, pro):
            self.pro = pro
            self.pro.geometry('1400x700+50+50')
            self.pro.title("الدوري الانجليزي الممتاز")

            def ope1():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981265.html')

            def ope2():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981259.html')

            def ope3():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981253.html')

            def ope4():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981246.html')

            def ope5():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981239.html')

            def ope6():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981236.html')

            def ope7():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981232.html')

            def ope8():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981226.html')

            def ope9():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981211.html')

            def ope10():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981199.html')

            def ope11():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981169.html')

            def ope12():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981158.html')

            def ope13():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981155.html')

            def ope14():
                webbrowser.open('https://hihi2.com/2022/08/05/p1981152.html')

            def ope15():
                webbrowser.open(
                    'https://www.yallakora.com/epl/2761/News/429759/%D9%83%D9%84%D9%88%D8%A8-%D9%83%D8%A3%D8%B3-%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85-%D9%8A%D9%82%D8%A7%D9%85-%D9%81%D9%8A-%D8%A7%D9%84%D9%88%D9%82%D8%AA-%D8%A7%D9%84%D8%AE%D8%B7%D8%A3-%D9%88%D9%84%D9%8A%D9%81%D8%B1%D8%A8%D9%88%D9%84-%D9%84%D9%85-%D9%8A%D8%BA%D9%8A%D8%B1-%D8%AE%D8%B7%D8%B7%D9%87-%D9%84%D9%84%D9%85%D9%8A%D8%B1%D9%83%D8%A7%D8%AA%D9%88#NewsListing')

            def ope16():
                webbrowser.open(
                    'https://www.yallakora.com/epl/2761/News/429756/%D8%B5%D9%84%D8%A7%D8%AD-%D8%B9%D9%84%D9%89-%D8%A8-%D8%B9%D8%AF-%D8%AE%D8%B7%D9%88%D8%A9-%D9%85%D9%86-%D9%85%D8%B9%D8%A7%D8%AF%D9%84%D8%A9-%D8%B1%D9%82%D9%85-%D9%82%D9%8A%D8%A7%D8%B3%D9%8A-%D9%81%D9%8A-%D8%A7%D9%81%D8%AA%D8%AA%D8%A7%D8%AD-%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84%D8%A5%D9%86%D8%AC%D9%84%D9%8A%D8%B2%D9%8A#NewsListing')

            def ope17():
                webbrowser.open(
                    'https://arabic.sport360.com/article/%D9%83%D8%B1%D8%A9-%D8%A7%D9%86%D8%AC%D9%84%D9%8A%D8%B2%D9%8A%D8%A9/%D8%AA%D8%B4%D9%84%D8%B3%D9%8A/1152345/%D8%B1%D8%B3%D9%85%D9%8A%D8%A7%D9%8B-%D8%AA%D8%B4%D9%8A%D9%84%D8%B3%D9%8A-%D9%8A%D8%AA%D8%B9%D8%A7%D9%82%D8%AF-%D9%85%D8%B9-%D9%85%D8%A7%D8%B1%D9%83-%D9%83%D9%88%D9%83%D9%88%D8%B1%D9%8A%D9%84%D8%A7')

            def ope18():
                webbrowser.open(
                    'https://arabic.sport360.com/article/%D9%83%D8%B1%D8%A9-%D8%A7%D9%86%D8%AC%D9%84%D9%8A%D8%B2%D9%8A%D8%A9/%D8%AA%D8%B4%D9%84%D8%B3%D9%8A/1152320/%D8%AA%D8%B4%D9%8A%D9%84%D8%B3%D9%8A-%D9%8A%D8%AC%D8%AF-%D8%B6%D8%A7%D9%84%D8%AA%D9%87-%D8%A7%D9%84%D8%AF%D9%81%D8%A7%D8%B9%D9%8A%D8%A9-%D9%81%D9%8A-%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84')

            def ope19():
                webbrowser.open(
                    'https://arabic.sport360.com/article/%25d9%2583%25d8%25b1%25d8%25a9-%25d8%25a7%25d9%2586%25d8%25ac%25d9%2584%25d9%258a%25d8%25b2%25d9%258a%25d8%25a9/%25d9%2585%25d8%25a7%25d9%2586%25d8%25b4%25d8%25b3%25d8%25aa%25d8%25b1-%25d8%25b3%25d9%258a%25d8%25aa%25d9%258a/1152305/%25d8%25a3%25d8%25ac%25d9%2588%25d9%258a%25d8%25b1%25d9%2588-%25d9%258a%25d8%25ae%25d8%25aa%25d8%25a7%25d8%25b1-%25d8%25a7%25d9%2584%25d9%2585%25d9%258f%25d8%25b1%25d8%25b4%25d8%25ad-%25d8%25a7%25d9%2584%25d8%25a3%25d9%2588%25d9%2581%25d8%25b1-%25d8%25ad%25d8%25b8%25d8%25a7%25d9%258b-%25d9%2584%25d9%2584%25d9%2581%25d9%258')

            def ope20():
                webbrowser.open(
                    'https://arabic.sport360.com/article/%D9%83%D8%B1%D8%A9-%D8%A7%D9%86%D8%AC%D9%84%D9%8A%D8%B2%D9%8A%D8%A9/%D8%AA%D8%B4%D9%84%D8%B3%D9%8A/1152276/%D8%B1%D8%B3%D9%85%D9%8A%D8%A7%D9%8B-%D8%A3%D8%B2%D8%A8%D9%84%D9%83%D9%88%D9%8A%D8%AA%D8%A7-%D9%8A%D9%8F%D8%AC%D8%AF%D8%AF-%D8%AA%D8%B9%D8%A7%D9%82%D8%AF%D9%87-%D9%85%D8%B9-%D8%AA%D8%B4%D9%8A%D9%84')

            def ope21():
                webbrowser.open(
                    'https://arabic.sport360.com/article/%D9%83%D8%B1%D8%A9-%D8%A7%D9%86%D8%AC%D9%84%D9%8A%D8%B2%D9%8A%D8%A9/%D9%85%D8%A7%D9%86%D8%B4%D8%B3%D8%AA%D8%B1-%D9%8A%D9%88%D9%86%D8%A7%D9%8A%D8%AA%D8%AF/1152231/%D9%86%D8%A7%D9%86%D9%8A-%D9%8A%D8%B7%D8%A7%D9%84%D8%A8-%D9%83%D8%B1%D9%8A%D8%B3%D8%AA%D9%8A%D8%A7%D9%86%D9%88-%D8%B1%D9%88%D9%86%D8%A7%D9%84%D8%AF%D9%88-%D8%A8%D8%A7%D9%84%D8%A8%D9%82%D8%A7%D8%A1')

            def ope22():
                webbrowser.open(
                    'https://arabic.sport360.com/category/football/%D9%83%D8%B1%D8%A9-%D8%A7%D9%86%D8%AC%D9%84%D9%8A%D8%B2%D9%8A%D8%A9')
            self.pro.iconbitmap(r"new4.png")
            self.pro.config(background='#98AFC7')
            photo = PhotoImage(file=r'new1.png')
            res = photo.subsample(5, 5)
            bt = Button(pro, image=res, text="صفقة تبادلية بين توتنهام وبرشلونة", font=('tajawal', 8, 'bold'),
                        compound=TOP, width=190, height=150, command=ope1)
            bt.place(x=1200, y=4)
            photo1 = PhotoImage(file=r'new2.png')

            style = ttk.Style()
            style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
            style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
            style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
            res1 = photo1.subsample(5, 5)
            bt1 = Button(pro, image=res1, text="ماني:أريد مواجهة ليفربول وهزيمتهم", font=('tajawal', 8, 'bold'),
                         compound=TOP, width=190, height=150, command=ope2)
            bt1.place(x=1000, y=4)
            photo2 = PhotoImage(file=r'new3.png')
            res2 = photo2.subsample(4, 5)
            bt2 = Button(pro, image=res2, text="نادي عربي يقترب من إتفاقة مع نجم برشلونة", font=('tajawal', 8, 'bold'),
                         compound=TOP, width=240, height=150, command=ope3)
            bt2.place(x=750, y=4)
            photo3 = PhotoImage(file=r'new4.png')
            res3 = photo3.subsample(5, 5)
            bt3 = Button(pro, image=res3, text="تعرف علي الراحلين عن ريال مدريد", font=('tajawal', 8, 'bold'),
                         compound=TOP, width=200, height=150, command=ope4)
            bt3.place(x=540, y=4)
            photo4 = PhotoImage(file=r'new5.png')
            res4 = photo4.subsample(4, 5)
            bt4 = Button(pro, image=res4, text="مدرب ليفربول:تشيلسي أصعب خصم لنا", font=('tajawal', 8, 'bold'),
                         compound=TOP, width=220, height=150, command=ope5)
            bt4.place(x=312, y=4)
            photo5 = PhotoImage(file=r'new6.png')
            res5 = photo5.subsample(3, 5)
            bt5 = Button(pro, image=res5, text="شاهد كيف خطف مودريتش الأضواء في مران ريال مدريد",
                         font=('tajawal', 8, 'bold'), compound=TOP, width=300, height=150, command=ope6)
            bt5.place(x=2, y=4)
            photo6 = PhotoImage(file=r'new7.png')
            res6 = photo6.subsample(4, 5)
            bt6 = Button(pro, image=res6, text="السداسية ليست حلما بل هدفا لريال مدريد", font=('tajawal', 8, 'bold'),
                         compound=TOP, width=230, height=150, command=ope7)
            bt6.place(x=1160, y=165)
            photo7 = PhotoImage(file=r'new8.png')
            res7 = photo7.subsample(4, 5)
            bt7 = Button(pro, image=res7, text="البداية قد تكون صعبة ولكنها ليست مستحيلة", font=('tajawal', 8, 'bold'),
                         compound=TOP, width=250, height=150, command=ope8)
            bt7.place(x=893, y=165)
            photo8 = PhotoImage(file=r'new9.png')
            res8 = photo8.subsample(4, 5)
            bt8 = Button(pro, image=res8, text="هل كان برشلونة المتضرر الوحيد بعد رحيل ميسي",
                         font=('tajawal', 8, 'bold'), compound=TOP, width=258, height=150, command=ope9)
            bt8.place(x=620, y=165)
            photo9 = PhotoImage(file=r'new10.png')
            res9 = photo9.subsample(3, 5)
            bt9 = Button(pro, image=res9, text="الكل في برشلونة يجب أن يفهم بيكيه ليس مذنبا",
                         font=('tajawal', 8, 'bold'), compound=TOP, width=255, height=150, command=ope10)
            bt9.place(x=350, y=165)
            photo10 = PhotoImage(file=r'new11.png')
            res10 = photo10.subsample(3, 4)
            bt10 = Button(pro, image=res10, text="وكيل أعمال بيرناردو سيلفا يعطي الضوء الأخضر لبرشلونة",
                          font=('tajawal', 8, 'bold'), compound=TOP, width=310, height=150, command=ope11)
            bt10.place(x=20, y=165)
            photo11 = PhotoImage(file=r'new12.png')
            res11 = photo11.subsample(3, 4)
            bt11 = Button(pro, image=res11, text="ليفربول شوكة في حلق مانشيستر سيتي", font=('tajawal', 8, 'bold'),
                          compound=TOP, width=250, height=150, command=ope12)
            bt11.place(x=1139, y=328)
            photo12 = PhotoImage(file=r'new13.png')
            res12 = photo12.subsample(3, 4)
            bt12 = Button(pro, image=res12, text="المرشح الأوفر حظا لنيل لقب البريمير ليج هذا الموسم",
                          font=('tajawal', 8, 'bold'), compound=TOP, width=310, height=150, command=ope13)
            bt12.place(x=818, y=328)
            photo13 = PhotoImage(file=r'new14.png')
            res13 = photo13.subsample(3, 4)
            bt13 = Button(pro, image=res13, text="إيرلينج هالاند..أكثر من مجرد صفقة", font=('tajawal', 8, 'bold'),
                          compound=TOP, width=310, height=150, command=ope14)
            bt13.place(x=496, y=328)
            photo14 = PhotoImage(file=r'new15.png')
            res14 = photo14.subsample(4, 6)
            bt14 = Button(pro, image=res14, text="كلوب:كأس العالم يقام في الوقت الخطأ", font=('tajawal', 8, 'bold'),
                          compound=TOP, width=260, height=150, command=ope15)
            bt14.place(x=225, y=328)
            photo15 = PhotoImage(file=r'new16.png')
            res15 = photo15.subsample(4, 6)
            bt15 = Button(pro, image=res15, text="صلاح علي وشك تحقق رقم قياسي", font=('tajawal', 8, 'bold'),
                          compound=TOP, width=209, height=150, command=ope16)
            bt15.place(x=4, y=328)
            photo16 = PhotoImage(file=r'new17.png')
            res16 = photo16.subsample(4, 6)
            bt16 = Button(pro, image=res16, text="رسميا اتشيلسي يتعاقد مع مارك كوكوريلا", font=('tajawal', 8, 'bold'),
                          compound=TOP, width=250, height=150, command=ope17)
            bt16.place(x=1139, y=490)
            photo17 = PhotoImage(file=r'new18.png')
            res17 = photo17.subsample(4, 6)
            bt17 = Button(pro, image=res17, text="تشيلسي يجد ضالته الدفاعية في الدوري الايطالي",
                          font=('tajawal', 8, 'bold'), compound=TOP, width=260, height=150, command=ope18)
            bt17.place(x=869, y=490)
            photo18 = PhotoImage(file=r'new19.png')
            res18 = photo18.subsample(4, 6)
            bt18 = Button(pro, image=res18, text="اجويرو يختار المرشح الأوفر حظا للفوز بالدوري الانجليزي",
                          font=('tajawal', 8, 'bold'), compound=TOP, width=290, height=150, command=ope19)
            bt18.place(x=568, y=490)
            photo19 = PhotoImage(file=r'new20.png')
            res19 = photo19.subsample(3, 4)
            bt19 = Button(pro, image=res19, text="رسميا أزبلكويتا يجدد تعاقده مع تشيلسي", font=('tajawal', 8, 'bold'),
                          compound=TOP, width=232, height=150, command=ope20)
            bt19.place(x=325, y=490)
            photo20 = PhotoImage(file=r'new21.png')
            res20 = photo20.subsample(2, 4)
            bt20 = Button(pro, image=res20, text="ناني يطالب كريستيانو رونالدو بالبقاء في مانشيستر يونايتيد",
                          font=('tajawal', 8, 'bold'), compound=TOP, width=310, height=150, command=ope21)
            bt20.place(x=4, y=490)
            bt21 = Button(pro, text='المزيد', font=('tajawal', 11, 'bold'), width=20, height=1, bg='#1589FF',
                          command=ope22)
            bt21.place(x=640, y=650)
            b = customtkinter.CTkButton(pro, text="Back", width=20, command=main2, bg_color="#f22693")
            b.place(x=850, y=0)
            pro.mainloop()

    temp = Dawre1(pro)
    pro.mainloop()
main2()
var.mainloop()
db.commit()
db.close()
