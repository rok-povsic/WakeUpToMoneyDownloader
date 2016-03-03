
import urllib
import urllib2
import datetime
import os
import mp3play

from bs4 import BeautifulSoup

LOCAL_FOLDER = r"E:/podcasts/wake_up_to_money/"

response = urllib2.urlopen("http://www.bbc.co.uk/podcasts/series/money")
page_source = response.read()

parsed_html = BeautifulSoup(page_source)

today_date_str = datetime.date.today().strftime("%Y%m%d")

found_online = False
for a in parsed_html.find_all('a', href=True):
    mp3_url = str(a['href'])
    if today_date_str in mp3_url:
        print mp3_url
        found_online = True
        break
if found_online:
	mp3_local = os.path.join(LOCAL_FOLDER, "wutm_" + today_date_str + ".mp3")
	urllib.urlretrieve(mp3_url, mp3_local)
else:
	mp3_local = "C:/Users/rock/Desktop/WakeUpToMOney Alarm/money_20150212-0613a.mp3"

#os.startfile(mp3_local)
mp3 = mp3play.load(mp3_local)
mp3.play()

import time
time.sleep(mp3.seconds())

mp3.stop()