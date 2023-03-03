"""
2/8/2023
Flight Attendant and Pilot GUI
APCSP
Sprint 1 Group 5
"""
from tkinter import *
import sqlite3
from sqlCommandClass import SqlCommandClass
from tableGui import TableGui


def main():
  #runs gui which contains db class
  #No need to initialize the db class
  TableGui()


if (__name__ == "__main__"):
  main()
