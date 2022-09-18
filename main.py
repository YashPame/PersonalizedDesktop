from tkinter import *
import pyautogui
from Database import *
import os
from tkinter import messagebox
from webbrowser import open as WbOpen
from psutil import sensors_battery, virtual_memory, cpu_percent
from plyer import notification
from datetime import datetime
from time import strftime
import requests
from bs4 import BeautifulSoup
from random import randint
from pygame import mixer
from screen_brightness_control import get_brightness, set_brightness
from tkinter import ttk


class Desktop:
    def __init__(self, Root):
        self.root = Root
        MainWidth = self.root.winfo_screenwidth()
        MainHeight = self.root.winfo_screenheight()
        self.root.geometry(f"{MainWidth}x{MainHeight}+0+0")
        self.BG = PhotoImage(file="Background.png")
        Background = Label(self.root, image=self.BG)
        Background.place(x=0, y=0, width=1920, height=1080)

        self.Exit_BG = PhotoImage(file=ExitImg)
        ExitBtn = Button(self.root, image=self.Exit_BG, relief=RIDGE, bd=4, command=self.Exit)
        ExitBtn.place(x=1865, y=0, width=55, height=55)

        # --------------------------------------------------------
        self.Central1Btn_BG = PhotoImage(file=Central[0][0][0])
        self.Central2Btn_BG = PhotoImage(file=Central[1][0])
        self.Central3Btn_BG = PhotoImage(file=Central[2][0])
        self.Central4Btn_BG = PhotoImage(file=Central[3][0])
        self.Central5Btn_BG = PhotoImage(file=Central[4][0])
        self.Central6Btn_BG = PhotoImage(file=Central[5][0])
        self.Central7Btn_BG = PhotoImage(file=Central[6][0][0])

        self.Central1Btn = Button(self.root, image=self.Central1Btn_BG, relief=RIDGE, bd=3, bg="White", command=lambda: self.openApplication(Central[0][0][1]))
        self.Central1Btn.place(x=840, y=147, width=55, height=55)

        self.Central1_1Btn = Button(self.root, text=Central[0][1][0][0], font="Ariel 10 bold", relief=RIDGE, bd=1, bg='White', command=lambda: self.openApplication(Central[0][1][0][0]))
        self.Central1_1Btn.place(x=927, y=135, width=38, height=20)
        self.Central1_2Btn = Button(self.root, text=Central[0][1][1][0], font="Ariel 10 bold", relief=RIDGE, bd=1, bg='White', command=lambda: self.openApplication(Central[0][1][1][0]))
        self.Central1_2Btn.place(x=954, y=166, width=38, height=20)
        self.Central1_3Btn = Button(self.root, text=Central[0][1][2][0], font="Ariel 10 bold", relief=RIDGE, bd=1, bg='White', command=lambda: self.openApplication(Central[0][1][2][0]))
        self.Central1_3Btn.place(x=979, y=196, width=38, height=20)

        self.Central2Btn = Button(self.root, image=self.Central2Btn_BG, relief=RIDGE, bd=3, bg="White", command=lambda: self.openApplication(Central[1][1]))
        self.Central3Btn = Button(self.root, image=self.Central3Btn_BG, relief=RIDGE, bd=3, bg="White", command=lambda: self.openApplication(Central[2][1]))
        self.Central4Btn = Button(self.root, image=self.Central4Btn_BG, relief=RIDGE, bd=3, bg="White", command=lambda: self.openApplication(Central[3][1]))
        self.Central5Btn = Button(self.root, image=self.Central5Btn_BG, relief=RIDGE, bd=3, bg="White", command=lambda: self.openApplication(Central[4][1]))
        self.Central6Btn = Button(self.root, image=self.Central6Btn_BG, relief=RIDGE, bd=3, bg="White", command=lambda: self.openApplication(Central[5][1]))

        self.Central2Btn.place(x=712, y=221, width=55, height=55)
        self.Central3Btn.place(x=840, y=296, width=55, height=55)
        self.Central4Btn.place(x=712, y=370, width=55, height=55)
        self.Central5Btn.place(x=840, y=446, width=55, height=55)
        self.Central6Btn.place(x=712, y=521, width=55, height=55)

        self.Central7Btn = Button(self.root, image=self.Central7Btn_BG, relief=RIDGE, bd=3, bg="White", command=lambda: self.openApplication(Central[6][0][1]))
        self.Central7Btn.place(x=840, y=596, width=55, height=55)

        self.Central7_1Btn_BG = PhotoImage(file=Central[6][1][0][0])
        self.Central7_2Btn_BG = PhotoImage(file=Central[6][1][1][0])
        self.Central7_3Btn_BG = PhotoImage(file=Central[6][1][2][0])

        self.Central7_1Btn = Button(self.root, image=self.Central7_1Btn_BG, relief=RIDGE, bd=1, bg='White')
        self.Central7_2Btn = Button(self.root, image=self.Central7_2Btn_BG, relief=RIDGE, bd=1, bg='White')
        self.Central7_3Btn = Button(self.root, image=self.Central7_3Btn_BG, relief=RIDGE, bd=1, bg='White')

        self.Central7_1Btn.place(x=926, y=584, width=39, height=19)
        self.Central7_2Btn.place(x=954, y=615, width=38, height=20)
        self.Central7_3Btn.place(x=979, y=645, width=38, height=20)

        # --------------------------------------------------------------------------------

        self.Button_1to6_main_BG = PhotoImage(file=Button_1to6[0][0])
        self.Button_1to6_1_BG = PhotoImage(file=Button_1to6[1][0])
        self.Button_1to6_2_BG = PhotoImage(file=Button_1to6[2][0])
        self.Button_1to6_3_BG = PhotoImage(file=Button_1to6[3][0])
        self.Button_1to6_4_BG = PhotoImage(file=Button_1to6[4][0])
        self.Button_1to6_5_BG = PhotoImage(file=Button_1to6[5][0])
        self.Button_1to6_6_BG = PhotoImage(file=Button_1to6[6][0])

        self.Button_1to6_main = Button(self.root, image=self.Button_1to6_main_BG, relief=RIDGE, bd=3)
        self.Button_1to6_1 = Button(self.root, image=self.Button_1to6_1_BG, relief=RIDGE, bd=1, bg='White', command=lambda: self.openApplication(Button_1to6[1][1]))
        self.Button_1to6_2 = Button(self.root, image=self.Button_1to6_2_BG, relief=RIDGE, bd=1, bg='White', command=lambda: self.openApplication(Button_1to6[2][1]))
        self.Button_1to6_3 = Button(self.root, image=self.Button_1to6_3_BG, relief=RIDGE, bd=1, bg='White', command=lambda: self.openApplication(Button_1to6[3][1]))
        self.Button_1to6_4 = Button(self.root, image=self.Button_1to6_4_BG, relief=RIDGE, bd=1, bg='White', command=lambda: self.openApplication(Button_1to6[4][1]))
        self.Button_1to6_5 = Button(self.root, image=self.Button_1to6_5_BG, relief=RIDGE, bd=1, bg='White', command=lambda: self.openApplication(Button_1to6[5][1]))
        self.Button_1to6_6 = Button(self.root, image=self.Button_1to6_6_BG, relief=RIDGE, bd=1, bg='White', command=lambda: self.openApplication(Button_1to6[6][1]))

        self.Button_1to6_main.place(x=632, y=703, width=55, height=55)
        self.Button_1to6_1.place(x=718, y=691, width=38, height=20)
        self.Button_1to6_2.place(x=745, y=722, width=38, height=20)
        self.Button_1to6_3.place(x=770, y=752, width=38, height=20)
        self.Button_1to6_4.place(x=620, y=790, width=20, height=38)
        self.Button_1to6_5.place(x=651, y=818, width=20, height=38)
        self.Button_1to6_6.place(x=681, y=843, width=20, height=38)

        # --------------------------------------------------------------------------------

        self.Battery_Variable = StringVar()
        self.Battery_Variable.set("100%")
        self.RAM_Variable = StringVar()
        self.RAM_Variable.set("100%")
        self.CPU_Variable = StringVar()
        self.CPU_Variable.set("100%")

        self.Battery_LBL = Label(self.root, textvariable=self.Battery_Variable, font=("Broadway", 20, 'bold'), bg="white", anchor=W)
        self.Battery_LBL.place(x=1325, y=490, width=125, height=50)

        self.RAM_LBL = Label(self.root, textvariable=self.RAM_Variable, font=("Agency FB", 15, 'bold'), bg="white", anchor=W)
        self.RAM_LBL.place(x=1337, y=540, width=125, height=50)

        self.CPU_LBL = Label(self.root, textvariable=self.CPU_Variable, font=("Agency FB", 15, 'bold'), bg="White", anchor=W)
        self.CPU_LBL.place(x=1325, y=590, width=125, height=50)

        # ------------------------------------------------------------------------

        self.Temperature_Variable = StringVar()
        self.Temperature_Variable.set("88 *C")
        self.WeatherType_Variable = StringVar()
        self.WeatherType_Variable.set("Mostly Sunny")
        self.Place_Variable = StringVar()
        self.Place_Variable.set("Pathri")

        self.Temperature_LBL = Label(self.root, textvariable=self.Temperature_Variable, font=("Broadway", 40, 'bold'), bg="White", anchor=W)
        self.WeatherType_LBL = Label(self.root, textvariable=self.WeatherType_Variable, font=("Agency FB", 20, 'bold'), bg="White", anchor=W)
        self.Place_LBL = Label(self.root, textvariable=self.Place_Variable, font=("Agency FB", 20, 'bold'), bg="White", anchor=W)

        self.Temperature_LBL.place(x=1262, y=291, width=312, height=87)
        self.WeatherType_LBL.place(x=1318, y=362, width=550, height=50)
        self.Place_LBL.place(x=1381, y=406, width=187, height=50)

        # ----------------------------------------------------------------------

        self.Time_Variable = StringVar()
        self.Time_Variable.set("88:88")
        self.Date_Variable = StringVar()
        self.Date_Variable.set("88 September 2022")
        self.Day_Variable = StringVar()
        self.Day_Variable.set("Wednesday")

        self.Time_LBL = Label(self.root, textvariable=self.Time_Variable, font=("Broadway", 50, 'bold'), bg="White", anchor=W)
        self.Date_LBL = Label(self.root, textvariable=self.Date_Variable, font=("Agency FB", 20, 'bold'), bg="White", anchor=W)
        self.Day_LBL = Label(self.root, textvariable=self.Day_Variable, font=("Agency FB", 20, 'bold'), bg="White", anchor=W)

        self.Time_LBL.place(x=1225, y=73, width=371, height=87)
        self.Date_LBL.place(x=1333, y=163, width=262, height=50)
        self.Day_LBL.place(x=1408, y=218, width=187, height=50)

        # ----------------------------------------------------------------------------
        self.paused = False
        self.i = 0

        path = "D:\\"
        self.songsList = os.listdir(path)
        self.SongListLength = len(self.songsList)
        self.num = randint(0, self.SongListLength - 1)

        self.MusicBtn_BG = PhotoImage(file=Music[0])
        self.MusicBtn = Button(self.root, image=self.MusicBtn_BG, relief=RIDGE, bg='White', bd=2, command=self.MusicBtn_Clicked)
        self.MusicBtn.place(x=165, y=727, width=55, height=55)

        self.PreviousBtn = Button(self.root, text="<", font="Ariel 10 bold", relief=RIDGE, bd=1, bg='White', command=self.PreviousBtn_Clicked)
        self.PreviousBtn.place(x=176, y=804, width=32, height=32)

        self.PausePlayBtn = Button(self.root, text="▶", font="Ariel 10 bold", relief=RIDGE, bd=1, bg='White', command=self.PausePlayBtn_Clicked)
        self.PausePlayBtn.place(x=176, y=859, width=32, height=32)

        self.NextBtn = Button(self.root, text=">", font="Ariel 10 bold", relief=RIDGE, bd=1, bg='White', command=self.NextBtn_Clicked)
        self.NextBtn.place(x=176, y=913, width=32, height=32)

        # --------------------------------------------------------------------------------

        self.buttonPair1_BG = PhotoImage(file=buttonPair[0][0])
        self.buttonPair2_BG = PhotoImage(file=buttonPair[1][0])

        self.buttonPair1Btn = Button(self.root, image=self.buttonPair1_BG, relief=RIDGE, bg="White", bd=1, command=lambda: self.openApplication(buttonPair[0][1]))
        self.buttonPair1Btn.place(x=312, y=795, width=55, height=55)

        self.buttonPair1Btn = Button(self.root, image=self.buttonPair2_BG, bg="White", relief=RIDGE, bd=1, command=lambda: self.openApplication(buttonPair[1][1]))
        self.buttonPair1Btn.place(x=312, y=875, width=55, height=55)

        # --------------------------------------------------------------------------------

        self.MikeBtn_BG = PhotoImage(file=Assistant[0])
        self.TickMarkBtn_BG = PhotoImage(file=Assistant[1])

        self.MikeBtn = Button(self.root, image=self.MikeBtn_BG, relief=RIDGE, bg="White", bd=2)
        self.MikeBtn.place(x=1166, y=695, width=57, height=57)

        self.CommandEntry = Entry(self.root, font="Ariel 15 bold", relief=RIDGE, bd=2, bg="White")
        self.CommandEntry.place(x=1193, y=779, width=298, height=43)

        self.TickMarkBtn = Button(self.root, image=self.TickMarkBtn_BG, relief=RIDGE, bd=2, bg="White")
        self.TickMarkBtn.place(x=1506, y=777, width=46, height=46)

        # -------------------------------------------------------------------------

        self.VolumeUpBtn = Button(self.root, text="🔊", font="ariel 12", bg="White", relief=RIDGE, bd=2, command=lambda: pyautogui.press("volumeup"))
        self.VolumeDownBtn = Button(self.root, text="🔉", font="ariel 12", bg="White", relief=RIDGE, bd=2, command=lambda: pyautogui.press("volumedown"))
        self.VolumeMuteBtn = Button(self.root, text="🔇", font="ariel 12", bg="White", relief=RIDGE, bd=2, command=lambda: pyautogui.press("volumemute"))

        self.BrightnessIBtn = Button(self.root, text="🔆+", font="ariel 10", bg="White", relief=RIDGE, bd=2, command=lambda: set_brightness(get_brightness() + 5) if(get_brightness()<=95) else None)
        self.BrightnessDBtn = Button(self.root, text="🔆-", font="ariel 10", bg="White", relief=RIDGE, bd=2, command=lambda: set_brightness(get_brightness() - 5) if(get_brightness()>=5) else None)

        self.Btn = Button(self.root, text="", relief=RIDGE, bd=2)

        self.VolumeUpBtn.place(x=1229, y=920, width=32, height=32)
        self.VolumeDownBtn.place(x=1282, y=920, width=32, height=32)
        self.VolumeMuteBtn.place(x=1336, y=920, width=32, height=32)
        self.BrightnessIBtn.place(x=1317, y=972, width=32, height=32)
        self.BrightnessDBtn.place(x=1371, y=972, width=32, height=32)

        self.Btn.place(x=1236, y=1021, width=32, height=32)

        # ---------------------------------------------------------------

        self.PowerOptionsBool = False

        self.PowerOption_BG = PhotoImage(file=powerMenu[0][0])
        self.ShutDown_BG = PhotoImage(file=powerMenu[1][0])
        self.Restart_BG = PhotoImage(file=powerMenu[2][0])
        self.LogOut_BG = PhotoImage(file=powerMenu[3][0])
        self.Sleep_BG = PhotoImage(file=powerMenu[4][0])

        self.PowerOptionFrame = Frame(self.root, bg='White')
        self.PowerOptionFrame.place(x=1611, y=60, width=306, height=61)
        PowerOptionBtn = Button(self.root, image=self.PowerOption_BG, relief=RIDGE, bd=4, command=self.PowerOption)
        PowerOptionBtn.place(x=1863, y=62, width=56, height=56)

        # ----------------------------------------------------------------

        self.LeftApplicationLineBtn_1_BG = PhotoImage(file=LeftApplicationLine[0][0])
        self.LeftApplicationLineBtn_2_BG = PhotoImage(file=LeftApplicationLine[1][0])
        self.LeftApplicationLineBtn_3_BG = PhotoImage(file=LeftApplicationLine[2][0])
        self.LeftApplicationLineBtn_4_BG = PhotoImage(file=LeftApplicationLine[3][0])
        self.LeftApplicationLineBtn_5_BG = PhotoImage(file=LeftApplicationLine[4][0])
        self.LeftApplicationLineBtn_6_BG = PhotoImage(file=LeftApplicationLine[5][0])
        self.LeftApplicationLineBtn_7_BG = PhotoImage(file=LeftApplicationLine[6][0])
        self.LeftApplicationLineBtn_8_BG = PhotoImage(file=LeftApplicationLine[7][0])
        self.LeftApplicationLineBtn_9_BG = PhotoImage(file=LeftApplicationLine[8][0])
        self.LeftApplicationLineBtn_10_BG = PhotoImage(file=LeftApplicationLine[9][0])
        self.LeftApplicationLineBtn_11_BG = PhotoImage(file=LeftApplicationLine[10][0])
        self.LeftApplicationLineBtn_12_BG = PhotoImage(file=LeftApplicationLine[11][0])
        self.LeftApplicationLineBtn_13_BG = PhotoImage(file=LeftApplicationLine[12][0])
        self.LeftApplicationLineBtn_14_BG = PhotoImage(file=LeftApplicationLine[13][0])

        LeftApplicationLineBtn_1 = Button(self.root, image=self.LeftApplicationLineBtn_1_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[0][1]))
        LeftApplicationLineBtn_2 = Button(self.root, image=self.LeftApplicationLineBtn_2_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[1][1]))
        LeftApplicationLineBtn_3 = Button(self.root, image=self.LeftApplicationLineBtn_3_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[2][1]))
        LeftApplicationLineBtn_4 = Button(self.root, image=self.LeftApplicationLineBtn_4_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[3][1]))
        LeftApplicationLineBtn_5 = Button(self.root, image=self.LeftApplicationLineBtn_5_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[4][1]))
        LeftApplicationLineBtn_6 = Button(self.root, image=self.LeftApplicationLineBtn_6_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[5][1]))
        LeftApplicationLineBtn_7 = Button(self.root, image=self.LeftApplicationLineBtn_7_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[6][1]))
        LeftApplicationLineBtn_8 = Button(self.root, image=self.LeftApplicationLineBtn_8_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[7][1]))
        LeftApplicationLineBtn_9 = Button(self.root, image=self.LeftApplicationLineBtn_9_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[8][1]))
        LeftApplicationLineBtn_10 = Button(self.root, image=self.LeftApplicationLineBtn_10_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[9][1]))
        LeftApplicationLineBtn_11 = Button(self.root, image=self.LeftApplicationLineBtn_11_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[10][1]))
        LeftApplicationLineBtn_12 = Button(self.root, image=self.LeftApplicationLineBtn_12_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[11][1]))
        LeftApplicationLineBtn_13 = Button(self.root, image=self.LeftApplicationLineBtn_13_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[12][1]))
        LeftApplicationLineBtn_14 = Button(self.root, image=self.LeftApplicationLineBtn_14_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(LeftApplicationLine[13][1]))

        LeftApplicationLineBtn_1.place(x=0, y=125, width=56, height=56)
        LeftApplicationLineBtn_2.place(x=0, y=187, width=56, height=56)
        LeftApplicationLineBtn_3.place(x=0, y=250, width=56, height=56)
        LeftApplicationLineBtn_4.place(x=0, y=375, width=56, height=56)
        LeftApplicationLineBtn_5.place(x=0, y=437, width=56, height=56)
        LeftApplicationLineBtn_6.place(x=0, y=500, width=56, height=56)
        LeftApplicationLineBtn_7.place(x=0, y=560, width=56, height=56)
        LeftApplicationLineBtn_8.place(x=0, y=625, width=56, height=56)
        LeftApplicationLineBtn_9.place(x=0, y=687, width=56, height=56)
        LeftApplicationLineBtn_10.place(x=0, y=750, width=56, height=56)
        LeftApplicationLineBtn_11.place(x=0, y=812, width=56, height=56)
        LeftApplicationLineBtn_12.place(x=0, y=875, width=56, height=56)
        LeftApplicationLineBtn_13.place(x=0, y=937, width=56, height=56)
        LeftApplicationLineBtn_14.place(x=0, y=1000, width=56, height=56)

        # ----------------------------------------------------------------

        self.ApplicationsRightBtn_1_BG = PhotoImage(file=ApplicationsRight[0][0])
        self.ApplicationsRightBtn_2_BG = PhotoImage(file=ApplicationsRight[1][0])
        self.ApplicationsRightBtn_3_BG = PhotoImage(file=ApplicationsRight[2][0])
        self.ApplicationsRightBtn_4_BG = PhotoImage(file=ApplicationsRight[3][0])
        self.ApplicationsRightBtn_5_BG = PhotoImage(file=ApplicationsRight[4][0])
        self.ApplicationsRightBtn_6_BG = PhotoImage(file=ApplicationsRight[5][0])
        self.ApplicationsRightBtn_7_BG = PhotoImage(file=ApplicationsRight[6][0])
        self.ApplicationsRightBtn_8_BG = PhotoImage(file=ApplicationsRight[7][0])
        self.ApplicationsRightBtn_9_BG = PhotoImage(file=ApplicationsRight[8][0])
        self.ApplicationsRightBtn_10_BG = PhotoImage(file=ApplicationsRight[9][0])
        self.ApplicationsRightBtn_11_BG = PhotoImage(file=ApplicationsRight[10][0])
        self.ApplicationsRightBtn_12_BG = PhotoImage(file=ApplicationsRight[11][0])
        self.ApplicationsRightBtn_13_BG = PhotoImage(file=ApplicationsRight[12][0])

        ApplicationsRightBtn_1 = Button(self.root, image=self.ApplicationsRightBtn_1_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[0][1]))
        ApplicationsRightBtn_2 = Button(self.root, image=self.ApplicationsRightBtn_2_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[1][1]))
        ApplicationsRightBtn_3 = Button(self.root, image=self.ApplicationsRightBtn_3_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[2][1]))
        ApplicationsRightBtn_4 = Button(self.root, image=self.ApplicationsRightBtn_4_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[3][1]))
        ApplicationsRightBtn_5 = Button(self.root, image=self.ApplicationsRightBtn_5_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[4][1]))
        ApplicationsRightBtn_6 = Button(self.root, image=self.ApplicationsRightBtn_6_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[5][1]))
        ApplicationsRightBtn_7 = Button(self.root, image=self.ApplicationsRightBtn_7_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[6][1]))
        ApplicationsRightBtn_8 = Button(self.root, image=self.ApplicationsRightBtn_8_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[7][1]))
        ApplicationsRightBtn_9 = Button(self.root, image=self.ApplicationsRightBtn_9_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[8][1]))
        ApplicationsRightBtn_10 = Button(self.root, image=self.ApplicationsRightBtn_10_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[9][1]))
        ApplicationsRightBtn_11 = Button(self.root, image=self.ApplicationsRightBtn_11_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[10][1]))
        ApplicationsRightBtn_12 = Button(self.root, image=self.ApplicationsRightBtn_12_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[11][1]))
        ApplicationsRightBtn_13 = Button(self.root, image=self.ApplicationsRightBtn_13_BG, relief=RIDGE, bd=4, bg="White", command=lambda: self.openApplication(ApplicationsRight[12][1]))

        ApplicationsRightBtn_1.place(x=1748, y=447, width=55, height=55)
        ApplicationsRightBtn_2.place(x=1633, y=510, width=55, height=55)
        ApplicationsRightBtn_3.place(x=1858, y=510, width=55, height=55)
        ApplicationsRightBtn_4.place(x=1748, y=572, width=55, height=55)
        ApplicationsRightBtn_5.place(x=1633, y=635, width=55, height=55)
        ApplicationsRightBtn_6.place(x=1858, y=635, width=55, height=55)
        ApplicationsRightBtn_7.place(x=1750, y=697, width=55, height=55)
        ApplicationsRightBtn_8.place(x=1635, y=760, width=55, height=55)
        ApplicationsRightBtn_9.place(x=1860, y=760, width=55, height=55)
        ApplicationsRightBtn_10.place(x=1750, y=822, width=55, height=55)
        ApplicationsRightBtn_11.place(x=1635, y=885, width=55, height=55)
        ApplicationsRightBtn_12.place(x=1860, y=885, width=55, height=55)
        ApplicationsRightBtn_13.place(x=1750, y=949, width=55, height=55)

        # ----------------------------------------------------------------

        self.ApplicationsBottomBtn_1_BG = PhotoImage(file=ApplicationsBottom[0][0])
        self.ApplicationsBottomBtn_2_BG = PhotoImage(file=ApplicationsBottom[1][0])
        self.ApplicationsBottomBtn_3_BG = PhotoImage(file=ApplicationsBottom[2][0])
        self.ApplicationsBottomBtn_4_BG = PhotoImage(file=ApplicationsBottom[3][0])
        self.ApplicationsBottomBtn_5_BG = PhotoImage(file=ApplicationsBottom[4][0])
        self.ApplicationsBottomBtn_6_BG = PhotoImage(file=ApplicationsBottom[5][0])
        self.ApplicationsBottomBtn_7_BG = PhotoImage(file=ApplicationsBottom[6][0])
        self.ApplicationsBottomBtn_8_BG = PhotoImage(file=ApplicationsBottom[7][0])
        self.ApplicationsBottomBtn_9_BG = PhotoImage(file=ApplicationsBottom[8][0])
        self.ApplicationsBottomBtn_10_BG = PhotoImage(file=ApplicationsBottom[9][0])
        self.ApplicationsBottomBtn_11_BG = PhotoImage(file=ApplicationsBottom[10][0])
        self.ApplicationsBottomBtn_12_BG = PhotoImage(file=ApplicationsBottom[11][0])
        self.ApplicationsBottomBtn_13_BG = PhotoImage(file=ApplicationsBottom[12][0])

        self.ApplicationsBottomBtn_1 = Button(self.root, image=self.ApplicationsBottomBtn_1_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[0][1]))
        self.ApplicationsBottomBtn_2 = Button(self.root, image=self.ApplicationsBottomBtn_2_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[1][1]))
        self.ApplicationsBottomBtn_3 = Button(self.root, image=self.ApplicationsBottomBtn_3_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[2][1]))
        self.ApplicationsBottomBtn_4 = Button(self.root, image=self.ApplicationsBottomBtn_4_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[3][1]))
        self.ApplicationsBottomBtn_5 = Button(self.root, image=self.ApplicationsBottomBtn_5_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[4][1]))
        self.ApplicationsBottomBtn_6 = Button(self.root, image=self.ApplicationsBottomBtn_6_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[5][1]))
        self.ApplicationsBottomBtn_7 = Button(self.root, image=self.ApplicationsBottomBtn_7_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[6][1]))
        self.ApplicationsBottomBtn_8 = Button(self.root, image=self.ApplicationsBottomBtn_8_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[7][1]))
        self.ApplicationsBottomBtn_9 = Button(self.root, image=self.ApplicationsBottomBtn_9_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[8][1]))
        self.ApplicationsBottomBtn_10 = Button(self.root, image=self.ApplicationsBottomBtn_10_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[9][1]))
        self.ApplicationsBottomBtn_11 = Button(self.root, image=self.ApplicationsBottomBtn_11_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[10][1]))
        self.ApplicationsBottomBtn_12 = Button(self.root, image=self.ApplicationsBottomBtn_12_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[11][1]))
        self.ApplicationsBottomBtn_13 = Button(self.root, image=self.ApplicationsBottomBtn_13_BG, relief=RIDGE, bd=1, bg="White", command=lambda: self.openApplication(ApplicationsBottom[12][1]))

        self.ApplicationsBottomBtn_1.place(x=480, y=945, width=55, height=55)
        self.ApplicationsBottomBtn_2.place(x=547, y=877, width=55, height=55)
        self.ApplicationsBottomBtn_3.place(x=547, y=1012, width=55, height=55)
        self.ApplicationsBottomBtn_4.place(x=615, y=945, width=55, height=55)
        self.ApplicationsBottomBtn_5.place(x=682, y=1012, width=55, height=55)
        self.ApplicationsBottomBtn_6.place(x=750, y=946, width=55, height=55)
        self.ApplicationsBottomBtn_7.place(x=816, y=880, width=55, height=55)
        self.ApplicationsBottomBtn_8.place(x=816, y=1011, width=55, height=55)
        self.ApplicationsBottomBtn_9.place(x=950, y=748, width=55, height=55)
        self.ApplicationsBottomBtn_10.place(x=883, y=813, width=55, height=55)
        self.ApplicationsBottomBtn_11.place(x=950, y=879, width=55, height=55)
        self.ApplicationsBottomBtn_12.place(x=883, y=946, width=55, height=55)
        self.ApplicationsBottomBtn_13.place(x=948, y=1011, width=55, height=55)

        # ----------------------------------------------------------------
        self.SearchOptionBool = False
        self.SearchOption_BG = PhotoImage(file="Images\SearchOption.png")
        self.SearchOptionFrame = Frame(self.root, bg='White')
        self.SearchOptionFrame.place(x=1611, y=185, width=306, height=61)
        SearchOptionBtn = Button(self.root, image=self.SearchOption_BG, relief=RIDGE, bd=4, command=self.SearchOption)
        SearchOptionBtn.place(x=1863, y=187, width=56, height=56)
        # ----------------------------------------------------------------
        self.News = ['News Here']
        self.NewsOptionBool = False
        self.NewsOption_BG = PhotoImage(file=NewsHeadlines[0])
        self.NewsOptionFrame = Frame(self.root, bg='White')
        self.NewsOptionFrame.place(x=0, y=0, width=1860, height=61)
        NewsOptionBtn = Button(self.root, image=self.NewsOption_BG, relief=RIDGE,bg="White", bd=4, command=self.NewsOption)
        NewsOptionBtn.place(x=0, y=2, width=56, height=56)
        # ----------------------------------------------------------------
        self.PcStatus()
        self.TimeDateDay()
        self.Weather()
        self.NewsGet()

    def NewsGet(self):
        main_url = NewsHeadlines[2]+ NewsHeadlines[1]
        news = requests.get(main_url).json()
        article = news["articles"]
        for arti in article:
            self.News.append(arti['title'])

    def NewsOption(self):
        if not self.NewsOptionBool:
            self.NewsOptionFrame.config(bg='yellow')

            self.NewsCMB = ttk.Combobox(self.root, value=self.News, font="Ariel 15 bold")
            self.NewsCMB.place(x=62, y=5, width=1795, height=51)
            self.NewsCMB.current(0)
            self.NewsOptionBool = True
        else:
            self.NewsOptionFrame.config(bg='white')
            self.NewsCMB.destroy()
            self.NewsOptionBool = False

    def SearchOption(self):
        if not self.SearchOptionBool:
            self.SearchOptionFrame.config(bg='yellow')
            self.SearchEntry = Entry(self.root, font="Ariel 15 bold", relief=RIDGE, bd=2)
            self.SearchEntry.place(x=1613, y=191, width=243, height=51)
            self.SearchOptionBool = True
        else:
            if self.SearchEntry.get() == "":
                self.SearchOptionFrame.config(bg='white')
                self.SearchEntry.destroy()
                self.SearchOptionBool = False
            else:
                WbOpen(f"https://google.com/search?q={self.SearchEntry.get()}")
                self.SearchOptionFrame.config(bg='white')
                self.SearchEntry.destroy()
                self.SearchOptionBool = False

    def TimeDateDay(self):
        Dummy = Label(self.root)
        Time = datetime.now().strftime("%H:%M")
        Date = datetime.now().strftime("%d\%m\%y")
        Day = datetime.now().strftime("%A")

        self.Time_Variable.set(Time)
        self.Date_Variable.set(Date)
        self.Day_Variable.set(Day)

        h = str(strftime("%H"))
        m = str(strftime("%M"))

        if f"{h}:{m}" == '08:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '08:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '09:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '09:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '10:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '10:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '11:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '11:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '12:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '12:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '13:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '13:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '14:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '14:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '15:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '15:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '16:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '16:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '17:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '17:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '18:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '18:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '19:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '19:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '20:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '20:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '21:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '21:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '22:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '22:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '23:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '23:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '00:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '00:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '01:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '01:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '02:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '02:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '03:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '03:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '04:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '04:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '05:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '05:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '06:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '06:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '07:00':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        elif f"{h}:{m}" == '07:30':
            if not self.NotificationBool:
                self.notifyMe("Drink Water", "Drink Water")
                self.NotificationBool = True
        else:
            self.NotificationBool = False

        Dummy.after(30000, self.TimeDateDay)

    def PcStatus(self):
        Dummy = Label(self.root)
        battery = sensors_battery()
        ram = virtual_memory()[2]
        cpu = cpu_percent(4)

        if str(battery[2]) == 'False':
            self.Battery_Variable.set(f"{battery[0]}%")
        else:
            self.Battery_Variable.set(f"{battery[0]}%  🔌")
        self.RAM_Variable.set(ram)
        self.CPU_Variable.set(cpu)

        Dummy.after(60000, self.PcStatus)

    def PowerOption(self):
        def ShutDown():
            a = messagebox.askyesno("Confirmation", "Are yo sure you want to ShutDown")
            if a == 1:
                print("ShutDown")
            else:
                print("OK")

        def Restart():
            a = messagebox.askyesno("Confirmation", "Are yo sure you want to Restart")
            if a == 1:
                print("Restart")
            else:
                print("OK")

        def LogOut():
            a = messagebox.askyesno("Confirmation", "Are yo sure you want to LogOut")
            if a == 1:
                print("LogOut")
            else:
                print("OK")

        def Sleep():
            a = messagebox.askyesno("Confirmation", "Are yo sure you want to go Sleep")
            if a == 1:
                print("Sleep")
            else:
                print("OK")

        if not self.PowerOptionsBool:
            self.PowerOptionFrame.config(bg='Yellow')
            self.ShutDownBtn = Button(self.root, image=self.ShutDown_BG, relief=RIDGE, bd=3, command=ShutDown)
            self.ShutDownBtn.place(x=1801, y=62, width=56, height=56)
            self.RestartBtn = Button(self.root, image=self.Restart_BG, relief=RIDGE, bd=3, command=Restart)
            self.RestartBtn.place(x=1738, y=62, width=56, height=56)
            self.SleepBtn = Button(self.root, image=self.Sleep_BG, relief=RIDGE, bd=3, command=Sleep)
            self.SleepBtn.place(x=1676, y=62, width=56, height=56)
            self.LogOutBtn = Button(self.root, image=self.LogOut_BG, relief=RIDGE, bd=3, command=LogOut)
            self.LogOutBtn.place(x=1613, y=62, width=56, height=56)
            self.PowerOptionsBool = True
        else:
            self.PowerOptionFrame.config(bg='White')
            self.ShutDownBtn.destroy()
            self.RestartBtn.destroy()
            self.SleepBtn.destroy()
            self.LogOutBtn.destroy()
            self.PowerOptionsBool = False

    def openApplication(self, X):
        if X != "":
            if 'start' in X:
                os.system(X)
            elif "https://" in X:
                WbOpen(X)
            else:
                os.startfile(X)

    def notifyMe(self, title, message):
        notification.notify(
            title=title,
            message=message,
            timeout=10
        )

    def Weather(self):
        Dummy = Label(self.root)
        url = WeatherUrl[0]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        location = soup.find(WeatherUrl[1][0], class_=WeatherUrl[1][1]).text
        temperature = soup.find(WeatherUrl[2][0], class_=WeatherUrl[2][1]).text
        weatherPrediction = soup.find(WeatherUrl[3][0], WeatherUrl[3][1]).text
        timelast = soup.find(WeatherUrl[4][0], class_=WeatherUrl[4][1]).text

        self.Temperature_Variable.set(temperature)
        self.WeatherType_Variable.set(f"{weatherPrediction}, {timelast}")
        self.Place_Variable.set(f"{location.split(',')[0]}")

        Dummy.after(600000, self.Weather)

    def Exit(self):
        self.root.destroy()
        exit()

    def playMusic(self):
        songF = self.songsList[self.num]
        self.song = f"D:\\songs\\{songF}"
        mixer.music.load(self.song)
        mixer.music.play(loops=1)

    def MusicBtn_Clicked(self):
        mixer.init()
        self.playMusic()

    def PreviousBtn_Clicked(self):
        self.paused = True
        self.PausePlayBtn_Clicked()
        if self.num == 0:
            self.num = len(self.songsList) - 1
            self.playMusic()
        else:
            self.num -= 1
            self.playMusic()

    def PausePlayBtn_Clicked(self):
        if self.paused:
            mixer.music.unpause()
            self.PausePlayBtn.config(text='▶')
            self.paused = False
        else:
            mixer.music.pause()
            self.PausePlayBtn.config(text='⏸')
            self.paused = True

    def NextBtn_Clicked(self):
        self.paused = True
        self.PausePlayBtn_Clicked()
        if self.num == len(self.songsList) - 1:
            self.num = 0
            self.playMusic()
        else:
            self.num += 1
            self.playMusic()


if __name__ == '__main__':
    root = Tk()
    obj = Desktop(root)
    root.overrideredirect(1)
    root.mainloop()