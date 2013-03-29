#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# json end point for latrobe valley
bom = requests.get('http://www.bom.gov.au/fwo/IDV60801/IDV60801.94891.json')
#using weatherzone for current cond
weatherzone = requests.get('http://www.weatherzone.com.au/vic/w-and-s-gippsland/traralgon')

data = bom.json()
soup = BeautifulSoup(weatherzone.text)

current = data["observations"]["data"][0]

temp = current['air_temp']
hum = current['rel_hum']

current_cond = soup.find(id="top_fcast_icon")['alt']

with open('/tmp/tmux-powerline/weather_yahoo.txt', 'w') as f:
	f.write("%s°C, %s%%\n" % (temp, hum))

#"""☽☾☀☼☂☔☃❅☁⚡☈♨﹌〰⚐⚑☾〇"""
