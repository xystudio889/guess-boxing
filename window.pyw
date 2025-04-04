from tkinter import *
from random import choice
from time import sleep
from tkinter import messagebox
from os import path
from pathlib import Path

hard = 1
folder = Path(__file__).parent.resolve()
boxing_list = ['石头','剪刀','布']

def back_beta():
    beta_win.destroy()

def beta():
    global beta_win,beta_mode,hard

    beta_mode  =  False
    back = Button(beta_win,text = '关闭软件',bg = 'light green',command = back_beta)

    back.grid(row=2,column=4)

    beta_win.mainloop()

def hard1OK():
    if me_boxing.get == '':
        messagebox.showerror(title = '未选拳',message = '请先选拳')
    else:
        if me_boxing.get() in boxing_list:
            AIBoxing.delete(0,END)
            AIBoxing.insert(0,'正在选拳...')
            sleep(1)
            AIBoxing.delete(0,END)
            AIBoxing.insert(0,choice(boxing_list))
            if me_boxing.get() == AIBoxing.get():
                messagebox.showinfo(title = '猜拳结果',message = '平局')
            elif ((me_boxing.get() == '石头' and AIBoxing.get() == '剪刀')
                or (me_boxing.get() == '剪刀' and AIBoxing.get() == '布')
                or (me_boxing.get() == '布' and AIBoxing.get() == '石头')):
                    messagebox.showinfo(title = '猜拳结果',message = '你赢了')
            else:
                messagebox.showinfo(title = '猜拳结果',message = '你输了')
        else:
            messagebox.showerror(title = '猜拳类型错误',message = '请选择选项内的拳')
        me_boxing.delete(0,END)
        AIBoxing.delete(0,END)
    
def hard2OK():
    boxing_list = ['石头','剪刀','布']
    if me_boxing2.get == '':
        messagebox.showerror(title = '未选拳',message = '请先选拳')
    else:
        if me_boxing2.get() in boxing_list:
            AI2Boxing.delete(0,END)
            AI2Boxing.insert(0,'正在选拳...')
            sleep(1)
            if me_boxing2.get() == '石头':
                AI2Boxing.delete(0,END)
                AI2Boxing.insert(0,'布')
            if me_boxing2.get() == '剪刀':
                AI2Boxing.delete(0,END)
                AI2Boxing.insert(0,'石头')
            if me_boxing2.get() == '布':
                AI2Boxing.delete(0,END)
                AI2Boxing.insert(0,'剪刀')
            messagebox.showinfo(title = '猜拳结果',message = '你输了')
        else:
            messagebox.showerror(title = '猜拳类型错误',message = '请选择选项内的拳')
        me_boxing2.delete(0,END)
        AI2Boxing.delete(0,END)

def AIChoose(me_boxing:str):
    if hard  == 1:
        me_boxing.delete(0,END)
        me_boxing.insert(0,me_boxing)
    elif hard  == 2:
        me_boxing2.delete(0,END)
        me_boxing2.insert(0,me_boxing)

def Rock():
    AIChoose('石头')

def Scissor():
    AIChoose('剪刀')

def Paper():
    AIChoose('布')

def hard1Go():
    global me_boxing,AIBoxing,goWin

    beta_win.destroy()
    goWin = Tk()
    goWin.title('猜拳')

    title2 = Label(goWin,text = '猜拳',font = ('微软雅黑',28))
    AI = Button(goWin,text = '对方',font = ('微软雅黑',24))
    me = Button(goWin,text = '我方',font = ('微软雅黑',24))
    me_boxing = Entry(goWin)
    AIBoxing = Entry(goWin)
    rock = Button(goWin,text = '石头',font = ('微软雅黑',20),command = Rock)
    scissor = Button(goWin,text = '剪刀',font = ('微软雅黑',20),command = Scissor)
    paper = Button(goWin,text = '布',font = ('微软雅黑',20),command = Paper)
    ok = Button(goWin,text = '点击完成',font = ('微软雅黑',25),command = hard1OK)

    title2.grid(row=0,columnspan=3)
    AI.grid(row=3,column=3,rowspan=2)
    me.grid(row=3,column=0,rowspan=2)
    me_boxing.grid(row=6,column=0)
    AIBoxing.grid(row=6,column=3)
    rock.grid(row=7,column=0)
    scissor.grid(row=7,column=1)
    paper.grid(row=7,column=3)
    ok.grid(row=8,column=1)

    goWin.mainloop()

def hard2Go():
    global me_boxing2,AI2Boxing,goWin2,hard

    hard = 2

    # beta_win.destroy()

    goWin2 = Toplevel(beta_win)
    goWin2.title('猜拳')

    title2 = Label(goWin2,text = '猜拳',font = ('微软雅黑',28))
    AI = Button(goWin2,text = '对方',font = ('微软雅黑',24))
    me = Button(goWin2,text = '我方',font = ('微软雅黑',24))
    me_boxing2 = Entry(goWin2)
    AI2Boxing = Entry(goWin2)
    rock = Button(goWin2,text = '石头',font = ('微软雅黑',20),command = Rock)
    scissor = Button(goWin2,text = '剪刀',font = ('微软雅黑',20),command = Scissor)
    paper = Button(goWin2,text = '布',font = ('微软雅黑',20),command = Paper)
    ok = Button(goWin2,text = '点击完成',font = ('微软雅黑',25),command = hard2OK)

    title2.grid(row=0,columnspan=3)
    AI.grid(row=3,column=3,rowspan=2)
    me.grid(row=3,column=0,rowspan=2)
    me_boxing2.grid(row=6,column=0)
    AI2Boxing.grid(row=6,column=3)
    rock.grid(row=7,column=0)
    scissor.grid(row=7,column=1)
    paper.grid(row=7,column=3)
    ok.grid(row=8,column=1)

    goWin2.mainloop()

def hard3Go():
    global hard

    hard = 3
    messagebox.showinfo(title = '猜拳信息',message = '你输了')
    hard = 1

beta_win = Tk()
beta_win.title('猜拳')
beta_win.iconbitmap(path.join(folder,'assets/icon.ico'))
title = Label(beta_win,text = '猜拳',font = ('微软雅黑',20))
hard1 = Button(beta_win,text = '基础难度',font = ('微软雅黑',18),command = hard1Go)
hard2 = Button(beta_win,text = '困难难度',font = ('微软雅黑',18),command = hard2Go)
hard3 = Button(beta_win,text = '噩梦难度',font = ('微软雅黑',18),command = hard3Go)

title.grid(row=0,columnspan=3)
hard1.grid(row=1,column=1)
# hard2.grid(row=1,column=2)
# hard3.grid(row=1,column=3)

beta_win.mainloop()