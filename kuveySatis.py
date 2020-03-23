import requests
from bs4 import BeautifulSoup

from bokeh.driving import count
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
import datetime

URL = 'https://www.kuveytturk.com.tr/finans-portali/'



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


    verileriLogla.write("%.2f" % bankaAlis +"+"+ "%.2f" % bankaSatis + "\n")
    verileriLogla.close()
    
    source.stream({"x": [x], "y": [bankaSatis]}, rollover=ROLLOVER)

p = figure(plot_width=1800, plot_height=400)
p.line("x", "y", source=source,color='navy')

doc = curdoc()
doc.add_root(p)
doc.add_periodic_callback(update, UPDATE_INTERVAL)