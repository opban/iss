#!/bin/python3

import json
import turtle
import urllib.request
import time

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("People in space: ", result['number'])

people = result['people']
for p in people:
  print(p['name'],'on',(p['craft']))
  
url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lot = float(location['longitude'])
print(lat, ',',lot)
  
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')
screen.register_shape('iss.gif')
iss=turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lot,lat)

cityDict = {}

#with open('worldcities.txt') as f: 
  #line = f.readline() 
  #while line: 
    #list1 = line.split() 
    #cityDict[list1[0]] = list1[1:3] 
    #line = f.readline()
#print(cityDict)

#cityname = input('Enter a city name')

#lat=float(cityDict[cityname][0])
#lon=float(cityDict[cityname][1])
#print (lat)
#print (lon)
lat=input()
lon=input()
url = "http://api.open-notify.org/iss-pass.json"
url = url + '?lat='+ str(lat) + '&lon=' + str(lot)
response = urllib.request.urlopen(url)
result = json.loads(response.read())


location = turtle.Turtle()
location.penup()
location.color('green')
location.goto(lat,lon)
location.dot(5)
location.hideturtle()


over = result['response'][1]['risetime']
style = ('Arial', 6, 'bold')


location.write(time.ctime(over), font=style)
