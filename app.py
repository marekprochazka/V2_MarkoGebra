from tkinter import *
import tkinter.ttk as t
from tkinter.ttk import Button
import tkinter.colorchooser as col
from colormap import rgb2hex
from math import floor
from tkinter import filedialog
from PIL import Image
import json
from numpy import sin, cos, tan, pi
import matplotlib as mp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as anim
from matplotlib import style as st
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import webbrowser
# Ver. Alpha 1.6
#


from Static.constants import *
from Globals.calculated import *
from Globals.variables import Variables as V
from GUI.base import Base
from Utils import DeleteAll, Saving, ShowFrame, UpdateTable
from Graphing.graph_animation import GraphAnimation

mp.use("TkAgg")
with open("graphstyle.txt", "r") as style:
    st.use(style)

# st.use('ggplot')

import numpy as np

# f = plt.figure(figsize=(4.5, 4.5), dpi=100)
from Graphing.setup import *



class MarkoGebra(Base,DeleteAll,Saving,ShowFrame,UpdateTable):
    def __init__(self):

        self.to_inherit = (DeleteAll,Saving,ShowFrame,UpdateTable)
        self.doInherit()
        Base.__init__(self)


    def doInherit(self):
        for cls in self.to_inherit:
            cls.__init__(self,main=self)

    def on_exit(self):
        self.show_Setup_Frame()
        self.destroy()

    def openHelp(self):
        webbrowser.open(url="https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270", new=1)
        webbrowser.open(url="D:\Věci\Programování\Dlohodoba_prace_main_2020\web\index.html", new=1)



    def colorize_grid(self):
        color = col.askcolor()
        a.grid(color=color[1])

    def size_grid(self, size):
        a.grid(linewidth=size)

    def line_grid(self, line):
        a.grid(linestyle=line)

    def add_point_scatter(self, x, y, marker=".", color="blue", size="1", error=None, entry1=None, entry2=None):
        try:
            x = int(x)
            y = int(y)
            if x > V.lim1:
                V.lim1 = x
            if x < V.lim2:
                V.lim2 = x
            if y > V.lim1:
                V.lim1 = y
            if y < V.lim2:
                V.lim2 = y
            if [x, y] not in V.coordinates_scatter:
                V.coordinates_scatter.append([x, y, marker, color, size])
                V.coordinates_all_list.append([[x, y], marker, color, size])
                if error != None:
                    error["text"] = ""
                    entry1.delete(0, END)
                    entry2.delete(0, END)
                    self.update_table()
        except:
            if error != None:
                error["text"] = "chyba"
                entry1.delete(0, END)
                entry2.delete(0, END)

    def add_plot_from_function(self, function: str, line="solid", color="blue", size="1", error=None, entry=None):
        is_all_fine = True
        for char in function:
            if char not in FUNCTION_ALLOWED_MARKS:
                is_all_fine = False

        if is_all_fine:
            function = function.replace("s", "sin")
            function = function.replace("c", "cos")
            function = function.replace("t", "tan")
            function = function.replace("p", "pi")
            x = np.arange(V.lim2, V.lim1, 0.5)
            y = function

            checnk = True
            if len(V.coordinates_plot) >= 1:
                for val in V.coordinates_plot:
                    if val[1] == y:
                        checnk = False
            if checnk:
                V.coordinates_plot.append([x, y, line, color, size, function])
                V.coordinates_all_list.append([["f(x)", function], line, color, size])
            if error != None:
                error["text"] = ""
                entry.delete(0, END)
            self.update_table()
        else:
            if error != None:
                entry.delete(0, END)

                error["text"] = "chyba"

    def add_pie_data(self, data, expl=0, entry1=None, entry2=None, cbb=None, error=None):

        try:
            float(data[0])
            V.slices.append(data[0])
            V.activities.append(data[1])
            V.cols.append(data[2])
            V.explode.append(expl)
            if entry1 != None:
                entry1.delete(0, END)
                entry2.delete(0, END)
                cbb.set("")
            V.coordinates_all_list.append([data[1], data[0], data[2]])
            error["text"] = ""

            self.update_table()
        except:
            if entry1 != None:
                entry1.delete(0, END)
                entry2.delete(0, END)
                error["text"] = "Chyba"
                cbb.set("")
            else:
                pass

    def add_bar_data(self, name, value, color, entry1, entry2, cbb, error):
        try:

            float(value)
            V.bars.append([name, value, color, 0.8])

            V.coordinates_all_list.append([name, value, color])
            entry1.delete(0, END)
            entry2.delete(0, END)
            cbb.set("")
            error["text"] = ""

            self.update_table()
        except:
            entry1.delete(0, END)
            entry2.delete(0, END)
            error["text"] = "Chyba"
            cbb.set("")

    def create_basic_gen(self, number, dispersion, col):
        V.basic_gen = [np.random.rand(number), np.random.rand(number)]
        self.update_dispersion(dispersion, col)

    def update_dispersion(self, dispersion, col):
        V.noises[0] = [[floor(V.basic_gen[0][indx] * dispersion), floor(V.basic_gen[1][indx] * dispersion), ".", col, 1] for
                     indx, gn in enumerate(V.basic_gen[0])]

    def lock_noise(self, disper, num):
        V.noises.append(V.noises[0])
        V.dispersion.append(disper)
        V.number.append(num)
        V.coordinates_all_list.append([num, disper, V.noises[-1][0][2], V.noises[-1][0][3], V.noises[-1][0][4]])
        self.update_table()





    def console_controller(self):
        top = Toplevel()
        top.config(background="black")
        top.wm_geometry("800x500")
        top.maxsize(width=800, height=400)
        top.minsize(width=800, height=400)
        top.title("Konzole")
        types = t.Entry(top)
        types.place(bordermode=OUTSIDE, width=700, height=20, x=0, y=380)
        types.focus()
        send_command = t.Button(top, text="odeslat", command=lambda: self.command_entered(types, scrollable_Frame))
        send_command.place(bordermode=OUTSIDE, width=100, height=20, x=700, y=380)

        table_container = t.Frame(top)
        canvas = Canvas(table_container)
        canvas.configure(bg="black")
        scrollbar = t.Scrollbar(table_container, orient="vertical", command=canvas.yview)
        scrollable_Frame = Frame(canvas)
        scrollable_Frame.configure(bg="black")
        scrollable_Frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=self.canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_Frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        table_container.place(bordermode=OUTSIDE, x=0, y=0, width=800,
                              height=380)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        top.bind("<Return>", lambda event: self.command_entered(types, scrollable_Frame, top))
        top.bind("<Up>", lambda event: self.history_move_up(types))
        top.bind("<Down>", lambda event: self.history_move_down(types))

    def history_move_up(self, entry):


        if V.command_history != []:
            if V.history_moves < len(V.command_history):
                V.history_moves += 1
                entry.delete(0, END)
                entry.insert(0, V.command_history[-V.history_moves])

    def history_move_down(self, entry):
        V.history_moves -= 1
        if V.history_moves > 0:
            entry.delete(0, END)
            entry.insert(0, V.command_history[-V.history_moves])
        else:
            V.history_moves = 1

    def command_entered(self, entry, frame, top):
        V.history_moves = 0
        command = entry.get().split(" ")
        if V.command_history != []:
            if command != V.command_history[-1]:
                if command in V.command_history:
                    V.command_history.remove(command)
                V.command_history.append(command)
        else:
            V.command_history.append(command)
        if command[0] == "del":
            try:
                if int(command[1]) <= len(V.coordinates_all_list):
                    self.delete_value(int(command[1]))
                    Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(fill=BOTH)
                    Label(frame, text=f"Souřadnice indexu {command[1]} odstraněna!", bg="black", fg="green",
                          font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)
                    entry.delete(0, END)
                else:
                    Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(
                        fill=BOTH)
                    entry.delete(0, END)
            except IndexError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except ValueError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)


        elif command[0] == "col":
            try:
                if int(command[1]) <= len(V.coordinates_all_list):
                    self.changeColor(int(command[1]), top)
                    Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(fill=BOTH)
                    Label(frame, text=f"Barva indexu {command[1]} změněna!", bg="black", fg="green",
                          font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)

                    entry.delete(0, END)
                    entry.focus()
                else:
                    Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(
                        fill=BOTH)
                    entry.delete(0, END)

            except IndexError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except ValueError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)


        elif command[0] == "size":
            try:
                if int(command[1]) <= len(V.coordinates_all_list):
                    self.changeSize(int(command[1]), command[2])
                    Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(fill=BOTH)
                    Label(frame, text=f"Tloušťka indexu {command[1]} změněna!", bg="black", fg="green",
                          font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)

                    entry.delete(0, END)
                else:
                    Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(
                        fill=BOTH)
                    entry.delete(0, END)

            except IndexError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except ValueError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except ArithmeticError:
                Label(frame, text="Neplatná velikost!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except BlockingIOError:
                Label(frame, text="Příkaz nelze použít pro aktuální způsob grafování!", bg="black", fg="red",
                      font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)


        elif command[0] == "mktype":
            try:
                if int(command[1]) <= len(V.coordinates_all_list):
                    self.changeLine(int(command[1]), command[2])
                    Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(fill=BOTH)
                    Label(frame, text=f"Značkování indexu {command[1]} upraveno!", bg="black", fg="green",
                          font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)
                    entry.delete(0, END)
                else:
                    Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(
                        fill=BOTH)
                    entry.delete(0, END)
            except IndexError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except ValueError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except SyntaxError:
                Label(frame, text="Neplatná značka!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                Label(frame, text="Použij 'markers' pro zobrazení dostupných značek", bg="black", fg="red",
                      font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except BlockingIOError:
                Label(frame, text="Příkaz nelze použít pro aktuální způsob grafování!", bg="black", fg="red",
                      font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)

        elif command[0] == "GPstyle":
            try:
                self.changeGraphStyle(command[1])
                Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                      anchor="w").pack(fill=BOTH)
                Label(frame, text=f"Styl grafu úspěšně změněn na {command[1]}!", bg="black", fg="green",
                      font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)
                Label(frame, text=f"Změny na grafu se projeví po restartu aplikace", bg="black", fg="aqua",
                      font=fonts()["ITALIC_SMALL"], anchor="w").pack(fill=BOTH)
                entry.delete(0, END)
            except SyntaxError:
                Label(frame, text="Neplatný styl!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                Label(frame, text="Použij 'ShowMeStyles' pro zobrazení dostupných stylů", bg="black", fg="aqua",
                      font=fonts()["ITALIC_SMALL"],
                      anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)

        # pie specials
        elif command[0] == "explode":
            try:
                if int(command[1]) <= len(V.coordinates_all_list):
                    self.explode(int(command[1]), float(command[2]))
                    Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(fill=BOTH)
                    Label(frame, text=f"Vysunutí indexu {command[1]} upraveno!", bg="black", fg="green",
                          font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)
                    entry.delete(0, END)
                else:
                    Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(
                        fill=BOTH)
                    entry.delete(0, END)
            except IndexError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except ValueError:
                Label(frame, text="Neplatná hodnota!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except SyntaxError:
                Label(frame, text="Akce lze porovést pouze u PIE grafu!", bg="black", fg="red",
                      font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)


        elif command[0] == "stAngle":
            try:
                self.stAngle(int(command[1]))
                Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                      anchor="w").pack(fill=BOTH)
                Label(frame, text=f" Počáteční úhel změněn!", bg="black", fg="green",
                      font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)
                entry.delete(0, END)
            except ValueError:
                Label(frame, text="Neplatná hodnota!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except SyntaxError:
                Label(frame, text="Akce lze porovést pouze u PIE grafu!", bg="black", fg="red",
                      font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)


        elif command == ["ShowMeStyles"]:
            Label(frame, text=f"{', '.join(AVALIBLE_STYLES[0:10])},", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"{', '.join(AVALIBLE_STYLES[10:16])},", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"{', '.join(AVALIBLE_STYLES[16:23])},", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"{', '.join(AVALIBLE_STYLES[23:27])}", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            entry.delete(0, END)

        elif command == ["markers"]:
            Label(frame, text="Dostupné značky: ", bg="black", fg="green", font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"Body: {'; '.join(POINT_MARKERS)}", bg="black", fg="green", font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)

            Label(frame, text=f"Funkce: {'; '.join(LINE_MARKERS)} ", bg="black", fg="green", font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            entry.delete(0, END)



        elif command == ["clear"]:
            for child in frame.winfo_children():
                child.destroy()
            entry.delete(0, END)


        elif (command == ["?"]) or (command == ["help"]):
            Label(frame, text="Dostupné příkazy", bg="black", fg="green", font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="del [index] - pro odstranění konkrétního vstupu", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="mktype [index] [marker] - pro změnu značkování vstupu", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="markers - pro vypsání značek", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="clear - pro vyčištění konzole", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="col [index] - pro změnu barvy indexu", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="size [index] [size] - pro vyčištění konzole", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="GPstyle [style] - pro změnu stylu grafu (projeví se po restartu)", bg="black",
                  fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="ShowMeStyles - pro zobrazení dostupných stylů grafu", bg="black",
                  fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="explode [index] [value] - pro 'vystoupení' hodnoty z grafu (pouze pro PIE) ", bg="black",
                  fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="stAngle - pro změnu začánajícího úhlu grafu (poze pro PIE) ", bg="black",
                  fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)

            entry.delete(0, END)

        else:
            Label(frame, text="Neplatný příkaz!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="Zadej 'help' nebo '?' pro vypsání možností", bg="black", fg="red",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            entry.delete(0, END)

    # DONE
    def delete_value(self, index):
        if V.to_animate == 1:
            if V.coordinates_all_list[index][0][0] == "f(x)":
                for indx, val in enumerate(V.coordinates_plot):
                    if val[1] == V.coordinates_all_list[index][0][1]:
                        del V.coordinates_plot[indx]
                        del V.coordinates_all_list[index]
                        self.update_table()




            else:
                for coord in V.coordinates_scatter:
                    if coord[0:2] == V.coordinates_all_list[index][0]:
                        V.coordinates_scatter.remove(coord)

                del V.coordinates_all_list[index]
                self.update_table()

        if V.to_animate == 2:
            del V.coordinates_all_list[index]
            del V.slices[index]
            del V.cols[index]
            del V.activities[index]
            del V.explode[index]
            self.update_table()

        if V.to_animate == 3:
            del V.bars[index]
            del V.coordinates_all_list[index]
            self.update_table()

        if V.to_animate == 4:
            del V.noises[index + 1]
            del V.dispersion[index]
            del V.number[index]
            del V.coordinates_all_list[index]
            self.update_table()

    # DONE
    def changeLine(self, index, linetype: str):
        if V.to_animate == 1:
            if V.coordinates_all_list[index][0][0] == "f(x)":
                if linetype in LINE_MARKERS:
                    for indx, val in enumerate(V.coordinates_plot):
                        if val[1] == V.coordinates_all_list[index][0][1]:
                            V.coordinates_plot[indx][2] = linetype
                            V.coordinates_all_list[index][1] = linetype
                            self.update_table()
                else:
                    raise SyntaxError

            else:
                if (linetype in POINT_MARKERS) or ((linetype[0] and linetype[-1]) == "$"):

                    for indx, val in enumerate(V.coordinates_scatter):
                        if val[0:2] == V.coordinates_all_list[index][0]:
                            V.coordinates_scatter[indx][2] = linetype
                            V.coordinates_all_list[index][1] = linetype

                    self.update_table()
                else:
                    raise SyntaxError

        elif V.to_animate == 4:
            if (linetype in POINT_MARKERS) or ((linetype[0] and linetype[-1]) == "$"):
                for coord in V.noises[index + 1]:
                    coord[2] = linetype
                V.coordinates_all_list[index][2] = linetype
                self.update_table()

            else:
                raise SyntaxError
        else:
            raise BlockingIOError

    # DONE
    def changeColor(self, index, top):
        if V.to_animate == 1:
            if V.coordinates_all_list[index][0][0] == "f(x)":
                for indx, val in enumerate(V.coordinates_plot):
                    if val[1] == V.coordinates_all_list[index][0][1]:
                        color = col.askcolor()

                        V.coordinates_plot[indx][3] = color[1]
                        V.coordinates_all_list[index][2] = color[1]
                        self.update_table()
                        top.lift()

            else:

                for indx, val in enumerate(V.coordinates_scatter):
                    if val[0:2] == V.coordinates_all_list[index][0]:
                        color = col.askcolor()
                        V.coordinates_scatter[indx][3] = color[1]
                        V.coordinates_all_list[index][2] = color[1]
                        self.update_table()
                        top.lift()


        elif V.to_animate == 2:
            color = col.askcolor()
            V.cols[index] = color[1]
            V.coordinates_all_list[index][2] = color[1]
            self.update_table()
            top.lift()
        elif V.to_animate == 3:
            color = col.askcolor()
            V.bars[index][2] = color[1]
            V.coordinates_all_list[index][2] = color[1]
            self.update_table()
            top.lift()
        elif V.to_animate == 4:
            color = col.askcolor()
            for coord in V.noises[index + 1]:
                coord[3] = color[1]
            V.coordinates_all_list[index][3] = color[1]
            self.update_table()
            top.lift()

    # DONE
    def changeSize(self, index, size):
        try:
            float(size)
            if V.to_animate == 1:
                if V.coordinates_all_list[index][0][0] == "f(x)":
                    for indx, val in enumerate(V.coordinates_plot):
                        if val[1] == V.coordinates_all_list[index][0][1]:
                            V.coordinates_plot[indx][4] = size
                            V.coordinates_all_list[index][3] = size
                            self.update_table()

                else:

                    for indx, val in enumerate(V.coordinates_scatter):
                        if val[0:2] == V.coordinates_all_list[index][0]:
                            V.coordinates_scatter[indx][4] = float(size)
                            V.coordinates_all_list[index][3] = size

                    self.update_table()

            elif V.to_animate == 3:
                # TODO během po úpravě coord_all přidat úpravu
                V.bars[index][3] = size

            elif V.to_animate == 4:
                for coord in V.noises[index + 1]:
                    coord[4] = size
                V.coordinates_all_list[index][4] = size
                self.update_table()


            else:
                raise BlockingIOError
        except:
            raise ArithmeticError

    def changeGraphStyle(self, style):
        if style in AVALIBLE_STYLES:
            with open("graphstyle.txt", "w") as stl:
                stl.truncate()
            with open("graphstyle.txt", "w") as stl:
                stl.write(style)
        else:
            raise SyntaxError

    def explode(self, index, value):
        if V.to_animate == 2:
            V.explode[index] = value
            self.update_table()
        else:
            raise SyntaxError

    def stAngle(self, angle):
        if V.to_animate == 2:
            V.start_angle = angle
            self.update_table()
        else:
            raise SyntaxError


aniObj = GraphAnimation()
aniFun = aniObj.Go

app = MarkoGebra()

ani = anim.FuncAnimation(f, aniFun, interval=1000, blit=False)
app.protocol("WM_DELETE_WINDOW", app.on_exit)
app.mainloop()
