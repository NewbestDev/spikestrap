from tkinter import *
import os
global mc
mc = False
openm = False
theme = "#141414"
oofsound = True
discordpres = False
touchmode = True
opengl = True
themechange = False
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
    
def dropdown():
    global mc
    mc = not mc
    if mc == True:
        menu.config(text="↓")
        settingmenu.grid(row=1,column=0)
        dismenu.place(x=0,y=101)
    else:
        menu.config(text="≡")
        settingmenu.grid_forget()
        dismenu.place(x=100000,y=100000)

def oldoof():
    global oofsound
    oofsound = not oofsound
    oldoofsound.config(text="Old oof sound: " + str(oofsound))
def touchscrn():
    global touchmode
    touchmode = not touchmode
    touchscreenmode.config(text="Touchscreen mode: " + str(touchmode))
def dcstat():
    global discordpres
    discordpres = not discordpres
    discordstatus.config(text="Show roblox on discord status: " + str(discordpres))
def ogl():
    global opengl
    opengl = not opengl
    useopengl.config(text="Use openGL: " + str(opengl))
def discord():
    os.system("xdg-open https://discord.gg/5JQ4g34YHX")
def settings():
    print('settings')
    global themechange
    global theme
    themechange = not themechange
    items = [root,oldoofsound, touchscreenmode, useopengl, discordstatus, textlabel2, textlabel, configbtn, menu, dismenu, settingmenu, ]
    if themechange == True:
        theme = "white"
        settingmenu.config(text="☼")
    else:
        theme = "#141414"
        settingmenu.config(text="☽")
    for t in items:
        t.config(bg=theme)
    
def configeditor():
    global openm
    global opengl
    global discordpres
    global touchmode
    global oofsound
    openm = not openm
    if openm == True:
        oldoofsound.place(x=100,y=210)
        touchscreenmode.place(x=80,y=260)
        useopengl.place(x=120,y=310)
        discordstatus.place(x=8,y=360)
    else:
        buttons = [oldoofsound, touchscreenmode, useopengl, discordstatus]
        opengl1 = str(opengl).lower()
        discordpres1 = str(discordpres).lower()
        touchmode1 = str(touchmode).lower()
        oof1 = str(oofsound).lower()
        home_dir = os.path.expanduser("~")
        replace_line(home_dir + "/.var/app/org.vinegarhq.Sober/config/sober/config.json", 1, "    \"bring_back_oof:\"" + " " + oof1 + ",\n")
        replace_line(home_dir + "/.var/app/org.vinegarhq.Sober/config/sober/config.json", 2, "    \"discord_rpc_enabled:\"" + " " + discordpres1 + ",\n")
        if touchmode1 == "true":
            replace_line(home_dir + "/.var/app/org.vinegarhq.Sober/config/sober/config.json", 6, "    \"touch_mode:\"" + " on" + ",\n")
        else:
            replace_line(home_dir + "/.var/app/org.vinegarhq.Sober/config/sober/config.json", 6, "    \"touch_mode:\"" + " off" + ",\n")
        replace_line(home_dir + "/.var/app/org.vinegarhq.Sober/config/sober/config.json", 7, "    \"use_opengl:\"" + " " + opengl1 + "\n")
        for t in buttons:
            t.place(x=100000, y=100000)
root = Tk()
discordico = PhotoImage(file = r'discord.png')


root.title("Spikestrap")
root.geometry("500x500")
root.configure(background = theme)
oldoofsound = Button(root,text="Old oof sound: " + str(oofsound), font=('Arials', 20), bg=theme, command=oldoof)
touchscreenmode = Button(root,text="Touchscreen mode: " + str(touchmode), font=('Arials', 20), bg=theme, command=touchscrn)
useopengl = Button(root,text="Use openGL: " + str(opengl), font=('Arials', 20), bg=theme, command=ogl)
discordstatus = Button(root,text="Show roblox on discord status: " + str(discordpres), font=('Arials', 20), bg=theme, command=dcstat)
textlabel2 = Label(root, text="Spikestrap", font=('Arials', 37), bg=theme)
textlabel = Label(root, text="Bloxstrap, for linux", font=('Arials', 15), fg='#808080', bg=theme)
configbtn = Button(root,text="Config editor", font=('Arials', 20), command=configeditor, bg=theme)
menu = Button(root, text="≡", font=('Arials', 20), command=dropdown, bg=theme)
dismenu = Button(root, image=discordico, command=discord, height=46,width=46, bg=theme)
settingmenu = Button(root, text="☽", font=('Arials', 20), command=settings, bg=theme)
textlabel2.place(x=125,y=0)
textlabel.place(x=160,y=80)
configbtn.place(x=160,y=160)
menu.grid(row=0,column=0)
root.mainloop()
