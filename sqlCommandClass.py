"""
2/8/2023
Flight Attendant and Pilot GUI
APCSP
Sprint 1 Group 5
"""
from tkinter import *
import os
import mysql.connector

class SqlCommandClass():

  def connect(self):
        #All database connections and queries should be try/excepted
        try:
            #Connection object to local database in mysql
            self.conn = mysql.connector.connect(
              host = "192.168.0.116",
              port = 3306,
              user = "yoda",
              password = "jchs",
              database =""
            )

            #Cursor object for this database
            self.cursor = self.conn.cursor()

            return "Connected Properly."
        
        except mysql.connector.Error as e:
            return "Error Connecting: ", e 

    #Disconnecting from the database
  def disconnect(self):
        if(self.conn):
            self.conn.close()
            return "Connection Closed"



  def placeholder(self):
      pass

  
  def updatePilotTable(self):
    try:
      self.pilotIdHold = self.pilotId.get()
      self.pilotFnHold = self.pilotFirstName.get()
      self.pilotLnHold = self.pilotLastName.get()
      self.pilotPosHold = self.pilotVarPos.get()
      self.pilotPQ1Hold = self.pilotPlaneQualification1.get()
      self.pilotPQ2Hold = self.pilotPlaneQualification2.get()
      self.pilotPQ3Hold = self.pilotPlaneQualification3.get()
      
      self.pilotUpdater = self.c.execute("UPDATE pilots SET firstname = '"+ self.pilotFnHold +"', lastname ='"+ self.pilotLnHold +"',pos = '"+ self.pilotPosHold +"',aircraftTypeQualif1 ='"+self.pilotPQ1Hold +"',aircraftTypeQualif2 ='"+ self.pilotPQ2Hold +"'), aircraftTypeQualif3 = '"+ self.pilotPQ3Hold +"' ")
      self.pilotUpdater.commit()
      
      
    except:
      
      pass

      
  def deletePilotTable(self):
    try:
      self.pilotIdHold = self.pilotId.get()
      
      self.updateValues = (self.pilotIdHold)
      self.cursor.execute("""DELETE FROM pilots
WHERE id = ?""", self.updateValues)
      
    except:
      
      pass

    #insert Pilot
    #CREATE
    #Andy
    #used to creating the informations for the pilots
  def createP(self):
    try:
      q = (''' INSERT INTO pilot (first_name,
                                  last_name,
                                  company, 
                                  gender)''')
      self.cursor.execute(q,self.insertP)
      self.conn.commit()
      self.loadPilot
    except mysql.connector.error as e:
      return 'Error:' + e

    #READ
    #reading and selecting the pilots
  def loadP(self):
    try:
      q = ('''SELECT * FROM pilot''')
      self.cursor.execute(q)
      self.pilot = self.cursor.fetchall()
      return ""
    except mysql.connector.error as e:
     return 'Error:' + e 


    #UPDATE 
    #updating the pilots information if the wrong information is put or ohter information is needed
  def updateP(self, ID):
    try:
      q = ('UPDATE pilot SET gender='+self.updateP[1]+
          "', first_name='"+self.updateP[2]+
          "', last_name='"+self.updateP[3])
      self.cursor.execute(q)
      self.conn.commit()
      
    except mysql.connector.error as e:
      return 'Error, {}' .format(e)

    #DELETE 
    #deleting the pilots information
  def deleteP(self, id):
    try:
      q = ('DELETE FROM pilot WHERE ID='+str(id)+';')
      self.cursor.execute(q)
      self.conn.commit()
      self.loadP()
    except mysql.connector.error as e:
      return 'Error, {}'.format(e)


      
    # - Kingsley(start)
  # Inserting a flight attendant
    #CREATE
  def createFa(self):
      try:
        q = ("""INSERT INTO flightattendants (firstName, 
        lastName, 
             airlineId, pos)""")
        self.cursor.execute(q, self.insertFa)
        self.conn.commit()
        self.loadFlightAttendant
      except mysql.connector.error as e:
        return "Error:" + e
      #READ
  def loadFA(self):
    # Selects all records from the flight_attendant table and loads it into the gui
      try:
        q = ("SELECT * FROM flightattendants")
        self.cursor.execute(q)
        self.attendants = self.curor.fetchall()
        return ""
      except mysql.connector.error as e:
        return "Error:" + e

  # Kingsley(stop)

        #Andy
  #Update a flight attendant
  def updateFA(self, ID):
    try:
      q = ("UPDATE flightattendants SET firstName='"+self.updateFa[1]+
          "', lastName='"+self.updateFa[2]+
          "', airlineId="+str(self.updateFa[3]))
      +", pos='"+self.updateFa[4]+"' WHERE idFlightAttendant="+str(self.updateFa[0])
      self.cursor.execute(q)
      self.conn.commit()
      
    except mysql.connector.error as e:
      return "Error, {}" .format(e)

        #Andy and Leo
  #Deleting a flight attendant
  def deleteFA(self, id):
    try:
      q = ("DELETE FROM flightattendants WHERE idFlightAttendant="+str(id)+";")
      self.cursor.execute(q)
      self.conn.commit()
      self.loadFA()
    except mysql.connector.error as e:
      return "Error, {}".format(e)


      
  def __init__(self):
    self.attendants = []
    self.insertFa = ["","",0,"",]
    self.updateFa = [0,"","",0,""]

    self.pilots = []
    self.insertPilot = ["","","",""]
    self.updatePilot = [0, "", "", "" ""]


