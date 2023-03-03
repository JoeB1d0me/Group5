import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import Button
import os
import mysql.connector
from sqlCommandClass import SqlCommandClass


class flightAttendantWindow():

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
