import logging
import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.geometry("516x700+340+10")
root.title("Лехин аудиоплеер")
root.config(bg='#0f0f0f')
root.resizable(False, False)
mixer.init()


def add_song():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        logging.info(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)


def play_song():
    music_name = playlist.get(ACTIVE)
    logging.info(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()


lower_frm = Frame(root, bg="#000000", width=700, height=700)
lower_frm.place(x=0, y=0)

# frmcount = 32
# frms = [
#     PhotoImage(
#         file=os.path.join(os.path.dirname(__file__), 'my_gif_fooo.gif'),
#         format='gif -index %i' % i)
#     for i in range(frmcount)
# ]


# def update(ind):
#     frame = frms[ind]
#     ind += 1
#     if ind == frmcount:
#         ind = 0
#     lbl.config(image=frame)
#     root.after(40, update, ind)


audioplayer = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'static/audioplayer.png'))
lbl = Label(root, image=audioplayer, width=300, height=300)
lbl.place(x=0, y=0)
# root.after(0, update, 0)

menu = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'static/menu.png'))
lb_menu = Label(root, image=menu, width=516, height=120)
lb_menu.place(x=0, y=580)

frm_music = Frame(root, bd=2, relief=RIDGE, width=516, height=120)
frm_music.place(x=0, y=580)

btn_play = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'static/play.png'))
btn_p = Button(root, image=btn_play, bg='#0f0f0f', height=50, width=50, command=play_song)
btn_p.place(x=225, y=516)

btn_stop = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'static/stop.png'))
btn_s = Button(root, image=btn_stop, bg='#0f0f0f', height=50, width=50, command=mixer.music.stop)
btn_s.place(x=140, y=516)

btn_pause = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'static/pause.png'))
btn_ps = Button(root, image=btn_pause, bg='#0f0f0f', height=50, width=50, command=mixer.music.pause)
btn_ps.place(x=310, y=516)

btn_browse = Button(root, text="Выбрать папку с музыкой", font=('Arial,bold', 15), fg="Black", bg="#FFFFFF", width=48,
                    command=add_song)
btn_browse.place(x=0, y=572)

scroll = Scrollbar(frm_music)
playlist = Listbox(frm_music, width=100, font=('Arial,bold', 15), bg='#0f0f0f', fg='#00ff00',
                   selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=RIGHT, fill=BOTH)

root.mainloop()
