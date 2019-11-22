# -*- coding: utf-8 -*-
"""
Data extraction from train.csv

Created on Thu Nov 21 20:38:27 2019

@author: nikhil
"""
import csv
import pandas
print("Hello NFL")

#colnames = ['GameId','PlayId','Team','X','Y','S','A','Dis','Orientation','Dir','NflId','DisplayName','JerseyNumber','Season','YardLine','Quarter','GameClock','PossessionTeam','Down','Distance','FieldPosition','HomeScoreBeforePlay','VisitorScoreBeforePlay','NflIdRusher','OffenseFormation','OffensePersonnel','DefendersInTheBox','DefensePersonnel','PlayDirection','TimeHandoff','TimeSnap','Yards','PlayerHeight','PlayerWeight','PlayerBirthDate','PlayerCollegeName','Position','HomeTeamAbbr','VisitorTeamAbbr','Week','Stadium','Location','StadiumType','Turf','GameWeather','Temperature','Humidity','WindSpeed','WindDirection']
#data = pandas.read_csv('C:\Users\nikhil\Documents\GitHub\big_data_bowl\resources\train.csv', names=colnames)


# open the file in universal line ending mode 
with open('C:\\Users\\nikhil\\Documents\\GitHub\\big_data_bowl\\resources\\train.csv','rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

# extract the variables you want
gameid = data['GameId']
print("First game: "+ gameid[0])
#print(gameid[0])


