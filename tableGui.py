"""
2/8/2023
Flight Attendant and Pilot GUI
APCSP
Sprint 1 Group 5
"""
import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import Button
import os
import mysql.connector
from sqlCommandClass import SqlCommandClass


class TableGui():

  def aboutOpen(self):
    #WINDOW THAT IS OPENED WHEN ABOUT TAB PRESSED

    self.aboutWindow = tk.Tk()
    self.aboutWindow.title("About")
    self.aboutWindow.geometry("150x100")

    self.aboutDesc = Label(
      self.aboutWindow,
      text=
      "GUI/CRUD of Flight Attendants and Pilots for CS50 Period 6 by Group 5",
      wraplength=100)
    self.aboutDesc.pack()

  def pilotWindowOpen(self):

    #Pilot Gui written by Nicholas

    #Window and canvas geometry
    self.pilotTableRoot = tk.Tk()
    self.pilotTableRoot.title("Pilot/Flight Attendants Tables")
    self.pilotTableRoot.geometry("450x300")
    self.pilotTableCanvas = tk.Canvas(self.pilotTableRoot,
                                      width=450,
                                      height=300)
    self.pilotTableCanvas.pack()

    #DROPDOWN MENU VARIABLES
    self.pilotVP = tk.StringVar(self.pilotTableRoot)
    self.pilotVP.set("placeholder")
    self.varPQ1 = tk.StringVar(self.pilotTableRoot)
    self.varPQ1.set("No")
    self.varPQ2 = tk.StringVar(self.pilotTableRoot)
    self.varPQ2.set("No")
    self.varPQ3 = tk.StringVar(self.pilotTableRoot)
    self.varPQ3.set("No")

    #SQL TABLE NAME LABELS
    self.fnLabel = tk.Label(self.pilotTableCanvas, text="First Name")
    self.lnLabel = tk.Label(self.pilotTableCanvas, text="Last Name")
    self.posLabel = tk.Label(self.pilotTableCanvas, text="Position")
    self.pq1 = tk.Label(self.pilotTableCanvas, text="Plane Qualification 1")
    self.pq2 = tk.Label(self.pilotTableCanvas, text="Plane Qualification 2")
    self.pq3 = tk.Label(self.pilotTableCanvas, text="Plane Qualification 3")
    self.idLabel = tk.Label(self.pilotTableCanvas, text="Entry Id:")

    self.fnLabel.place(x=20, y=50)
    self.lnLabel.place(x=20, y=80)
    self.posLabel.place(x=20, y=110)
    self.pq1.place(x=20, y=140)
    self.pq2.place(x=20, y=170)
    self.pq3.place(x=20, y=200)
    self.idLabel.place(x=20, y=20)

    #USER ENTRY WIDGETS
    self.pilotFirstName = tk.Entry(self.pilotTableCanvas)
    self.pilotLastName = tk.Entry(self.pilotTableCanvas)
    self.pilotVarPos = tk.OptionMenu(self.pilotTableCanvas, self.pilotVP,
                                     "placeholder", "placeholder1")
    self.planeQualification1 = tk.OptionMenu(self.pilotTableCanvas,
                                             self.varPQ1, "Yes", "No")
    self.planeQualification2 = tk.OptionMenu(self.pilotTableCanvas,
                                             self.varPQ2, "Yes", "No")
    self.planeQualification3 = tk.OptionMenu(self.pilotTableCanvas,
                                             self.varPQ3, "Yes", "No")
    self.pilotId = tk.Text(self.pilotTableCanvas, height=1, width=5)
    self.pilotId.configure(state="disabled")

    self.pilotId.place(x=90, y=20)
    self.pilotFirstName.place(x=90, y=50)
    self.pilotLastName.place(x=90, y=80)
    self.pilotVarPos.place(x=150, y=105)
    self.planeQualification1.place(x=150, y=135)
    self.planeQualification2.place(x=150, y=165)
    self.planeQualification3.place(x=150, y=195)

    #BUTTONS TO NAVIGATE THROUGH THE DATABASE (READ)
    self.pilotsVeryLastButton = Button(self.pilotTableCanvas,
                                       text="<--",
                                       command=lambda: self.data.placeholder)
    self.pilotsLastLastButton = Button(self.pilotTableCanvas,
                                       text="<<",
                                       command=lambda: self.data.placeholder)
    self.pilotsLastButton = Button(self.pilotTableCanvas,
                                   text="<",
                                   command=lambda: self.data.placeholder)
    self.pilotsNextButton = Button(self.pilotTableCanvas,
                                   text=">",
                                   command=lambda: self.data.placeholder)
    self.pilotsNextNextButton = Button(self.pilotTableCanvas,
                                       text=">>",
                                       command=lambda: self.data.placeholder)
    self.pilotsVeryNextButton = Button(self.pilotTableCanvas,
                                       text="-->",
                                       command=lambda: self.data.placeholder)

    self.pilotsVeryLastButton.place(x=30, y=235)
    self.pilotsLastLastButton.place(x=80, y=235)
    self.pilotsLastButton.place(x=120, y=235)
    self.pilotsNextButton.place(x=150, y=235)
    self.pilotsNextNextButton.place(x=180, y=235)
    self.pilotsVeryNextButton.place(x=230, y=235)

    #INSERTION BUTTON
    self.pilotCreateButton = Button(
      self.pilotTableCanvas,
      text="INSERT",
      command=lambda: SqlCommandClass.createPilot(self))
    #UPDATE BUTTON
    self.pilotUpdateButton = Button(
      self.pilotTableCanvas,
      text="Update",
      command=lambda: SqlCommandClass.updatePilotTable(self))

    #DELETE BUTTON
    self.pilotDeleteButton = Button(
      self.pilotTableCanvas,
      text="Delete",
      command=lambda: SqlCommandClass.deletePilotTable(self))

    self.pilotUpdateButton.place(x=300, y=75)
    self.pilotDeleteButton.place(x=300, y=125)
    self.pilotCreateButton.place(x=300, y=35)

    self.pilotTableRoot.mainloop()

  def flightAttendantWindowOpen(self):

    #Flight attendant Gui written by Nicholas up to "***"

    #Window and canvas geometry
    self.flightAttendantRoot = tk.Tk()
    self.flightAttendantRoot.title("Flight Attendants Tables")
    self.flightAttendantRoot.geometry("450x300")
    self.flightAttendantCanvas = tk.Canvas(self.flightAttendantRoot,
                                           width=450,
                                           height=300)
    self.flightAttendantCanvas.pack()

    #DROPDOWN MENU VARIABLES
    self.faVarPos = tk.StringVar(self.flightAttendantRoot)
    self.faVarPos.set("placeholder1")

    self.fnLabel = tk.Label(self.flightAttendantCanvas, text="First Name")
    self.lnLabel = tk.Label(self.flightAttendantCanvas, text="Last Name")
    self.posLabel = tk.Label(self.flightAttendantCanvas, text="Position")
    self.idLabel = tk.Label(self.flightAttendantCanvas, text="Entry Id:")

    self.fnLabel.place(x=20, y=50)
    self.lnLabel.place(x=20, y=80)
    self.posLabel.place(x=20, y=110)
    self.idLabel.place(x=20, y=20)

    #USER ENTRY WIDGETS
    self.faFirstName = tk.Entry(self.flightAttendantCanvas)
    self.faLastName = tk.Entry(self.flightAttendantCanvas)
    self.pos = tk.OptionMenu(self.flightAttendantCanvas, self.faVarPos,
                             "placeholder1", "placeholder2", "placeholder3",
                             "placeholder4")
    self.faId = tk.Text(self.flightAttendantCanvas, height=1, width=5)
    self.faId.configure(state="disabled")

    self.faFirstName.place(x=90, y=50)
    self.faLastName.place(x=90, y=80)
    self.pos.place(x=90, y=110)
    self.faId.place(x=90, y=20)

    #BUTTONS TO NAVIGATE THROUGH THE DATABASE (READ)
    self.faVeryLastButton = tk.Button(self.flightAttendantCanvas,
                                      text="<--",
                                      command=lambda: self.data.placeholder)
    self.faLastLastButton = tk.Button(self.flightAttendantCanvas,
                                      text="<<",
                                      command=lambda: self.data.placeholder)
    self.faLastButton = tk.Button(self.flightAttendantCanvas,
                                  text="<",
                                  command=lambda: self.data.placeholder)
    self.faNextButton = tk.Button(self.flightAttendantCanvas,
                                  text=">",
                                  command=lambda: self.data.placeholder)
    self.faNextNextButton = tk.Button(self.flightAttendantCanvas,
                                      text=">>",
                                      command=lambda: self.data.placeholder)
    self.faVeryNextButton = tk.Button(self.flightAttendantCanvas,
                                      text="-->",
                                      command=lambda: self.data.placeholder)

    self.faVeryLastButton.place(x=30, y=150)
    self.faLastLastButton.place(x=80, y=150)
    self.faLastButton.place(x=120, y=150)
    self.faNextButton.place(x=150, y=150)
    self.faNextNextButton.place(x=180, y=150)
    self.faVeryNextButton.place(x=230, y=150)

    #***#

    #Flight attendants Gui (Andy and Kinsley)
    # Connection

    #CREATE
    self.flightAttendantsCreateBtn = Button(
      self.flightAttendantCanvas,
      text="Insert",
      command=lambda: self.SqlCommandClass.createFa())
    #READ
    #UPDATE
    #Andy
    self.flightAttendantsUpdateButton = Button(
      self.flightAttendantCanvas,
      text='Update',
      command=lambda: self.SqlCommandClass.updateFa())

    #Andy
    #DELETE
    self.flightAttendantsDeleteButton = Button(
      self.flightAttendantCanvas,
      text='Delete',
      command=lambda: self.SqlCommandClass.deleteFA())

    self.flightAttendantsUpdateButton.place(x=300, y=75)
    self.flightAttendantsDeleteButton.place(x=300, y=125)
    self.flightAttendantsCreateBtn.place(x=300, y=35)

#Method that allows user to return to the main menu

  def __init__(self):

    #table gui opener by nicholas

    self.root = tk.Tk()

    #menubar for miscelaneous commands
    self.menubar = tk.Menu(self.root)
    self.root.config(menu=self.menubar)
    self.filemenu = tk.Menu(self.menubar, tearoff=0)
    self.filemenu.add_command(label="Exit", command=self.root.quit)
    self.menubar.add_cascade(label="File", menu=self.filemenu)

    self.helpmenu = tk.Menu(self.menubar, tearoff=0)
    self.helpmenu.add_command(label="About", command=self.aboutOpen)
    self.menubar.add_cascade(label="Help", menu=self.helpmenu)

    self.connectMenu = tk.Menu(self.menubar, tearoff=0)
    self.connectMenu.add_command(label="Connect",
                                 command=lambda: SqlCommandClass.connect(self))
    self.connectMenu.add_command(
      label="Disconnect", command=lambda: SqlCommandClass.disconnect(self))
    self.menubar.add_cascade(label="Database", menu=self.connectMenu)

    self.recordMenu = tk.Menu(self.menubar, tearoff=0)

    #Object of the database class
    self.data = SqlCommandClass()
    self.root.title("Opener")
    self.root.geometry("450x300")

    self.pilotOpener = Button(self.root,
                              command=self.pilotWindowOpen,
                              text="Open Pilot Window")
    self.flightAttendantOpener = Button(self.root,
                                        command=self.flightAttendantWindowOpen,
                                        text="Open FA Window")

    self.pilotOpener.place(x=60, y=120)
    self.flightAttendantOpener.place(x=300, y=120)


# Methods for the Buttons

# Flight Attendant Button Methods (Kingsley & Andy)
