from tkinter import Tk, Button, Canvas
import tkinter.font
import pickle
from tkinter.messagebox import showinfo,showerror,showwarning,askyesno
import tkinter as tk
import datetime
import os
import time
import pyautogui
from tkinter.ttk import *
from tkinter import Tk, Checkbutton, IntVar
from PIL import Image, ImageFont
from tkinter import *
from PIL import *
from PIL import ImageTk
import tkinter
from PIL import ImageTk, Image


def a():
    root = Tk()
    root.title('zoom helper')
    root.geometry('{}x{}'.format(1000,520))

    frame_top    = Frame(root, width=300, height=70, bg="#424242")
    frame_top2    = Frame(root, width=800, height=70, bg="#424242")
    frame_top3    = Frame(root, width=1, height=70, bg="#424242")
    frame_left   = Label(root, width=500, height=70)
    frame_right  = Frame(root, width=800, height=490, bg="#DCDCDC")
    frame_center = Frame(root, width=1, height=490, bg="#424242")

    frame_top.grid  (row=1,column=1)
    frame_top2.grid  (row=1,column=3)
    frame_top3.grid  (row=1,column=2)
    frame_left.grid (row=2,column=1)
    frame_center.grid(row=2,column=2)
    frame_right.grid(row=2,column=3)

    font=tkinter.font.Font(family="Franklin Gothic Medium", size=19)
    font2=tkinter.font.Font(family="맑은 고딕", size=18,weight='bold')
    label_1 = Label(frame_top, text="Zoom Helper",fg='white',bg='#424242',width=20, height=2, font=font)
    label_1.grid(ipady=0)

    frame_label=Label(frame_left,width=35, height=30)
    frame_label.pack()


    #유저 인터페이스
    u1= Label(frame_label,text='환영합니다 User!',font=font2)
    u1.place(x=10, y=0)
    #버튼
    b1=tkinter.Button(frame_label,text='도움말',width=35, height=3,bg='white',command=helplabel)
    b1.place(x=0,y=290)

    b2=tkinter.Button(frame_label,text='드라이버 설정',width=35, height=3,bg='white',command=c)
    b2.place(x=0,y=350)

    #일정 버튼
    c1=tkinter.Button(frame_right,text='일정 1',width=100, height=3,bg='white',command=b)
    c1.place(x=10, y=10)

    c2=tkinter.Button(frame_right,text='일정 2',width=100, height=3,bg='white')
    c2.place(x=10, y=70)

    #label_1.grid(sticky="w")

    root.mainloop()

def b():
    window=tkinter.Toplevel()

    #기본 설정
    window.title("Zoom Helper")
    window.geometry("1512x550+100+100")  #너비X높이+X좌표+Y좌표
    window.resizable(False, False)      #사이즈 변경 가능
    window.configure(bg='#BCC6CC')

    #레이블
    LU_monday=tkinter.Label(window, text="월", width=30, height=2, fg="white", relief="ridge", bg='#38ACEC')
    LU_monday.grid(row=0, column=1)
    LU_tuesday=tkinter.Label(window, text="화", width=30, height=2, fg="white", relief="ridge", bg="#38ACEC")
    LU_tuesday.grid(row=0, column=2)
    LU_wednesday=tkinter.Label(window, text="수", width=30, height=2, fg="white", relief="ridge", bg="#38ACEC")
    LU_wednesday.grid(row=0, column=3)
    LU_thursday=tkinter.Label(window, text="목", width=30, height=2, fg="white", relief="ridge", bg="#38ACEC")
    LU_thursday.grid(row=0, column=4)
    LU_friday=tkinter.Label(window, text="금", width=30, height=2, fg="white", relief="ridge", bg="#38ACEC")
    LU_friday.grid(row=0, column=5)
    LU_saturday=tkinter.Label(window, text="토", width=30, height=2, fg="white", relief="ridge", bg="#38ACEC")
    LU_saturday.grid(row=0, column=6)
    LU_sunday=tkinter.Label(window, text="일", width=30, height=2, fg="white", relief="ridge", bg="#38ACEC")
    LU_sunday.grid(row=0, column=7)

    L_monday=tkinter.Label(window ,width=30, height=30, relief="groove",bg="#FEFCFF")
    L_monday.grid(row=1, column=1,sticky="NESW")
    L_tuesday=tkinter.Label(window, width=30, height=30, relief="groove", bg="#FEFCFF")
    L_tuesday.grid(row=1, column=2,sticky="NESW")
    L_wednesday=tkinter.Label(window, width=30, height=30, relief="groove", bg="#FEFCFF")
    L_wednesday.grid(row=1, column=3,sticky="NESW")
    L_thursday=tkinter.Label(window, width=30, height=30, relief="groove", bg="#FEFCFF")
    L_thursday.grid(row=1, column=4,sticky="NESW")
    L_friday=tkinter.Label(window, width=30, height=30, relief="groove", bg="#FEFCFF")
    L_friday.grid(row=1, column=5,sticky="NESW")
    L_saturday=tkinter.Label(window, width=30, height=30, relief="groove", bg="#FEFCFF")
    L_saturday.grid(row=1, column=6,sticky="NESW")
    L_sunday=tkinter.Label(window, width=30, height=30, relief="groove", bg="#FEFCFF")
    L_sunday.grid(row=1, column=7,sticky="NESW")

    ###-월 ㅡ 1-###

    #이름 (받는방법: m*_name.get() )
    m1_name=StringVar(window)
    m1_name.set('아직 정해지지 않은 알람')
    #줌 코드 (받는방법: m*_code.get() )
    m1_code=StringVar(window)
    m1_code.set('**********')
    #줌 비밀번호 (받는방법: m*_pass.get() )
    m1_pass=StringVar(window)
    m1_pass.set('*****')
    #시간1, (받는방법: m*_time.get() )
    m1_time=StringVar(window)
    m1_time.set('00:00')
    #오디오
    m1_audio=StringVar(window)
    m1_audio.set(0)

    #내부설정
    def WM1Open():
        WM1= Toplevel()
        WM1.title("시간 설정")
        WM1.geometry("320x190+100+100")  #너비X높이+X좌표+Y좌표
        WM1.resizable(False, False)        #사이즈 변경 가능
        WM1.configure(bg='white')

        #----라벨----#
        #이름
        M1_1L = tk.Label(WM1, text='알람 이름:')
        M1_1L.place(x=10,y=10)
        #줌 코드
        M1_2L = tk.Label(WM1, text='줌 코드:')
        M1_2L.place(x=10,y=40)
        #줌 비밀번호
        M1_3L = tk.Label(WM1, text='줌 비밀번호:')
        M1_3L.place(x=10,y=70)
        #시간
        M1_4L = tk.Label(WM1, text='시간:')
        M1_4L.place(x=10,y=100)
        #오디오
        M1_5L = tk.Label(WM1, text='오디오:')
        M1_5L.place(x=10,y=130)
        #비디오
        M1_6L = tk.Label(WM1, text='비디오:')
        M1_6L.place(x=10,y=160)

        #----엔트리----#
        #이름 
        M1_1var = StringVar(WM1, value=m1_name.get())
        M1_1WE = tk.Entry(WM1, textvariable = M1_1var)
        M1_1WE.place(x=100,y=10)
        #줌 코드
        M1_2var = StringVar(WM1, value=m1_code.get())
        M1_2WE = tk.Entry(WM1, textvariable = M1_2var,)
        M1_2WE.place(x=100,y=40)
        #줌 비밀번호
        M1_3var = StringVar(WM1, value=m1_pass.get())
        M1_3WE = tk.Entry(WM1, textvariable = M1_3var)
        M1_3WE.place(x=100,y=70)
        #시간
        M1_4var = StringVar(WM1, value=m1_time.get())
        M1_4WE = tk.Entry(WM1, textvariable = M1_4var)
        M1_4WE.place(x=100,y=100,width=40)

        #----변수----#
        #이름
        def M1_1btn():
            m1_name.set(M1_1var.get())
            B_monday1_1.configure(text=M1_1var.get())

        #줌 코드
        def M1_2btn():
            m1_code.set(M1_2var.get())

        #줌 비밀번호
        def M1_3btn():
            m1_pass.set(M1_3var.get())

        #시간
        def M1_4btn():
            m1_time.set(M1_4var.get())

        #----버튼----#
        #이름
        M1Wbtn = tk.Button(WM1, text = "확인", command=M1_1btn,relief="groove")
        M1Wbtn.place(x=270,y=8)
        #줌 코드
        M2Wbtn = tk.Button(WM1, text = "확인", command=M1_2btn,relief="groove")
        M2Wbtn.place(x=270,y=38)
        #줌 비밀번호
        M3Wbtn = tk.Button(WM1, text = "확인", command=M1_3btn,relief="groove")
        M3Wbtn.place(x=270,y=68)
        #시간
        M4btn = tk.Button(WM1, text = "확인", command=M1_4btn,relief="groove")
        M4btn.place(x=270,y=98)

        #---체크박스---#
        #오디오 (받는방법=> 켜짐: self.var_ma1.get()==1 / 꺼짐: self.var_ma1.get()==0
        class Audio_M1:
            def __init__(self, window2):
                self.var_ma1 = IntVar()
                self.c_ma1 = Checkbutton(
                    window2, text="체크",bg='white',
                    command=lambda:self.toggle(self.var_ma1))
                self.c_ma1.place(x=100,y=130)

            def toggle(self, var_ma1):
                var_ma1.set(not var_ma1.get())
                print(var_ma1.get())

        gui = Audio_M1(WM1)

        #비디오 (받는방법=> 켜짐: self.var_mv1.get()==1 / 꺼짐: self.var_mv1.get()==0
        class Video_M1:
            def __init__(self, window3):
                self.var_mv1 = IntVar()
                self.c_mv1 = Checkbutton(
                    window3, text="체크",bg='white',
                    command=lambda:self.toggle(self.var_mv1))
                self.c_mv1.place(x=100,y=160)

            def toggle(self, var_mv1):
                var_mv1.set(not var_mv1.get())
                print(var_mv1.get())

        gui2 = Video_M1(WM1)

        WM1.mainloop()

    #켜기/끄기 (o/x)

    Ma = IntVar()
    Ma.set(0)

    def switchButtonState1():
        #스위치 잠금/잠금해제 
        if (B_monday1_1['state'] == tk.NORMAL):
            B_monday1_1['state'] = tk.DISABLED
        else:
            B_monday1_1['state'] = tk.NORMAL

        #스위치 이미지
        if Ma.get()==0:
            path= file ="/Users/VIP/Desktop/visual code/switch_on.png"
            my_img = Image.open(path)
            my_img = my_img.resize((35, 18), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(my_img)
            B_monday1_2.configure(image=img)
            B_monday1_2.image = img # keep a reference!
            Ma.set(1)

        else:
            path= file ="/Users/VIP/Desktop/visual code/switch_off.png"
            my_img = Image.open(path)
            my_img = my_img.resize((35, 18), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(my_img)
            B_monday1_2.configure(image=img)
            B_monday1_2.image = img # keep a reference!
            Ma.set(0)
        
    
            

    #버튼 설정
    B_monday1_1 = tk.Button(L_monday, text=m1_name.get(),width=10, height=5,state=tk.DISABLED, command = WM1Open,relief="ridge",bg='white')
    #복붙할때 이부분은 전 교시 공통으로 쓰이기에 복붙 X
    path= file ="/Users/VIP/Desktop/visual code/switch_off.png"
    my_img = Image.open(path)
    my_img = my_img.resize((35, 18), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(my_img)

    B_monday1_2 = tk.Button(L_monday, image=img,relief="ridge",bg='white')
    B_monday1_1.place(x=0,y=0, width=170, height=50)
    B_monday1_2.place(x=161,y=0,width=50, height=50)
    B_monday1_2.configure(command=switchButtonState1)

    def wholething():
        driverlist = [("1.","A:/"),

        
                        ("2.","B:/"),
                        ("3.","C:/"),
                        ("4.","D:/"),
                        ("5.","E:/"),
                        ("6.","F:/"),
                        ("7.","G:/"),
                        ("8.","H:/"),
                        ("9.","I:/"),
                        ("10.","J:/"),
                        ("11.","K:/"),
                        ("12.","L:/"),
                        ("13.","M:/"),
                        ("14.","N:/"),
                        ("15.","O:/"),
                        ("16.","P:/"),
                        ("17.","Q:/"),
                        ("18.","R:/"),
                        ("19.","S:/"),
                        ("20.","T:/"),
                        ("21.","U:/"),
                        ("22.","V:/"),
                        ("23.","W:/"),
                        ("24.","X:/"),
                        ("25.","Y:/"),
                        ("26.","Z:/")]

        drives = []
        drivetestlist = []
        duplicatelist = []

        drivetest = []

        def checkdrive():
            for Num,Name in driverlist:
                print(Num,"=",Name)
            print()

            validdriver = False 
            while validdriver == False:
                try:
                    driverchoice = input("please Select the driver where zoom.exe is installed: ")
                    if driverchoice == "quit" or driverchoice == 'Quit' or driverchoice == "QUIT":
                        return
                    elif int(driverchoice) < 1 or int(driverchoice) > 27:
                        print("This number is not availble")
                    else:
                        driver = driverlist[int(driverchoice) - 1]
                        validdriver = True
                except:
                    print("Please enter number")

                check = (str(driver[1]))

                confirmeddrive = False
                while confirmeddrive == False:
                    try:
                        print("here is your drive set:")
                        print(check)
                        confirm = input("Is this driveset correct? Please confirm. Y/N ")
                        if confirm == "N" or confirm == "n" or confirm == "No" or confirm == "NO" or confirm == "no":
                            return
                        elif confirm == "Y" or confirm == "y" or confirm == "Yes" or confirm == "YES" or confirm == "yes":
                            confirmeddrive = True
                            drivetestlist.append(drivetest)
                            if drive not in drives:
                                drives.append(drive)
                                duplicatelist.append(drives)
                            else:
                                print("That seems to be a duplicate.")
                        else:
                            print("That isn't a valid answer.")
                            continue
                    except:
                        print()

                check = (str(driver[1]))

            start = True
            if start:
                check = (str(driver[1]))
                print('working...')
                target_filename = "Zoom.exe"
                start_folder = check 
                for root, dirs, files in os.walk(start_folder):
                    if target_filename in files:
                        file = (root + '\\' + target_filename )
                        os.startfile(file)

                        time.sleep(2)

                        i = pyautogui.locateOnScreen('zoomtest1.png')                                   

                        q = pyautogui.center(i)
                        pyautogui.click(q)

                        time.sleep(3)

                        i = pyautogui.locateOnScreen('zoomtest2.png')

                        q = pyautogui.center(i)
                        pyautogui.click(q)

                        pyautogui.typewrite(m1_code.get())

                        time.sleep(1)

                        i = pyautogui.locateOnScreen('zoomtest5.png')

                        q = pyautogui.center(i)
                        pyautogui.click(q)

                        time.sleep(2)

                        i = pyautogui.locateOnScreen('zoomtest3.png')

                        q = pyautogui.center(i)
                        pyautogui.click(q)

                        time.sleep(2)

                        pyautogui.typewrite(m1_pass.get())

                        time.sleep(1)

                        i = pyautogui.locateOnScreen('zoomtest4.png')

                        q = pyautogui.center(i)
                        pyautogui.click(q)
                        break        
                else: 
                    print('cant find Zoom.exe plese restart the program or send error code to us')
                    return checkdrive()

        def countdown(t): 
            
            while t: 
                mins, secs = divmod(t, 60) 
                timer = '{:02d}:{:02d}'.format(mins, secs) 
                print(timer, end="\r") 
                time.sleep(1) 
                t -= 1

            print('loading')
        
        t = 60

        def check_alarm_input(alarm_time):
            """Checks to see if the user has entered in a valid alarm time"""
            if len(alarm_time) == 1: 
                if alarm_time[0] < 24 and alarm_time[0] >= 0:
                    return True
            if len(alarm_time) == 2: 
                if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                alarm_time[1] < 60 and alarm_time[1] >= 0:
                    return True
            elif len(alarm_time) == 3: 
                if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                alarm_time[1] < 60 and alarm_time[1] >= 0 and \
                alarm_time[2] < 60 and alarm_time[2] >= 0:
                    return True
            return False

        print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
        while True:
            alarm_input = m1_time.get()
            try:
                alarm_time = [int(n) for n in alarm_input.split(":")]
                if check_alarm_input(alarm_time):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("ERROR: Enter time in HH:MM or HH:MM:SS format")

        seconds_hms = [3600, 60, 1] 
        alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

        now = datetime.datetime.now()
        current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

        time_diff_seconds = alarm_seconds - current_time_seconds

        if time_diff_seconds < 0:
            time_diff_seconds += 86400 

        print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))
        
        alarm_finish = (time_diff_seconds - 60)
        time.sleep(alarm_finish)
        countdown(t)

        print("start")
        checkdrive()

    '''임시 실행버튼'''
    B_monday_Test_btn = tk.Button(window, text="실행", command=wholething)
    B_monday_Test_btn.place(x=100,y=500, width=50, height=50)

    #저장 버튼
    def on_button_clicked(number):
        print("{} was clicked".format(number))

    button1 = tkinter.Button(window, text='저장', command=lambda: on_button_clicked(1))
    button2 = tkinter.Button(window, text='초기화', command=lambda: on_button_clicked(2))
    button1.grid(row=2, column=4, sticky="NESW")
    button2.grid(row=3, column=4, sticky="NESW")

    #뒤로가기 버튼
    tkinter.Button(window, text="확인", width=7 ,command=window.destroy).place(x=180,y=500)
    #초기화 버튼
    

    window.mainloop()

def c():
    OptionList = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "                                            "
    ]

    DM1 = Toplevel()
    DM1.title("드라이버 선택창")
    DM1.geometry("250x600+100+100")  #너비X높이+X좌표+Y좌표
    DM1.resizable(False, False)

    D_var1 = tk.StringVar(DM1)
    D_var1.set(OptionList[0])
    D_L = tk.Label(DM1,text='드라이버를 선택하시오:')
    D_L.pack(side="top")
    D_opt = tk.OptionMenu(DM1, D_var1, *OptionList)
    D_opt.config(width=90, font=('Helvetica', 12),bg='white',relief="ridge")
    D_opt["menu"].config(bg="white",font=('Helvetica', 10), relief="ridge")
    D_opt["menu"].insert_separator(1)
    D_opt["menu"].insert_separator(3)
    D_opt["menu"].insert_separator(5)
    D_opt["menu"].insert_separator(7)
    D_opt["menu"].insert_separator(9)
    D_opt["menu"].insert_separator(11)
    D_opt["menu"].insert_separator(13)
    D_opt["menu"].insert_separator(15)
    D_opt["menu"].insert_separator(17)
    D_opt["menu"].insert_separator(19)
    D_opt["menu"].insert_separator(21)
    D_opt["menu"].insert_separator(23)
    D_opt["menu"].insert_separator(25)
    D_opt["menu"].insert_separator(27)
    D_opt["menu"].insert_separator(29)
    D_opt["menu"].insert_separator(31)
    D_opt["menu"].insert_separator(33)
    D_opt["menu"].insert_separator(35)
    D_opt["menu"].insert_separator(37)
    D_opt["menu"].insert_separator(39)
    D_opt["menu"].insert_separator(41)
    D_opt["menu"].insert_separator(43)
    D_opt["menu"].insert_separator(45)
    D_opt["menu"].insert_separator(47)
    D_opt["menu"].insert_separator(49)
    D_opt["menu"].insert_separator(51)

    D_opt.pack(side="top")

    labelTest = tk.Label(text="", font=('Helvetica', 10), fg='red')
    labelTest.grid()

    path2= file ="/Users/VIP/Desktop/visual code/1-864px-Black_triangle.png"
    label_img = Image.open(path2)
    label_img = label_img.resize((13, 7), Image.ANTIALIAS)
    D_img = ImageTk.PhotoImage(label_img)
    
    labelimage= tk.Label(DM1, image=D_img,bg='white').place(x=225,y=34)
    tkinter.Button(DM1, text="확인", width=7 ,command=DM1.destroy).place(x=180,y=70)

    def callback(*args):
        labelTest.configure(DM1, text="드라이버 {} 선택됨.".format(D_var1.get()))

    D_var1.trace("w", callback)

    DM1.mainloop()
    
def helplabel():
        helpbox=tkinter.Tk()
        helpbox.title("도움말")
        helpbox.geometry("500x300+700+350")  #너비X높이+X좌표+Y좌표
        helpbox.resizable(False, False)
        helpbox.mainloop()
a()
