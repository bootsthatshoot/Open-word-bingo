import random
import tkinter.messagebox
import tkinter

root = tkinter.Tk()
frame = tkinter.Frame(root)

#window title goes here in the quotes!
root.wm_title("Miscbingo")

tkinter.Grid.rowconfigure(root, 0, weight=1)
tkinter.Grid.columnconfigure(root, 0, weight=1)
tkinter.Grid.rowconfigure(root, 1, weight=1)
tkinter.Grid.columnconfigure(root, 1, weight=1)
tkinter.Grid.rowconfigure(root, 2, weight=1)
tkinter.Grid.columnconfigure(root, 2, weight=1)
tkinter.Grid.rowconfigure(root, 3, weight=1)
tkinter.Grid.columnconfigure(root, 3, weight=1)
tkinter.Grid.rowconfigure(root, 4, weight=1)
tkinter.Grid.columnconfigure(root, 4, weight=1)
tkinter.Grid.rowconfigure(root, 5, weight=1)
grid = tkinter.Frame(frame)
frame.grid(row=0, column=0, sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
grid.grid(sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W, column=0, row=5, columnspan=4, rowspan=5)
tkinter.Grid.rowconfigure(frame, 5, weight=1)
tkinter.Grid.columnconfigure(frame, 0, weight=1)


def randomlist():
    random.shuffle(list1)
    line1.set(list1[0])
    line2.set(list1[1])
    line3.set(list1[2])
    line4.set(list1[3])
    line5.set(list1[4])
    line6.set(list1[5])
    line7.set(list1[6])
    line8.set(list1[7])
    line9.set(list1[8])
    line10.set(list1[9])
    line11.set(list1[10])
    line12.set(list1[11])
    line14.set(list1[12])
    line15.set(list1[13])
    line16.set(list1[14])
    line17.set(list1[15])
    line18.set(list1[16])
    line19.set(list1[17])
    line20.set(list1[18])
    line21.set(list1[19])
    line22.set(list1[20])
    line23.set(list1[21])
    line24.set(list1[22])
    line25.set(list1[23])


#RULES GO HERE, break lines with "\n"
# noinspection PyUnusedLocal
def popup():
    infomenu = tkinter.messagebox.showinfo(
                                           "-Bootsie"
                                           )

randomize = tkinter.Button(root, fg="#CFD8DC", text="Shuffle", bg="#263238", command=randomlist,
                           activebackground="#607D8B")
randomize.grid(row=5, column=1, columnspan=4, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
infomenubutton = tkinter.Button(root, fg="#CFD8DC", text="Info", bg="#263238", command=popup,
                                activebackground="#607D8B")
infomenubutton.grid(row=5, columnspan=1, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)

#INSERT ENTRIES HERE... need at least 25!
list1 = ['entries', 'submitted', 'like', 'this']

random.shuffle(list1)

line1 = tkinter.StringVar()
line1.set(list1[0])

line2 = tkinter.StringVar()
line2.set(list1[1])

line3 = tkinter.StringVar()
line3.set(list1[2])

line4 = tkinter.StringVar()
line4.set(list1[3])

line5 = tkinter.StringVar()
line5.set(list1[4])

line6 = tkinter.StringVar()
line6.set(list1[5])

line7 = tkinter.StringVar()
line7.set(list1[6])

line8 = tkinter.StringVar()
line8.set(list1[7])

line9 = tkinter.StringVar()
line9.set(list1[8])

line10 = tkinter.StringVar()
line10.set(list1[9])

line11 = tkinter.StringVar()
line11.set(list1[10])

line12 = tkinter.StringVar()
line12.set(list1[11])

line14 = tkinter.StringVar()
line14.set(list1[12])

line15 = tkinter.StringVar()
line15.set(list1[13])

line16 = tkinter.StringVar()
line16.set(list1[14])

line17 = tkinter.StringVar()
line17.set(list1[15])

line18 = tkinter.StringVar()
line18.set(list1[16])

line19 = tkinter.StringVar()
line19.set(list1[17])

line20 = tkinter.StringVar()
line20.set(list1[18])

line21 = tkinter.StringVar()
line21.set(list1[19])

line22 = tkinter.StringVar()
line22.set(list1[20])

line23 = tkinter.StringVar()
line23.set(list1[21])

line24 = tkinter.StringVar()
line24.set(list1[22])

line25 = tkinter.StringVar()
line25.set(list1[23])


# noinspection PyDefaultArgument
def color_change1(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile1.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile1.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change2(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile2.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile2.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change3(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile3.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile3.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change4(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile4.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile4.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change5(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile5.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile5.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change6(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile6.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile6.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change7(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile7.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile7.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change8(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile8.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile8.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change9(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile9.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile9.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change10(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile10.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile10.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change11(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile11.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile11.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change12(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile12.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile12.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change13(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile13.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile13.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change14(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile14.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile14.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change15(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile15.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile15.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change16(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile16.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile16.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change17(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile17.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile17.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change18(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile18.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile18.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change19(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile19.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile19.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change20(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile20.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile20.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change21(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile21.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile21.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change22(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile22.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile22.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change23(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile23.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile23.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change24(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile24.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile24.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


# noinspection PyDefaultArgument
def color_change25(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        tile25.config(bg="#B71C1C", activebackground="#E53935", activeforeground="#B0BEC5")
    else:
        tile25.config(bg="#263238", activebackground="#607D8B", activeforeground="#B0BEC5")


tile1 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line1, height=4, width=9,
                       command=color_change1, bg="#263238", activebackground="#607D8B")
tile2 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line2, height=4, width=9,
                       command=color_change2, bg="#263238", activebackground="#607D8B")
tile3 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line3, height=4, width=9,
                       command=color_change3, bg="#263238", activebackground="#607D8B")
tile4 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line4, height=4, width=9,
                       command=color_change4, bg="#263238", activebackground="#607D8B")
tile5 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line5, height=4, width=9,
                       command=color_change5, bg="#263238", activebackground="#607D8B")
tile6 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line6, height=4, width=9,
                       command=color_change6, bg="#263238", activebackground="#607D8B")
tile7 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line7, height=4, width=9,
                       command=color_change7, bg="#263238", activebackground="#607D8B")
tile8 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line8, height=4, width=9,
                       command=color_change8, bg="#263238", activebackground="#607D8B")
tile9 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line9, height=4, width=9,
                       command=color_change9, bg="#263238", activebackground="#607D8B")
tile10 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line10, height=4, width=9,
                        command=color_change10, bg="#263238", activebackground="#607D8B")
tile11 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line11, height=4, width=9,
                        command=color_change11, bg="#263238", activebackground="#607D8B")
tile12 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line12, height=4, width=9,
                        command=color_change12, bg="#263238", activebackground="#607D8B")
tile13 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, text="Free", height=4, width=9,
                        command=color_change13, bg="#263238", activebackground="#607D8B")
tile14 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line14, height=4, width=9,
                        command=color_change14, bg="#263238", activebackground="#607D8B")
tile15 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line15, height=4, width=9,
                        command=color_change15, bg="#263238", activebackground="#607D8B")
tile16 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line16, height=4, width=9,
                        command=color_change16, bg="#263238", activebackground="#607D8B")
tile17 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line17, height=4, width=9,
                        command=color_change17, bg="#263238", activebackground="#607D8B")
tile18 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line18, height=4, width=9,
                        command=color_change18, bg="#263238", activebackground="#607D8B")
tile19 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line19, height=4, width=9,
                        command=color_change19, bg="#263238", activebackground="#607D8B")
tile20 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line20, height=4, width=9,
                        command=color_change20, bg="#263238", activebackground="#607D8B")
tile22 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line22, height=4, width=9,
                        command=color_change22, bg="#263238", activebackground="#607D8B")
tile21 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line21, height=4, width=9,
                        command=color_change21, bg="#263238", activebackground="#607D8B")
tile23 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line23, height=4, width=9,
                        command=color_change23, bg="#263238", activebackground="#607D8B")
tile24 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line24, height=4, width=9,
                        command=color_change24, bg="#263238", activebackground="#607D8B")
tile25 = tkinter.Button(root, fg="#CFD8DC", wraplength=70, textvariable=line25, height=4, width=9,
                        command=color_change25, bg="#263238", activebackground="#607D8B")

tile1.grid(row=0, column=0, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile2.grid(row=0, column=1, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile3.grid(row=0, column=2, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile4.grid(row=0, column=3, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile5.grid(row=0, column=4, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile6.grid(row=1, column=0, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile7.grid(row=1, column=1, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile8.grid(row=1, column=2, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile9.grid(row=1, column=3, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile10.grid(row=1, column=4, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile11.grid(row=2, column=0, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile12.grid(row=2, column=1, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile13.grid(row=2, column=2, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile14.grid(row=2, column=3, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile15.grid(row=2, column=4, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile16.grid(row=3, column=0, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile17.grid(row=3, column=1, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile18.grid(row=3, column=2, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile19.grid(row=3, column=3, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile20.grid(row=3, column=4, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile21.grid(row=4, column=0, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile22.grid(row=4, column=1, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile23.grid(row=4, column=2, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile24.grid(row=4, column=3, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
tile25.grid(row=4, column=4, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)

tkinter.mainloop()
