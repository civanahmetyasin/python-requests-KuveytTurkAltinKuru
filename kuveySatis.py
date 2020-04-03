import requests
from bs4 import BeautifulSoup

from bokeh.driving import count
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
import datetime
from playsound import playsound

URL = 'https://www.kuveytturk.com.tr/finans-portali/'

playsound('alarm.mp3')

UPDATE_INTERVAL = 2000
ROLLOVER = 10800 # Number of displayed data points

source = ColumnDataSource({"x": [], "y": []})

@count()
def update(x):
    tarihSaat = datetime.datetime.now()
    verileriLogla = open("%d" % tarihSaat.year + "-" +"%d" % tarihSaat.month + "-" + "%d" % tarihSaat.day + ".txt","a")
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    veriler = soup.find(class_='finans-portali')
    sinif = veriler.find_all('p')

    bankaAlis = sinif[6].prettify().split('\n')[1]
    bankaAlis = round(float(bankaAlis.replace(',','.')),2)
    
    bankaSatis = sinif[7].prettify().split('\n')[1]
    bankaSatis = round(float(bankaSatis.replace(',','.')),2)
    
    print("%.2f" % bankaAlis + " - " +"%.2f" % bankaSatis )

    if bankaSatis < 333.5:
        playsound('alarm.mp3')
        pass

    if bankaAlis > 340.0:
        #playsound('alarm.mp3')
        pass


    verileriLogla.write("%.2f" % bankaAlis +"+"+ "%.2f" % bankaSatis + "\n")
    verileriLogla.close()
    
    source.stream({"x": [x], "y": [bankaSatis]}, rollover=ROLLOVER)

p = figure(title="BANKA SATIS", plot_width=1800, plot_height=400,tools = "pan,wheel_zoom,box_zoom,reset,xpan,ypan,xwheel_zoom,ywheel_zoom,crosshair,hover,save")
p.background_fill_color = 'black'
p.background_fill_alpha = 0.3
p.line("x", "y", source=source,color='navy')

doc = curdoc()
doc.add_root(p)
doc.add_periodic_callback(update, UPDATE_INTERVAL)